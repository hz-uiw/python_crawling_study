from function import add3, add2

if __name__ == "__main__":
    print("시작")
    print(__name__)
    print(add3(10, 20, 30))

    try:
        print("예외 처리")
        raise Exception("내가 만든 예외")
    except Exception as e:
        print("예외 발생")
        print(e)
