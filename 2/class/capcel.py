class Character:

    def __init__(self, name, level):
        self.name = name
        # levelは外からアクセスしないで欲しい
        self._level = level # アンスコ１つの場合は、アクセスしようと思えばできる
        self.__level = level # アンスコ２つの老婆には、アクセスできない

        """
        先頭にアンダースコア２つを他言語でいうprivate
        1つをprotected属性として、運用する方々も多い。
        """

    # 外からは干渉できないメソッドを作れる
    def _speak(selfself):
        print()

hero = Character('勇者', 1)
hero.__level = 2

print(hero._level)