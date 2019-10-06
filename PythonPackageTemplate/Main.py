from PythonPackageTemplate.Module.Module import Module


class Main(object):

    def __init__(self):
        print("hallo")
        pass

    def add(self, x: int, y: int) -> int:
        return x + y
        pass

    def sub(self, x: int, y: int) -> int:
        module = Module()
        return module.sub(x, y)
        pass


if __name__ == "__main__":
    main = Main()
    print(main.add(2, 3))
