# с этим заданием возникла сложность
numb = int(input("Введите целое положительное число "))
x = numb % 10
while numb > 0:
    if numb % 10 > x:
       x = numb % 10
    numb = numb // 10
print(x)

