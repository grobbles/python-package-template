
class Module(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def sub(self, x: int, y: int) -> int:
        return x - y
        pass
