from django.db import models


class StaffInformation(models.Model):
    staff_name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', blank=True, null=True)
    address = models.CharField('住所', blank=True, null=True, max_length=100)
    birthday = models.DateTimeField('誕生日', blank=True, null=True)
    hire_date = models.DateField('入社日', blank=True, null=True)
    at_desk = models.BooleanField('出社状態', default=False)

    def __str__(self):
        return self.staff_name


class Department(models.Model):
    name = models.CharField('部署名', unique=True, max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('書籍名', max_length=100)
    management_code = models.CharField('管理番号', unique=True, max_length=50)

    def __str__(self):
        return self.name


class Staff(models.Model):
    # モデルのフィールドが多すぎるとき、一部のフィールドが頻繁にアクセスルツ場合は
    # その頻繁にアクセスするフィールを別のモデルとして定義し、
    # 必要になっった時だけ、OneToOneで紐づいたモデルの情報にアクセスするということをよくやる
    name = models.CharField('ビジネスネーム', max_length=100)
    # １対１で、StaffInfomationと紐づく
    information = models.OneToOneField(
        # 紐づいた先のデータが削除される場合、こちらの情報も削除される
        StaffInformation, on_delete=models.CASCADE,
        verbose_name='社員情報', null=True, blank=True
    )

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        verbose_name="所属部署", null=True, blank=True
    )

    # 多対多
    rented_books = models.ManyToManyField(
        Book, verbose_name="借りている本", blank=True, null=True
    )

    def __str__(self):
        return self.name
