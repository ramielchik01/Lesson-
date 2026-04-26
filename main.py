class Universities:
    def __init__(self, fillial):
        self.fillial = fillial

    def nameOfFillials(self):
        return f'there are names: {self.fillial}'

univer1 = Universities("MGU")
print(univer1.nameOfFillials())
