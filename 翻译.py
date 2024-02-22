# encoding: utf-8
from translate import Translator
# 以下是将简单句子从英语翻译中文
# translator = Translator(to_lang="chinese")
# translation = translator.translate('hello!')
# print(translation)
# 在任何两种语言之间，中文翻译成英文
# translator = Translator(from_lang='chinese', to_lang='english')
# translation = translator.translate('我是中国人')
# print(translation)
translation = '你吃了吗'

for i in range(1, 21):
    translator = Translator(from_lang='chinese', to_lang='english')
    translation0 = translator.translate(translation)
    translator = Translator(from_lang='english', to_lang='chinese')
    translation = translator.translate(translation0)
    print(translation)
