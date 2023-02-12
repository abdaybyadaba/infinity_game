

n = 144


def square_root_counter(n):
    # m = 0
    # while m ** 2 <= n:
    #     m += 1
    # return m - 1
    x_prev = n
    x_curr = n / 3
    eps = 1
    n_iter = 0
    while abs(x_curr - x_prev) > eps:
        x_prev = x_curr
        x_curr = (x_prev + n / x_prev) / 2
        n_iter += 1

    return x_curr, n_iter
print(square_root_counter(n))