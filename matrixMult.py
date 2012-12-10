    
def matrixMult(matrix1,matrix2):
    '''
    Multiplies two matrices together without numpy.
    Matrices are formatted as lists of lists.
    '''

    r1 = len(matrix1)
    c1 = len(matrix1[0])
    r2 = len(matrix2)
    c2 = len(matrix2[0])
    answerList = []

    for i in range(r1):
        for j in range(c2):
            s = 0
            for k in range(c1):
                s = s + matrix1[i][k] * matrix2[k][j]
                answerList.append(s)
    answerList = answerList[1::2]

    answerMatrix = []
    for i in range(max(r1,c1,r2,c2)):
        row = answerList[i*c1:(i+1)*c1]
        answerMatrix.append(row)

    if r1 != c2:
        raise ValueError('Incompatible matrix dimensions')
    else:
        return answerMatrix

