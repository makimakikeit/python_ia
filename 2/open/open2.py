"""
変数に入っていないため
説明文として
使用できる。
コメントアウトの代わりに
"""

import csv


class SalesForText:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_data_length(self):
        """ファイルの行数を返す"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            count = 0
            for line in file:
                count += 1
            return count

    def get_total_sales(self):
        """売上の合計を返す"""
        sales_total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                sales = int(row)
                sales_total += sales
        return sales_total

    def get_total_surplus(self):
        """黒字の合計を返す"""
        sales_plus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                sales = int(row)
                if sales >= 0:
                    sales_plus += sales
        return sales_plus

    def get_total_deficit(self):
        """赤字の合計を返す"""
        sales_minus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                sales = int(row)
                if sales < 0:
                    sales_minus += sales
        return sales_minus


class SalesForCSV(SalesForText):

    def get_total_sales(self):
        """売上の合計を返す"""
        sales_total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # ['2023', '1', '200', 'Aさん']
                sales_price = int(row[2])
                sales_total += sales_price
            return sales_total

    def get_total_surplus(self):
        """黒字の合計を返す"""
        sales_total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                sales_price = int(row[2])
                if sales_price >= 0:
                    sales_total += sales_price
            return sales_total

    def get_total_deficit(self):
        """赤字の合計を返す"""
        sales_total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                sales_price = int(row[2])
                if sales_price < 0:
                    sales_total += sales_price
            return sales_total


sales = SalesForCSV('sales.csv')
total_sales = sales.get_total_sales()
total_surplus = sales.get_total_surplus()
total_deficit = sales.get_total_deficit()
count = sales.get_data_length()
print(total_sales, total_surplus, total_deficit)
print(f'件数:{count}')