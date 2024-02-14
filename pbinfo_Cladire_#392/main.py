f = open("cladire.in", "r")
s = f.read()
f.close()

s = s.split()

n = int(s[0])
m = int(s[1])

a = [[1 for _ in range(0, m)] for _ in range(0, n)]

for i in range(1, n):
    for j in range(1, m):
        a[i][j] = (a[i-1][j] + a[i][j-1]) % 9901

f = open("cladire.out", "w")
f.write(str(a[n-1][m-1]))
f.close()