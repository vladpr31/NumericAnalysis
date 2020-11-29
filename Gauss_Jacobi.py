def Jacobi(A, B):
    if abs(A[0][0]) < abs(A[0][1]) + abs(A[0][2]) or abs(A[1][1]) < abs(A[1][0]) + abs(A[1][2]) or abs(A[2][2]) < abs(
            A[2][1]) + abs(A[2][0]):
        print("There is no dominant diagonal")
    else:
        xr = lambda y, z: (B[0] - A[0][1] * y - A[0][2] * z) / A[0][0]
        yr = lambda x, z: (B[1] - A[1][0] * x - A[1][2] * z) / A[1][1]
        zr = lambda x, y: (B[2] - A[2][1] * y - A[2][0] * x) / A[2][2]
        e = 0.001
        x0 = 0
        y0 = 0
        z0 = 0
        count = 1
        condition = True
        print("Jacobi:")
        print("{:<8} {:<30} {:<30} {:<30}".format('count', 'Xr+1', 'Yr+1', 'Zr+1'))

        while condition:
            x1 = xr(y0, z0)
            y1 = yr(x0, z0)
            z1 = zr(x0, y0)
            print("{:<8} {:<30} {:<30} {:<30}".format(count, x1, y1, z1))
            stop = abs(x0 - x1)

            count += 1
            x0 = x1
            y0 = y1
            z0 = z1
            condition = stop > e


# ----------------------------------------------------------------------
def Gauss_Seidel(A, B):
    if abs(A[0][0]) < abs(A[0][1]) + abs(A[0][2]) or abs(A[1][1]) < abs(A[1][0]) + abs(A[1][2]) or abs(A[2][2]) < abs(
            A[2][1]) + abs(A[2][0]):
        print("There is no dominant diagonal")
    else:
        xr = lambda y, z: (B[0] - A[0][1] * y - A[0][2] * z) / A[0][0]
        yr = lambda x, z: (B[1] - A[1][0] * x - A[1][2] * z) / A[1][1]
        zr = lambda x, y: (B[2] - A[2][1] * y - A[2][0] * x) / A[2][2]
        e = 0.001
        x0 = 0
        y0 = 0
        z0 = 0
        xbase = 0
        count = 1
        condition = True
        print("\nGauss_Seidel:")
        print("{:<8} {:<30} {:<30} {:<30}".format('count', 'Xr+1', 'Yr+1', 'Zr+1'))

        while condition:
            x1 = xr(y0, z0)
            x0 = x1
            y1 = yr(x0, z0)
            y0 = y1
            z1 = zr(x0, y0)
            z0 = z1
            print("{:<8} {:<30} {:<30} {:<30}".format(count, x1, y1, z1))
            stop = abs(xbase - x1)
            xbase = x1

            count += 1
            condition = stop > e


#   x y z
A = [[4, 2, 0]
    , [2, 10, 4]
    , [0, 4, 5]]

# =
B = [2, 6, 5]
Jacobi(A, B)
Gauss_Seidel(A, B)
