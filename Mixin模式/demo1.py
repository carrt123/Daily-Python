"""
Mixin 通常被翻译成”混入” 模式

Mixin 类提供了一些其他类可能需要使用的功能，但不会单独使用， 将许多小功能封装进来
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('Bob', 20)

# print(s["name"]) # 出现报错
"""------------------------------------------------------------"""


# 解决以上问题， 谁继承StudentMixin 就有它的方法
class MapMixin(object):
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class DictMixin:
    def to_dict(self):
        return self.__convert_dict(self.__dict__)

    def __convert_dict(self, attrs: dict):
        result = {}
        for key, value in attrs.items():
            result[key] = self.__convert_value(value)

        return result

    def __convert_value(self, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self.__convert_dict(value)
        elif isinstance(value, list):
            return [self.__convert_value(item) for item in value]
        else:
            return value

import json
class JSONMixin():
    def to_json(self):
        return json.dumps(self.to_dict())


class Student(DictMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# {"name": "Bob", "age": 20, "class": "{"name":"alice"}"}
class Student2(MapMixin, DictMixin, JSONMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student2('Bob', 20)

print(s["name"])
print(s.to_dict())
print(s.to_json())
