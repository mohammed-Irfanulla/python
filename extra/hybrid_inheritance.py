class A:
    def prnta(self):
        print("Im from A")


class B(A):
    def prntb(self):
        print("Im from B")


class C:
    def prntc(self):
        print("Im from C")


class D(B, C):
    def prntd(self):
        print("Im from D")


if __name__ == "__main__":
    d1 = D()
    d1.prnta()
    d1.prntb()
    d1.prntc()
    d1.prntd()
