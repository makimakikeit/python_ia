japanese_to_english = {
    # キー：バリュー
    '水': 'water',
    '風': 'wind',
    '土': 'soil',
    '火': 'fire',
    1: 'one',
    (1, 1, 1): 5,
    (6, 6, 6): 3,
}
print(japanese_to_english['水'])
print(japanese_to_english[1])
print(japanese_to_english[(1,1,1)])