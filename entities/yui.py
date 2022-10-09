






class A:
    def __init__(self):
        pass


class B:
    def __init__(self):
        pass

d = {'A': A, 'B': B}
# print(type(d['A']()))


# -9(b-a) = -9(-a + b ) = -9 (-1)(a-b) = 9 (a-b)
# 9(b-a) = 9 (-1) (a-b) = -9(a-b)










































class Mob:
    def __init__(self):
        print("Mob")

    def update(self):
        print("upd")

    def destroy(self):
        print("in destroy")

class StaticMob(Mob):
    def __init__(self):
        print("sm")

    def update(self):
        print("static mob upd")
        self.destroy()

class Box(StaticMob):
    pass

b = Box()
b.update()




def print_mro(T):
    print(*[c.__name__ for c in T.mro()], sep=' -> ')

print_mro(b)