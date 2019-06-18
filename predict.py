# -*- coding:utf-8 -*-


from bert import Ner

model = Ner('output/')
output = model.predict('2 0 1 4 年 新 的 开 始 ，王 兴 很 高 兴')
print(output)
