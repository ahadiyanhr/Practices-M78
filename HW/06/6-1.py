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
    
    def __add__(self, matrix: object):
        '''
        This function adds two matrices.
        '''
        if isinstance(matrix, Matrix):
            if Matrix.euqal_dim(self, matrix):
                add_mat = Matrix(self._n, self._m)
                for i in range(self._n):
                    for j in range(self._m):
                        add_mat._matrix[i][j] = self._matrix[i][j]+matrix._matrix[i][j]
                return add_mat._matrix
            return f"Matices have not the same dimentions"
        return f"{matrix} is not a matirx-object"
        
    
mat1 = Matrix(3,4)
mat1._matrix[1][1] = 2
mat2 = Matrix(3,4)
mat2._matrix[1][1] = 4
print(mat1._matrix)
print(mat2._matrix)

print(mat1+mat2)
        