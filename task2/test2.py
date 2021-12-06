import unittest

def calculate(m:int, n:int, p:list[int]):
    a=[int(elem) for elem in p.split()]
    x=0
    b=[-1 for i in range(1002)]
    s=[-1 for i in range(1002)]
    s[0]=0
    for i in range(0,n):
        for j in range(0,m):
            if s[j]==-1: continue
            d=a[j%m]
            if b[0]<s[j]:
                b[0]=s[j]
            if b[(j+1)%m]<=s[j]+d:
                b[(j+1)%m]=s[j]+d
        s=b[:]
    for j in range(m):
        x=max(s[j],x)
    return x

class CalculateTestCase(unittest.TestCase):
    def test_calculate_1(self):
      truth = calculate(3,3,'6 2 3')
      self.assertEqual(truth, 12)
    def test_calculate_2(self):
      truth = calculate(3,3,'2 4 8')
      self.assertEqual(truth, 14)
if __name__ == "__main__":
  unittest.main()