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
        This method generates the n*m null-matrix.
        '''
        for _ in range(self._n):
            column = []
            for j in range(self._m):
                column.append(0)
            self._matrix.append(column)
        return self._matrix
    
    def assign_matrix(self, matrix: list):
        '''
        This method get a matrix as a list and assign it to instance.
        '''
        if Matrix.euqal_dim(self, matrix):
            self._matrix = matrix
            return self._matrix
        return f"Matices have not the same dimentions"
    
    def __len__(self) -> int:
        '''
        This method return the multiple of row*column of matrix.
        But if you use len(my_matrix), it prints the dimention of my_matrix.
        '''
        print(f"{self._n}*{self._m}")
        return self._n*self._m
    
    def __abs__(self) -> list:
        '''
        A method that gets a matrix and returns it with positive elements.
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
        This method evaluate the matrices have the same dimensions or not.
        '''
        if isinstance(matrix1, Matrix) and isinstance(matrix2, Matrix):
            if (len(matrix1._matrix[1]) == len(matrix2._matrix[1])) and (len(matrix1._matrix) == len(matrix2._matrix)):
                return True
            return False
        return f"Inputs are not Matrix Object."
    
    def elements_operator(self, matrix, operator):
        '''
        This method loops on self & matrix element by element and apply an operator on them.
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
        This method loops on self & matrix element by element and compares them.
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
        A method that calcualtes main diagonal of matrix and returns it as list.
        '''
        matrice = []
        for i in range(self._n):
            matrice.append(self._matrix[i][i])
        return matrice
    
    def get_2nd_diagonal(self) -> list:
        '''
        A method that calcualtes secondary diagonal of matrix and returns it as list.
        '''
        matrice = []
        j = self._n
        for i in range(self._n):
                j -= 1
                matrice.append(self._matrix[i][j])
        return matrice
    
    def __push_elements(self) -> list:
        '''
        This private method push first column in Square matrix to the end.
        '''
        push_matrix = self._matrix
        for row in range(self._n):
            pops = self._matrix[row].pop(0)
            push_matrix[row].extend([pops])
        return push_matrix
    
    @staticmethod
    def __multiple_rows(lists: list) -> int:
        '''
        This private method return the summation of multiples of a list's items.
        '''
        mult = 1
        for items in lists:
            mult = mult*items
        return mult
        
    
    
    def determinant(self) -> int:
        '''
        A method that calcualtes determinant of matrix and returns it as integer.
        '''
        determinants = 0
        matrice = self
        for _ in range(self._n):
            # main diagonal - secondary diagonal:
            determinants += Square._Square__multiple_rows(matrice.get_diagonal())-Square._Square__multiple_rows(matrice.get_2nd_diagonal())
            matrice.__push_elements() # for push the first column of matrix to the end column
        return determinants



mat3 = Square(3)
list1 = [[2, -3, 1], [2, 0, -1], [1, 4, 5]]
mat3.assign_matrix(list1)
print(mat3._matrix)

print(mat3.determinant())


# print(mat3._matrix)
# print(mat4._matrix)

        