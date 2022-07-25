class Singleton():

    __instance = None
    __has_init = False

    def __new__(cls):
        if cls.__instance is None:
            print('创建对象')
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        if not self.__has_init:
            print('对象初始化')
            self.type = '猫'
            self.__has_init = True

s1 = Singleton()
s1.type = '动漫人物'
print(s1.type)

s2 = Singleton()
print(s2.type)
