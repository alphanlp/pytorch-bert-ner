# -*- coding:utf-8 -*-


from bert import Ner

model = Ner('models/')
output = model.predict('2 0 1 4 年 新 的 开 始 ，胡 阿 沛 很 高 兴')
print(output)
