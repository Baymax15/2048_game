import random as r


class board:
    def __init__(self, size, data=False):
        self.size = size
        self.data = [x[:] for x in data] if data else [
            [0] * size for _ in range(size)]

    def copy(self):
        return [[x[i] for i in range(self.size)] for x in self.data]

    def match(self, another):
        return True if self.data == another.data else False

    def place(self, count=1, val=r.choice([4, *[2] * 9])):
        x = 0
        while x < count:
            i, j = [r.randrange(self.size) for _ in [0] * 2]
            if self.data[i][j] == 0:
                self.data[i][j] = val
                x += 1

    def state(self):
        for x in self.data:
            if 2048 in x:
                return 'won'
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == 0:
                    return ''
                try:
                    if self.data[i][j] == self.data[i][j+1]:
                        return ''
                except IndexError:
                    pass
                try:
                    if self.data[i][j] == self.data[i+1][j]:
                        return ''
                except IndexError:
                    pass
        return 'lost'

    def draw(self):
        rep = {0: '-'}
        rep.update(dict([(2**x, str(2**x)) for x in range(1, 12)]))
        return '\n'.join([''.join([rep[self.data[i][j]].rjust(5) for j in range(self.size)]) for i in range(self.size)])


def transpose(stat):
    return board(stat.size, [[x[i] for x in stat.data] for i in range(stat.size)])


def reverse(stat):
    return board(stat.size, [[x[-i] for i in range(1, stat.size+1)] for x in stat.data])


def move(stat):
    temp = stat.copy()

    def shift(row):
        for k in range(len(row)):
            if row[k] == 0:
                row.insert(0, row.pop(k))
        return row

    for i in range(stat.size):
        if sum(temp[i]) == 0:
            continue

        temp[i] = shift(temp[i])

        prev = False
        for k in range(stat.size - 1, 0, -1):
            if prev:
                prev = False
                continue
            if temp[i][k] == temp[i][k-1]:
                temp[i][k], temp[i][k-1] = 0, temp[i][k] * 2
                prev = True

        temp[i] = shift(temp[i])
    return board(stat.size, temp)


def check(stat, choice):
    if choice not in ['w', 'a', 's', 'd']:
        return False
    if choice in ['s', 'w']:
        temp = transpose(stat)
    else:
        temp = stat
    if choice in ['a', 'w']:
        temp2 = reverse(temp)
    else:
        temp2 = temp
    done = move(temp2)
    if choice in ['a', 'w']:
        temp2 = reverse(done)
    else:
        temp2 = done
    if choice in ['s', 'w']:
        temp = transpose(temp2)
    else:
        temp = temp2
    if temp.match(stat):
        return False
    else:
        return temp


size = 4
start = board(size)
start.place(count=2)
print('wasd to move. q to quit.')
while True:
    choice = input(start.draw())
    temp = check(start, choice)
    if not temp:
        continue
    print('-' * 20)
    temp.place()
    start = temp
    state = start.state()
    if state:
        print('You have', state, 'the match!')
        break
