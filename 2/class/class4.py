class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name
        self.level = level
        self.stamina = level * 20
        self.exp = exp
        self.itembox = itembox

    # デバッグなど、人間が見やすいクラスの文字列表現を返す
    def __str__(self):
        return (self.name + '(Lv.' + str(self.level) + ')')


hero = Character('勇者', 16, 0, {'かいふくやく': 2})
print(str(hero))
