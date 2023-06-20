from django import forms
from .models import Goods


class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')

    # clean_フィールド名という名前をつける
    def clean_image(self):
        # フィールドの値 = self.cleand_data.get('フィールド名')
        # 辞書のgetメソッドを使っている(この場合、デフォルト値がFalse)
        image = self.cleaned_data.get('image', False)
        # 画像がアップロードされていた場合
        if image:
            # ImageFieldとFildFieldには、.sizeという属性がある
            if image.size > 10 * 1024:
                # clean_メソッドで、何かエラ０を出したいならば
                # raise forms.ValidationError('エラーメッセージ名')
                raise forms.ValidationError("ファイルサイズが大きすぎます")
            # return self.clean_data.get('image')で取得した値
            return image

    def clean_name(self):
        name = self.cleaned_data.get('name', False)
        # NGワードが、商品名に含まれていないかチェック
        if 'NGワード' in name:
            raise forms.ValidationError("NGワードがふくまれていました")
        return name


class GoodsUpdateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')

