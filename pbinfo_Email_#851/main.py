f = open("email.in")
s = f.read()
f.close()

s = s[:len(s)-1]
d = {x.split('@')[1] : 0 for x in s.split('\n')}

for email in s.split('\n'):
    d[email.split('@')[1]] += 1

list = [(x, y) for (x, y) in d.items()]

list = sorted(list, key=lambda x: (-x[1], x[0]))

f = open("email.out", "w")

f.write(str(len(list)) + '\n')
for i in list:
    f.write(i[0] + " " + str(i[1]) + '\n')