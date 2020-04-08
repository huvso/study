class Duck:
    def quack(self):
        print('꽥꽥')

    def feathuers(self):
        print('오리에게 흰색, 회색 깃털이 있습니다.')

    def fly(self):
        print('오리가 날았지만 곧 떨어집니다.')


class Person:
    def quack(self):
        print('이 사람이 오리를 흉내냅니다.')

    def feathuers(self):
        print('사람은 바닥에서 깃털을 주어서 보여줍니다.')


def in_the_forest(duck):
    duck.quack()
    duck.feathuers()
    duck.fly()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


if __name__ == "__main__":
    game()

# result:
# 꽥꽥
# 오리에게 흰색, 회색 깃털이 있습니다.
# 오리가 날았지만 곧 떨어집니다.
# 이 사람이 오리를 흉내냅니다.
# 사람은 바닥에서 깃털을 주어서 보여줍니다.
# AttributeError: 'Person' object has no attribute 'fly'
