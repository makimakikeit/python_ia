# python ファイル名を実行した場所から見て、ファイルをimportする

# モジュールのみimport
import sample


# python ファイル名 を実行した場所から見て、ファイルをimportする
# python main.py と実行する例ならば、同じ階層にfizzbuzz_func.pyが必要

# モジュールのみimport
import sample

sample.fizzbuzz(1, 101)


# from モジュール import 関数
from sample import fizzbuzz

fizzbuzz(1, 101)
