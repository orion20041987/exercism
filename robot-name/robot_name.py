import random


class Robot:
    def __init__(self):
        self.name = self.name_generator()

    def name_generator(self):
        random.seed()
        letter_pool = []
        for i in range(65, 91):
            letter = chr(i)
            letter_pool.append(letter)
        counter = 0
        name = []
        while counter < 2:
            name.append(random.choice(letter_pool))
            counter += 1

        while 2 <= counter < 5:
            name.append(str(random.randint(0, 9)))
            counter += 1

        ST = ''.join(name)
        return ST

    def reset(self):
        self.name = self.name_generator()
