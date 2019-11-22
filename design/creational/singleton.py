"""
This pattern is a type of "creational" pattern and involves the presence of one class and restricting object creation
to a single object with a single global point of access to this instance.
"""
import unittest
import uuid


def singleton(cls):
    """
    Simple usage:

    @singleton
    class MyClass(BaseClass):
        pass

    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


class Singleton:
    """
    Simple usage:

    class MyClass(Singleton, BaseClass):
        pass

    """
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class SingletonMeta(type):
    """
    Simple usage:

    class MyClass(BaseClass, metaclass=SingletonMeta):
        pass

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestSingleton(unittest.TestCase):

    def test_singleton_with_decorator(self):
        class IdAssigner:
            def __init__(self):
                self.id = uuid.uuid4()

        class NormalClass(IdAssigner):
            pass

        @singleton
        class SingletonClass(IdAssigner):
            pass

        c1 = NormalClass()
        c2 = SingletonClass()
        c3 = SingletonClass()
        self.assertNotEqual(c1.id, c2.id)
        self.assertNotEqual(c1.id, c3.id)
        self.assertEqual(c2.id, c3.id)

    def test_singleton_with_class(self):
        class IdAssigner:
            def __init__(self):
                self.id = uuid.uuid4()

        class NormalClass(IdAssigner):
            pass

        class SingletonClass(Singleton, IdAssigner):
            pass

        c1 = NormalClass()
        c2 = SingletonClass()
        c3 = SingletonClass()
        self.assertNotEqual(c1.id, c2.id)
        self.assertNotEqual(c1.id, c3.id)
        self.assertEqual(c2.id, c3.id)

    def test_singleton_with_metaclass(self):
        class IdAssigner:
            def __init__(self):
                self.id = uuid.uuid4()

        class NormalClass(IdAssigner):
            pass

        class SingletonClass(IdAssigner, metaclass=SingletonMeta):
            pass

        c1 = NormalClass()
        c2 = SingletonClass()
        c3 = SingletonClass()
        self.assertNotEqual(c1.id, c2.id)
        self.assertNotEqual(c1.id, c3.id)
        self.assertEqual(c2.id, c3.id)


if __name__ == '__main__':
    unittest.main()
