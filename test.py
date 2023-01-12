
# -------------------------------------------------1

# nums = [2, 7, 11, 15]
# target = 9
#
#
# def two_sum(l1, target1):
#     for i in range(len(l1)):
#         for m in range(len(l1)):
#             if l1[m] + l1[i] == target1 and m != i:
#                 return [i, m]
#
#
# print(two_sum(nums, target))

# -------------------------------------------------2

# romans = {"I": 1,
#           "V": 5,
#           "X": 10,
#           "L": 50,
#           "C": 100,
#           "D": 500,
#           "M": 1000
#           }
# input_string = 'IXCMIVLVIII'
# words = [input_string[i] for i in range(len(input_string))]
#
#
# def translator_romans(rome_nums):
#     r_indexes = list(romans)
#     finish_num = 0
#
#     for n in range(len(rome_nums)):
#         try:
#             if n + 1 != len(rome_nums):
#                 if r_indexes.index(rome_nums[n]) in [0, 2, 4] and
#                 (romans[rome_nums[n + 1]] / romans[rome_nums[n]]) in [5, 10]:
#                     rome_nums[n] = (rome_nums[n] + rome_nums[n + 1])
#                     del rome_nums[n + 1]
#                     print(rome_nums)
#         except:
#             pass
#
#     for m in range(len(rome_nums)):
#         if len(rome_nums[m]) == 1:
#             finish_num += romans[rome_nums[m]]
#         else:
#             finish_num += romans[rome_nums[m][1]] - romans[rome_nums[m][0]]
#     return finish_num
#
#
# print(translator_romans(words))


# q = input("sdlfslkf")

#-------------------------------------------------------3

strs = [""]

import math
def min_num(strs):
    t = math.inf
    for i in strs:
        if len(i) < t:
            t = len(i)
    return t

def longest_prefix(strs):
    # prefix = ""
    # for i in range(min_num(strs)):
    #     common_letter = strs[0][i]
    #     for n in strs[1:]:
    #         if common_letter != n[i]:
    #             return prefix
    #     prefix += common_letter
    # return prefix

    prefix = ""
    for i, c in enumerate(strs[0]):
        for n in strs[1:]:
            if len(n) < i + 1 or c != n[i]:
                return prefix
        prefix += c

    return prefix
print(longest_prefix(strs))




