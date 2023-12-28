a = [1, 2 , 3, 3 , 4, 4, 5 , 5, 6, 7, 8]
b = {}
for i in a:
    if b.get(i):
        b[i] = b[i] + 1
    else:
        b[i] = 1
x = []
y = []
for i in a:
    if b.get(i) > 1:
        x.append(i)
    else:
        y.append(i)
print(x)
a =  list(set(x))
print(y)

h = a[0]
for i in a:
    if(h>i):
        h = i
print(h)