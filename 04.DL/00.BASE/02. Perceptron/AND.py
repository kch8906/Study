# def AND(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1*w1 + x2*w2
#     if tmp <= theta:
#         return 0
#     elif tmp > theta:
#         return 1

# print(AND(0, 0))
# print(AND(1, 0))
# print(AND(0, 1))
# print(AND(1, 1))



# import numpy as np
# x = np.array([0, 1])
# w = np.array([0.5, 0.5])
# b = -0.7
# print(w * x)
# print(np.sum(w * x))
# print(np.sum(w * x) + b)

from re import A
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w)+b

    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(AND(1, 0))
    print(AND(1, 1))