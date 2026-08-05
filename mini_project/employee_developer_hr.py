class Employee:
    def __init__(self, eid, ename, eage):
        self.eid = eid
        self.ename = ename
        self.eage = eage


class Dev(Employee):
    def __init__(self, eid, ename, eage, did, dname, dexp):
        super().__init__(eid, ename, eage)
        self.did = did
        self.dname = dname
        self.dexp = dexp


class HR(Dev):
    def __init__(self, eid, ename, eage, did, dname, dexp, hrname, hrage):
        super().__init__(eid, ename, eage, did, dname, dexp)
        self.hrname = hrname
        self.hrage = hrage

    def info(self):
        print(f"Emp_name:{self.ename}, dev_name:{self.dname}, HR_name:{self.hrname}")


if __name__ == "__main__":
    hr1 = HR(1, "emp", 25, 2, "dev", 3, "hr", 28)
    hr1.info()
