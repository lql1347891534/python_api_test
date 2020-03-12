import json

'''
    1、序列化：将Python格式转换成json格式    dumps(str)  dump(file)
    2、反序列化：将json格式转换成Python格式  loads(dict)  load(file)
'''

# 反序列化：将json格式转换成Python格式  loads(str)  load(file)
s='{"msg":"找不到用户","rc":1,"data":null}'
print(json.loads(s))
print(type(json.loads(s)))
print(type(s))

# 序列化：将Python格式转换成json格式    dumps(str)  dump(file)
s2={"msg":"找不到用户","rc":1,"data":None}
print(json.dumps(s2,ensure_ascii=False))
print(type(json.dumps(s2)))
print(type(s2))