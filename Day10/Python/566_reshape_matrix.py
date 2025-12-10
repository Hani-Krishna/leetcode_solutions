class Solution(object):
    def matrixReshape(self, mat, r, c):
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat
    
        flat = []
        for row in mat:
            flat.extend(row)
    
        new_mat = []
        index = 0

        for _ in range(r):
            new_mat.append(flat[index:index+c])
            index += c
        
        return new_mat
