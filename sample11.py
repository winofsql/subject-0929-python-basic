# 引数無し、戻り値無しの関数
def display() :
    print('Hello')
    print('World')
    print('!!')

display()

# 引数有り、戻り値有りの関数
def area(radius) :
    result = radius * radius * 3.14
    return result

print(area(5))