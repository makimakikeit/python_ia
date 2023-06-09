class Character:

    # ダンダーイニット。特殊メソッドと呼ぶ
    def __init__(self, name):
        self.name = name        # キャラクター名

    def speak(self, comment):
        print(self.name + ':' + comment)

# インスタンスの属性は、基本的にはコンストラクタ__int__で行う
# 他のメソッドないから、インスタンスの属性を設定することもあります
# # taro.name = 'ziro' のように外側から設定することは少ないです
taro = Character('tarou')
taro.speak(comment='ハロー')

# self.nameと同じ。結果的に、'tarou'が取得できる
print(taro.name)
