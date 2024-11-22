import random

class Apple:
    counter = 0
    total_weight = 0

    def __init__(self, weight):
        self.weight = weight
        Apple.total_weight += weight
        Apple.counter += 1

while Apple.counter < 1000 and Apple.total_weight < 300:
    apple = Apple(random.uniform(0.2, 0.5))

print('A limit has been reached. The order details:')
print('# of apples:', Apple.counter)
print('total weight:', round(Apple.total_weight, 2))
