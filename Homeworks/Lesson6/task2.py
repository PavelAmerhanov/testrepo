class Road:
    def __init__(self, len1, width1):
        self._length = len1
        self._width = width1

    def weight_asphalt(self):
        print(F'Масса асфальта длиной {self._length} м. и шириной {self._width} м., '
              F'составит {int((self._length * self._width * 25 * 0.05) / 1000)} тонн.')


road1 = Road(20, 5000)
road1.weight_asphalt()
