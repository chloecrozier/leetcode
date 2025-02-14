# https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2025-02-14
class ProductOfNumbers:
    def __init__(self):
        self.nums = []
        self.prod = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = []
        else:
            if self.prod:
                product = num * self.prod[-1]
                self.prod.append(product)
            else:
                self.prod.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.prod) < k:
            return 0
        elif len(self.prod) == k:
            return self.prod[-1]
        else:
            return self.prod[-1] // self.prod[len(self.prod) - 1 - k]
