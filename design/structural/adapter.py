"""
This pattern is a type of "structural" pattern and adapts the interface of a legacy system to be shaped as requested by
one of its clients. The purpose of the Adapter is to convert the interface of a legacy class in order to let two
incompatible interfaces work together.
"""
import unittest


class Target:
    """
    The Target class is the interface used by the client.
    """
    behavior = "This is the target behavior (but not the desired)."

    def request(self) -> str:
        return self.behavior


class Adaptee:
    """
    The "Adaptee" is a legacy class that has some useful methods, but its interface is incompatible with the existing
    client, that can't use it.
    """
    behavior = ("This", "is", "the", "desired", "behavior.")

    def specific_request(self) -> tuple:
        return self.behavior


class Adapter(Target):
    """
    The Adapter makes the legacy interface compatible with the target interface used by the client.
    """
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return " ".join(self.adaptee.specific_request())


class TestAdapter(unittest.TestCase):

    def test_client(self):

        class Client:
            def __init__(self):
                self.target = Target()
                adaptee_instance = Adaptee()
                self.adapter = Adapter(adaptee_instance)
                self.desired_behavior = "This is the desired behavior."

        client = Client()
        adaptee = Adaptee()
        self.assertNotEqual(client.target.request(), client.desired_behavior)
        self.assertNotEqual(adaptee.specific_request(), client.desired_behavior)
        self.assertEqual(client.adapter.request(), client.desired_behavior)


if __name__ == "__main__":
    unittest.main()
