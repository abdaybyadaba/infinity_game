






# 1st

# list = []
# list1 = [0]

# def g(listp, list1p):
#     list = listp
#     list1 = list1p
#     f = []
#     while True:
#         if list and list1:
#             if list[0] < list1[0]:
#                 f.append(list[0])
#                 list.pop(0)
#             else:
#                 f.append(list1[0])
#                 list1.pop(0)
#         else:
#             f += (list[0:]) if not list1 else (list1[0:])
#             return f
#
# print(g(list, list1))

#2nd

lst = [1, 2, 3, 6, 8]
valueq = 6

def h(lst, valueq):
    if valueq in lst:
        return lst.index(valueq)

    if lst[0] > valueq:
        return 0

    for i in range(len(lst)):
        if i + 1 < len(lst):
            if lst[i] < valueq < lst[i + 1]:
                return i + 1
        else:
            return i + 1

print(h(lst, valueq))