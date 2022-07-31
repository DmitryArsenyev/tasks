

class MetaClass(type):
    # выделение памяти для класса
    def __new__(cls, name, bases, dict):
        print("Создание нового класса {}".format(name))
        return type.__new__(cls, name, bases, dict)

    # инициализация класса
    def __init__(cls, name, bases, dict):
        print("Инициализация нового класса {}".format(name))
        return super(MetaClass, cls).__init__(name, bases, dict)


SomeClass = MetaClass("SomeClass", (), {})

# обычное наследование
class Child(SomeClass):
    def __init__(self, param):
        print(param)

# получение экземпляра класса
obj = Child("Hello")



class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)



