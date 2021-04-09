import taskE

class Robot:

    def __init__(self, x = (0,0)):
        if 0 <= x[0] <= 100:
            self.x = x[0]
        elif x[0] > 100:
            self.x = 100
        elif x[0] < 0:
            self.x = 0
        if 0 <= x[1] <= 100:
            self.y = x[1]
        elif x[1] > 100:
            self.y = 100
        elif x[1] < 0:
            self.y = 0
        self.list = []
        self.list.append((self.x, self.y))

    def move(self, command):
        for i in command:
            if i == "N":
                self.moveN()
            elif i == "S":
                self.moveS()
            elif i == "E":
                self.moveE()
            elif i == "W":
                self.moveW()
            else:
                print("Ошибка")
        return (self.x, self.y)

    def path(self):
        return self.list

    def moveN(self):
        if self.y + 1 <= 100:
            self.y += 1
            self.list.append((self.x, self.y))

    def moveS(self):
        if self.y - 1 >= 0:
            self.y -= 1
            self.list.append((self.x, self.y))

    def moveE(self):
        if self.x + 1 <= 100:
            self.x += 1
            self.list.append((self.x, self.y))

    def moveW(self):
        if self.x - 1 >= 0:
            self.x -= 1
            self.list.append((self.x, self.y))

if __name__ == '__main__':
    r = Robot((200,200))
    print(r.move('SS'))
    print(*r.path())



