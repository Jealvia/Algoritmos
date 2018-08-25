def count(S, m, n):
    if (n == 0):
        return 1
    if (n < 0):
        return 0;
    if (m <= 0 and n >= 1):
        return 0
    return count(S, m - 1, n) + count(S, m, n - S[m - 1]);


arr = [1, 2, 3]
m = len(arr)
#print("Coin change")
#print (arr)
#print(count(arr, m, 4))


def count(n):
    table = [0 for i in range(n + 1)]
    table[0] = 1
    for i in range(3, n + 1):
        table[i] += table[i - 3]
    for i in range(5, n + 1):
        table[i] += table[i - 5]
    for i in range(10, n + 1):
        table[i] += table[i - 10]
    return table[n]

#print("Count number of ways to reach a given score in a game")
n = 20
#print('Conteo para', n, 'es', count(n))
n = 13
#print('Conteo para', n, 'es', count(n))

N = 3
def maxPathSum(tri, m, n):
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):
            if (tri[i + 1][j] > tri[i + 1][j + 1]):
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]
    return tri[0][0]


print("Maximum path sum in a triangle")
tri = [[1, 0, 0],
       [4, 8, 0],
       [1, 5, 3]]
for arr in tri:
    print(arr)

print("Valor maximo: ",maxPathSum(tri, 2, 2))

