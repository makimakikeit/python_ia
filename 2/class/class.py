class Character:
    name=''

    # メソッドの第一引数は、ほぼ必ず、インスタンス自信が渡される
    def speak(self, comment):
        print(self.name + ':' + comment)

# Characterのインスタンスを、taroに代入
# selfとtaroは、全く同じもの
taro = Character() # インスタンス化
taro.name = 'ジロー'
# print(taro.name)
taro.speak(comment='ハロー')

# #
# taro.name = 'タロー'
# taro.last_name = 'タナカ'
# print(taro.name)
# print(taro.last_name)