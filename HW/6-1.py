class Matrix:
    '''
    Matrix is a class for define a n*m Matrix by user.
    '''
    
    def __init__(self, n: int, m: int) -> None:
        self._n = n
        self._m = m
        self.create()
        
    def create(self) -> list:
        '''
        This function generates the n*m null-matrix.
        '''
        row = []
        for i in range(self._n):
            column = []
            for j in range(self._m):
                column.append(0)
            row.append(column)
        return row
        