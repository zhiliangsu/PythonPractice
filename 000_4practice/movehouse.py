class Item():
    '''furniture class'''
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return "家具为%s, 占用面积%d" % (self.type, self.area)


class Home():
    '''Home class'''
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.items = []

    # def __str__(self):
    #     return '房子在：%s， 面积为%d， 剩余面积为%d' % (self.address, self.area, self.free_area)

    def __str__(self):
        # 房子在xx, 面积为xx, 包含的家具有: 双人床, 冰箱
        result_str = "房子在:%s, 面积为%d, 剩余面积为%d" % (
            self.address, self.area, self.free_area)
        # 判断是否包含家具
        if len(self.items) > 0:  # 有家具
            result_str += ",包含的家具有:"
            # 遍历家具列表,取出每一个家具(对象),然后拼接家具的type属性
            for item in self.items:
                result_str += item.type + ","
            # result_str = result_str.rstrip(",")
        return result_str

    def add_item(self, item):
        result_area = self.free_area - item.area
        if result_area >= 0:
            print('%s 添加成功' % item.type)
            self.items.append(item)
            self.free_area -= item.area
        else:
            print('房子面积不足，%s 添加失败' % item.type)


item1 = Item("双人床", 4)
print(item1)

# 创建房子
fangzi1 = Home("北京盘古大观", 200)
print(fangzi1)

# 添加家具
fangzi1.add_item(item1)
print(fangzi1)

# 再添加一个家具
item2 = Item("冰箱", 1)
print(item2)
fangzi1.add_item(item2)
print(fangzi1)

item3 = Item("篮球场", 420)
print(item3)
fangzi1.add_item(item3)
print(fangzi1)



