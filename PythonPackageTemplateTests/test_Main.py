
from unittest import TestCase

from PythonPackageTemplate.Main import Main


class TestMain(TestCase):

    def test_add(self):
        main = Main()
        result = main.add(2, 2)
        assert result == 4
        pass

    pass

    def test_sub(self):

        main = Main()
        result = main.sub(2, 2)
        assert result == 0
        pass

    pass
