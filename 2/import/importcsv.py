import csv
# pandas

# utf-8-sigを使うと、WindowsのエクセルでCSVを綺麗に表示でき
# 通常のテキストディタでも、文字化けせずにCSVを表示できる
# BOM付きUTF-8と呼ぶことも
with open('data.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow('\n')
    writer.writerow(['スライム', '15', '体液'])
    writer.writerow(['ゴーレム', '17', '拳'])
    writer.writerow(['ゴブリン', '16', '棍棒'])

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
