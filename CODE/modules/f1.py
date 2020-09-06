import f2

print("f1:", __name__)
if __name__ == "__main__":
    f2.funct()
    f2.funct()
    print("Main script", __name__, type(__name__))
