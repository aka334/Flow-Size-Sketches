import random

class ActiveCounter:
    def __init__(self, num_bits=16, exp_bits=16):
        self.num_bits = num_bits
        self.exp_bits = exp_bits
        self.c_n = 0
        self.c_e = 0
        self.max_val = 2 ** num_bits - 1

    def increase(self):
        probability = 1 / (2 ** self.c_e)
        if random.random() < probability:
            self.c_n += 1
            if self.c_n > self.max_val:
                self.c_n >>= 1
                self.c_e += 1

    def get_value(self):
        return self.c_n * (2 ** self.c_e)


if __name__ == "__main__":
    counter = ActiveCounter()

    for _ in range(1000000):
        counter.increase()

    with open("activecount.txt", "w") as file:
        file.write(f"Final value of the active counter: {counter.get_value()}")
