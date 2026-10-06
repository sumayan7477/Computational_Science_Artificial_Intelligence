def multiply(matrix , scalar):
    new_matrix =[]
    for row in matrix:
        new_row=[]
        for i in row:
            j=i*scalar
            new_row.append(j)
        new_matrix.append(new_row)
    return new_matrix

def multiply(matrix , scalar):
    return [[x*scalar for x in row] for row in matrix]
