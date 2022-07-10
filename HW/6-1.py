class Matrix(list):
    '''
    Matrix is a class for define a n*m Matrix by user.
    User define n and m of a matrix and Matrix class return
    a nested list as a user-defiend matrix.
    '''
    _matrix = []
    def __init__(self, n: int, m: int) -> None:
        self._n = n
        self._m = m
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
        for i in range(self._n):
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
    

mat1 = Matrix(3,4)
len(mat1)
print(type(mat1))
        