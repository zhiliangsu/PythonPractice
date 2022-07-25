class Gun():
    def __init__(self, model, damage):
        self.model = model
        self.damage = damage
        self.bullet_count = 0

    def __str__(self):
        return '%s: %d，剩余子弹：%d' % (self.model, self.damage, self.bullet_count)

    def add_bullets(self, count):
        self.bullet_count += count
        print('装填子弹完成，剩余子弹数量：%d' % self.bullet_count)

    def shoot(self, enemy):
        if self.bullet_count <= 0:
            print('子弹不足，无法射击')
            return

        self.bullet_count -= 1
        print('发射1颗子弹，剩余：%d' % self.bullet_count)

        if enemy is not None:
            enemy.hurt(self)


class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.gun = None

    def __str__(self):
        if self.hp <= 0:
            return '%s 已经挂了' % self.name

        if self.gun is None:
            return '%s[%d] 没有武器' % (self.name, self.hp)

        return '%s[%d] 武器：{%s}' % (self.name, self.hp, self.gun)

    def hurt(self, enemy_gun):
        self.hp -= enemy_gun.damage
        if self.hp <= 0:
            print('%s 被 %s 击毙！！' % (self.name, enemy_gun.model))
        else:
            print('%s 被 %s 击中，剩余血量：%d' % (self.name, enemy_gun.model, self.hp))

    def fire(self, enemy):
        if self.gun is None:
            print('%s 没有武器，请先装配武器' % self.name)
            return
        
        if self.gun.bullet_count <= 0:
            self.gun.add_bullets(10)

        print('%s 正在向 %s 开火...' % (self.name, enemy.name))
        self.gun.shoot(enemy)



def test():
    ak47 = Gun('AK47', 50)
    # print(ak47)

    # ak47.add_bullets(10)
    # print(ak47)

    # ak47.shoot(None)
    # ak47.add_bullets(50)
    # ak47.shoot(None)
    # print(ak47)
    # print('-' * 10 + ' 枪类测试完成 ' + '-' * 10)

    policeman = Player('警察', 100)
    print(policeman)
    badman = Player('匪徒', 100)
    print(badman)
    print('-' * 10 + ' 玩家就绪 ' + '-' * 10)

    policeman.gun = ak47
    # print(policeman)
    # print('-' * 10 + ' 玩家类属性准备完成 ' + '-' * 10)

    # badman.hurt(ak47)
    # badman.hurt(ak47)
    # print(badman)
    # print('-' * 10 + ' 受伤方法测试完成 ' + '-' * 10)
    
    # policeman.fire(badman)
    # policeman.fire(badman)
    # print(policeman)
    # print(badman)
    while badman.hp > 0:
        policeman.fire(badman)

    print('-' * 10 + ' 交战结果 ' + '-' * 10)
    print(policeman)
    print(badman)
    

if __name__ == '__main__':
    test()