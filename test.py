from Functions import *
import unittest

class TestSend(unittest.TestCase):

    # todo:
    def setUp(self):
        self.counter = 100
        self.data = bytes('andi', 'ascii')
        self.data_and_counter = 'andid'.encode('ascii')

    def test_add_counter_packet(self):
        self.assertEqual(add_counter_packet(self.data, self.counter), self.data_and_counter)


class TestReceive(unittest.TestCase):

    def setUp(self):
        self.counter = 100
        self.data = bytes('andi', 'ascii')
        self.data_and_counter = 'andid'.encode('ascii')
        self.filename = 'a.png'
        self.one_element_array= [b'andi0']

    def test_divide_counter_packet(self):
        data_and_counter_array = divide_counter_packet(self.data_and_counter)
        self.assertEqual(data_and_counter_array[0], self.data)

    def test_add_data_in_order(self):
        compare = [b'andi0',b'andi']
        self.assertSequenceEqual(add_data_in_order(self.one_element_array, self.data, 1), compare)

    def test_get_size_of_file(self):
        self.assertEqual(get_size_of_file(self.filename), 7)

    def test_create_empty_array(self):
        self.assertEqual(create_empty_array(1), [None])

    def test_get_missing_counters(self):
        array_of_counters=[0,2,3]
        self.assertEqual(get_missing_counters(array_of_counters, [2]), [0,3])
        self.assertEqual(get_missing_counters(array_of_counters, [0]), [3])

if __name__ == '__main__':
    unittest.main()
