class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list
        self.rows = len(matrix_list)
        self.columns = len(matrix_list[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("There is an error! Matrices must have the same dimensions for addition.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[self.matrix[i][j] * other for j in range(self.columns)] for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError("The 1st row's length of the 1st matrix is not equal to the length of the 2nd's column")
            result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)]
            return Matrix(result)
        else:
            raise TypeError("Unsupported type for multiplication.")

    def __matmul__(self, other):
        return self.__mul__(other)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(result)



m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
scalar = 2

result_add = m1 + m2
result_scalar_mul = m1 * scalar
result_matrix_mul = m1 * m2
result_matrix_matmul = m1 @ m2
result_transpose = m1.transpose()

print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)
print("\nMatrix Addition:")
print(result_add)
print("\nScalar Multiplication:")
print(result_scalar_mul)
print("\nMatrix Multiplication:")
print(result_matrix_mul)
print("\nMatrix Matmul:")
print(result_matrix_matmul)
print("\nTranspose of Matrix 1:")
print(result_transpose)
