if 1:
    a = 10
print(a)
#print(num)


#体现作用域
def func():
    b = 20
    print("b =", b)

func()
#print(b)  #报错，因为b找不到
