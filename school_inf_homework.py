

def age_printer(age):
    l = int(str(age)[-1])
    if l > 4 or not l or 10 < age < 20:
        return "Вам {} лет".format(age)
    if l < 5:
        if l == 1:
            return "Вам {} год".format(age)
        return "Вам {} года".format(age)


n = 0
while n < 100:
    n += 1
    print(age_printer(n))









