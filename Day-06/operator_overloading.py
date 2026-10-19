class Number:
    def __init__(self, n):
        self.n = n

    def __sub__(self, num):  #operators sub add mul etc
        return self.n - num.n

n = Number(3)
m = Number(2)

print(n - m)  # Output: 1