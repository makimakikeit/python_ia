# python ファイル名 を実行した場所から見て、ファイルをimportする
# python main.py と実行する例ならば、同じ階層にfizzbuzz_func.pyが必要

# モジュールのみimport
import sample

# fizzbuzz_func.pyの、fizzbuzz関数を呼んでいる
sample.fizzbuzz(1, 100)


# from モジュール import 関数やクラス
from sample import fizzbuzz

fizzbuzz(1, 101)