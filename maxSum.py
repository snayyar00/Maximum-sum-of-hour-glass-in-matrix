def hourglassSum(mat):
    sums=[]
    for i in range(len(mat)-2):
        for j in range(len(mat[0])-2):
            sums.append((mat[i][j]+mat[i][j+1]+mat[i][j+2])+ (mat[i+1][j+1])+(mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]))
    return max(sums)
    
    matrix = 5*[5*[0]]
    print(hourglassSum(matrix))
