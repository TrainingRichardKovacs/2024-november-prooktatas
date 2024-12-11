
def my_func():
    print("hello")

print(__file__)

print(__name__)

if __name__ == '__main__':
    print("most közvetlenül hívtak meg")
else:
    print("most importáltak")