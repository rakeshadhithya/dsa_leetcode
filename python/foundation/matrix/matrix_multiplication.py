A = eval(input('Enter matrix A:  '))
B = eval(input('Enter matrix B:  '))
rows_A, cols_A = len(A), len(A[0])
rows_B, cols_B = len(B), len(B[0])

if cols_A != rows_B:
    raise ValueError('no. of cols in A must be equal to no. of rows in B')

C = [ [0 for _ in range(cols_B)] for _ in range(rows_A)]

for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            C[i][j] += A[i][k] * B[k][j]
for l in C:
    print(l)

#TC: O(M*P*N) : creation of C takes O(m) * O(p) i.e. O(m*p) + i iterates throgh each row of A O(m) * j iterates through 
# each col of B O(p) * k iterates through each col of A O(n)
#SC: A stores matrix 1 O(mxn), B stores matrix 2 O(nxp), C stores resultant matrix O(mxp)
    # total: O(mxn + nxp + mxp )
    # dominant: O(max(mxn, nxp, mxp ))
    # auxilary:(without inputs): O(mxp)
'''
matrix multiplication:
A = m x n
B = n x p
*1. C = m x p
*2. for each row for each col in C, sum of each (col of A + row of B)
A = [[1, 2], [3,4]]
B = [[5, 6], [7, 8]]
output:
[19, 22]
[43, 50]
'''