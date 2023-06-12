class Character:

    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def speak(self, comment):
        print(self.name + ':' + comment)

    def show_profile(self):
        print(self.name)
        print(self.age)
        print(self.speed)

class Healer(Character):

    # __init__も上書きできます
    def __init__(self, name, age, speed, power):
        # super().基底クラスのメソッド名
        super().__init__(name, age, speed)
        self.power = power

    # オーバーライド
    def speak(self, comment):
        super().speak(comment)
        # 喋ったあとに、回復もするように上書きした
        self.healing()

    # 新規追加のメソッド
    def healing(self):
        print(f'{self.name}は回復した！')


taro = Healer(name='勇者', power=1)  # インスタンスか
taro.speak(comment='ハロー')

class Magician(Character):

    # __init__も上書きできます
    def __init__(self, name, age, speed, magic_power):
        super().__init__(name, age, speed)
        self.magic_power = magic_power

    def show_profile(self):
        # print(self.name)
        # print(self.age)
        # print(self.speed)
        # 上の3行は、Charcterのshow_profileメソッドで同様のことをしているので、
        # それを呼び出すほうが楽
        super().show_profile()
        print(self.magic_power)