def add(num1, num2):
    return num1 + num2, num1, num2

def add(num1:str="0", num2 = 0, num3 = 0):
    return num1, num2, num3

def add2(*a):   #튜플로 값 나옴
    print(a)
    result = 0
    for n in a:
        result += n
    return result

def add3(*b):
    print(__name__)
    return sum(b)

if __name__ == "__main__":
    print(add([10]))

    n1, n2, n3 = add(10, 20)        # 자바스크립트에서의 비구조 할당과 같은 역할
    print(add2(1, 2, 3, 4, 5))
    print(add3(1, 2, 3, 4, 5))