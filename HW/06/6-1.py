from operator import add, sub, mul, truediv, pow, lt, le, eq, ne, ge, gt

class Matrix:
    '''
    Matrix is a class for define a n*m Matrix by user.
    User define n and m of a matrix and Matrix class return
    a nested list as a user-defiend matrix.
    '''
 
    def __init__(self, n: int, m: int) -> None:
        self._n = n
        self._m = m
        self._matrix = []
        self.create() # call to create a null-matrix of n*m
        
    def __str__(self) -> str:
        '''
        Represent Matrix class as string.
        '''
        return f"A {self._n}*{self._m} Matrix created."
           
    def create(self) -> list:
        '''
        This function generates the n*m null-matrix.
        '''
        for _ in range(self._n):
            column = []
            for j in range(self._m):
                column.append(0)
            self._matrix.append(column)
        return self._matrix
    
    def __len__(self) -> int:
        '''
        This function return the multiple of row*column of matrix.
        But if you use len(my_matrix), it prints the dimention of my_matrix.
        '''
        print(f"{self._n}*{self._m}")
        return self._n*self._m
    
    def __abs__(self) -> list:
        '''
        A function that gets a matrix and returns it with positive elements.
        '''
        abs_matrix = self._matrix
        for i in range(self._n):
            for j in range(self._m):
                if j < 0:
                    abs_matrix[i] = abs_matrix[i][:j-1]+abs(j)+abs_matrix[i][j+1:]            
        return abs_matrix

    @staticmethod
    def euqal_dim(matrix1: object, matrix2: object):
        '''
        This function evaluate the matrices have the same dimensions or not.
        '''
        if isinstance(matrix1, Matrix) and isinstance(matrix2, Matrix):
            if (len(matrix1._matrix[1]) == len(matrix2._matrix[1])) and (len(matrix1._matrix) == len(matrix2._matrix)):
                return True
            return False
        return f"Inputs are not Matrix Object."
    
    def elements_operator(self, matrix, operator):
        '''
        This function loops on self & matrix element by element and apply an operator on them.
        '''
        if isinstance(matrix, Matrix):
            if Matrix.euqal_dim(self, matrix): # check the two matrices have identical dimension by staticmethod
                matrices = Matrix(self._n, self._m)
                for i in range(self._n):
                    for j in range(self._m):
                        matrices._matrix[i][j] = operator(self._matrix[i][j], matrix._matrix[i][j])
                return matrices._matrix
            return f"Matices have not the same dimentions"
        return f"{matrix} is not a matirx-object"
    
    def elements_comparison(self, matrix, operator):
        '''
        This function loops on self & matrix element by element and compares them.
        '''
        if isinstance(matrix, Matrix):
            if Matrix.euqal_dim(self, matrix): # check the two matrices have identical dimension by staticmethod
                matrices = Matrix(self._n, self._m)
                for i in range(self._n):
                    for j in range(self._m):
                        if operator(self._matrix[i][j], matrix._matrix[i][j]) is False:
                            return False
                return True
            return f"Matices have not the same dimentions"
        return f"{matrix} is not a matirx-object"
    
    def __add__(self, matrix: object):
        
        return self.elements_operator(matrix, add)
    
    def __sub__(self, matrix: object):

        return self.elements_operator(matrix, sub)
    
    def __mul__(self, matrix: object):

        return self.elements_operator(matrix, mul)
    
    def __truediv__(self, matrix: object):

        return self.elements_operator(matrix, truediv)
    
    def __pow__(self, matrix: object):

        return self.elements_operator(matrix, pow)
    
    def __lt__(self, matrix: object):

        return self.elements_comparison(matrix, lt)
    
    def __le__(self, matrix: object):
 
        return self.elements_comparison(matrix, le)
    
    def __eq__(self, matrix: object):
 
        return self.elements_comparison(matrix, eq)
    
    def __ne__(self, matrix: object):
 
        return self.elements_comparison(matrix, ne)
    
    def __ge__(self, matrix: object):
 
        return self.elements_comparison(matrix, ge)
    
    def __gt__(self, matrix: object):
 
        return self.elements_comparison(matrix, gt)
        

class Square(Matrix):
    '''
    Square is a class for define a n*n Matrix by user.
    User define n of a matrix and Square class return
    a nested list as a user-defiend matrix.
    '''
 
    def __init__(self, n: int) -> None:
        self._n = n
        self._m = n
        self._matrix = []
        self.create() # call to create a null-matrix of n*n
    
    def get_diagonal(self) -> list:
        '''
        A function that calcualtes main diagonal of matrix and returns it as list.
        '''
        matrice = []
        for i in range(self._n):
            matrice.append(self._matrix[i][i])
        return matrice
    
    def get_2nd_diagonal(self) -> list:
        '''
        A function that calcualtes secondary diagonal of matrix and returns it as list.
        '''
        matrice = []
        j = self._n
        for i in range(self._n):
                j -= 1
                matrice.append(self._matrix[i][j])
        return matrice
    
    def determinant(self) -> int:
        '''
        A function that calcualtes determinant of matrix and returns it as integer.
        '''
        adds = 0
        item = list(range(self._n))
        i = j = 0
        for _ in range(self._n):
                adds += self._matrix[item[i]][item[i]]
        return matrice


# mat1 = Matrix(3,4)
# mat2 = Matrix(3,4)
mat3 = Square(3)
# mat4 = Square(3)

# mat1._matrix[1][1] = 2
# mat2._matrix[1][1] = 4

mat3._matrix[1][1] = 2
mat3._matrix[0][2] = 4
# # mat4._matrix[1][1] = 2
# # print(mat3._matrix)
# # print(mat3._matrix[2][2])
# mat3.get_diagonal()
print(mat3.get_diagonal())
print(mat3.get_2nd_diagonal())


# print(mat3._matrix)
# print(mat4._matrix)

        