class ADD():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value + 1

x = ADD(10)
y = ADD(20)
print(x + y)

# output: 31 
