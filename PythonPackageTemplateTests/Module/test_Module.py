
from unittest import TestCase

from PythonPackageTemplate.Module.Module import Module


class TestModule(TestCase):

    def test_sub(self):
        module = Module()
        result = module.sub(2, 2)
        assert result == 0
        pass

    pass
