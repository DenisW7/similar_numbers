#вывести количество чисел, которые совпадают
a = int(input())
b = int(input())
c = int(input())
lst = [a, b, c]
similar = 0
for i in lst:
    for t in lst:
        if i == t:
            similar +=1
        else:
            continue
print(similar)