import numpy as np
import AND
import NAND_OR


def XOR(x1, x2):
    s1 = NAND_OR.NAND(x1, x2)
    s2 = NAND_OR.OR(x1, x2)
    y = AND.AND(s1, s2)
    return y


if __name__ == "__main__":
    print(XOR(0, 0))
    print(XOR(1, 0))
    print(XOR(0, 1))
    print(XOR(1, 1))