# Longest common subsequence
import numpy as np

def longestCommonSubsequence(a, b):
    m = len(a)
    n = len(b)
    # Write your code here
    c = [[0] * (m+1) for j in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,m+1):
            if i == 0 or j == 0:
                c[i][j] =  0
            elif b[i-1] == a[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

    length = c[n][m]

    indices_list = identify_the_index(c, length)

    lcs = plot_the_alphabet(a, indices_list)

    return length, lcs

def plot_the_alphabet(str_a, locate):
    str_list = ''
    for element in locate:
        x,y = element
        # y-1 as the grid matrix is +1 
        str_list += str_a[y-1]
    return str_list

def identify_the_index(c, length):
    locate = []
    c = np.array(c)
    for i in range(1,length+1):
        x, y = np.where(c == i)
        indices = [[i,j] for i, j in zip(x,y)]
        sum_indices = [i+j for i, j in zip(x,y)]
        index_min = np.where(sum_indices == np.min(sum_indices))[0][0]
        locate.append(indices[index_min])
    return locate



if __name__ == '__main__':
    a = 'loose'
    b = 'lush'
    length, string = longestCommonSubsequence(a,b)

    print(length)
    print(string)
