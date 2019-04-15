# -*- coding: utf-8 -*-
# 例えばターミナルに Hello, world! と印字するプログラムを書くという課題を考えてみた場合、
# 効率/わかりやすさ/簡潔さなどを無視しても良いと仮定したら、
# 何通りのプログラムを書けますか?
# 
# ちょっとしたゲームだと思って挑戦してみてください。

# Usage:
#    $ python hellos.py

# 以下はあくまで例です。

def hello_print():
    '''
    ただ単に`print`関数を使うだけ
    '''
    print("Hello, world!")

def hello_args(hello, world):
    '''
    引数で必要な文字列を受け取り、それらを組み合わせて印字
    '''
    print(hello + ', ' + world + '!')

def hello_if():
    '''
    `if`文が成功したら印字
    '''
    if True:
        print("Hello, world!")

def hello_call():
    '''
    `Hello, world!`を印字する別の関数を呼び出す
    '''
    hello_print()

def hello_arr():
    '''
    配列から文字列を生成して印字
    '''
    hello_chars = ['H', 'e', 'l', 'l', 'o']
    hello = "".join(hello_chars)
    print("{}, world!".format(hello))

def hello_fmt():
    '''
    `format`関数を積極的に使用。書式内に変数を使う
    '''
    print("{hello}, {world}!".format(hello="Hello", world="world"))

def hello_io():
    '''
    一度ファイルに書き出した内容を再度読み込んで印字
    '''
    txt = "./hello_io.txt"
    with open(txt, "w") as f:
        f.write("Hello, world!")

    with open(txt, "rt") as f:
        hello_world = f.read()
        print(hello_world)

def hello_json():
    '''
    JSON形式の文字列を読み込み、その中から`Hello, world!`を取り出して印字
    '''
    import json
    raw_data = '["Hello, world!"]'
    arr = json.loads(raw_data)
    print(arr[0])

def main():
    '''
    プログラミが起動するとこの関数が最初に呼ばれる
    以降、順に印字を行う関数を呼び出す
    '''
    hello_print()
    hello_args("Hello", "world")
    hello_if()
    hello_call()
    hello_fmt()
    hello_io()
    hello_json()

if __name__=='__main__':
    main()

