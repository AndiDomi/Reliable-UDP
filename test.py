import Send
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        data = bytes('andi', 'ascii')
        counter=100
        assert_true='andid'.encode('ascii')
        self.assertEqual(Send.add_counter_packet(data, counter),assert_true )



if __name__ == '__main__':
    unittest.main()