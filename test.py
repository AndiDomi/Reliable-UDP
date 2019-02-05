from Send import add_counter_packet
from Receive import divide_counter_packet
import unittest

class TestSend(unittest.TestCase):

    def setUp(cls):
        cls.counter=100


    def test_add_counter_packet(self):
        self.assertEqual(add_counter_packet(bytes('andi', 'ascii'), self.counter), 'andid'.encode('ascii'))

class TestReceive(unittest.TestCase):
    def test_divide_counter_packet(self):
        print('failed')


if __name__ == '__main__':
    unittest.main()