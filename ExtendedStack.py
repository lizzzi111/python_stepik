class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+self.pop())

    def sub(self):
        self.append(self.pop()-self.pop())# операция вычитания

    def mul(self):
        self.append(self.pop()*self.pop())

    def div(self):
        self.append(self.pop()//self.pop())


x = ExtendedStack([1, 2, 3, 4])
x.sum()
