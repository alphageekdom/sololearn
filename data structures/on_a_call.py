class CallCenter:
    
    def __init__(self):
        self.customers = []
    
    def is_empty(self):
        self.customers == []
    
    def add(self, x):
        self.customers.insert(0, x)
    
    def next(self):
        self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

time = 0
while True:
    
    if c.is_empty():
        break
    
    item = c.next()
    
    if item == "general":
        time += 5
    
    if item == "technical":
        time += 10


print(time)