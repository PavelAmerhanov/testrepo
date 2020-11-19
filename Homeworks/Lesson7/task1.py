class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):  # оч хочется напечатать ровно но простого кода не смог
        my_str = ''
        for i in self.my_list:
            my_str = my_str + str(i) + '\n'
        return my_str

    def __add__(self, other):
        # len(self.my_list) - количество строк
        # len(self.my_list[0]) - количество стобцов
        if len(self.my_list) == len(other.my_list) and len(self.my_list[0]) == len(other.my_list[0]):
            my_list = [[self.my_list[i][j] + other.my_list[i][j] for j in range(len(self.my_list[0]))] for i in
                       range(len(self.my_list))]
            return Matrix(my_list)  # можно было бы не вводить переменную но тогда строка уж больно большая
        else:
            return 'Матрицы не равны'


m = Matrix([[11, 2, 3], [22, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 22, 33], [5, 55, 66], [7, 8, 9]])
m3 = Matrix([[1, 22], [5, 66], [8, 9]])

print(m)
print(m2)
sum_m1 = m + m2
print(sum_m1)
sum_m2 = m + m3
print(sum_m2)
