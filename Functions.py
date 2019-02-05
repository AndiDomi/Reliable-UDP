import os
import math

buffer_size = 1024


def divide_counter_packet(data_and_counter):
    data = data_and_counter[:-1]
    counter = ord(data_and_counter[-1:])
    data_and_counter_array = [data, counter]
    return data_and_counter_array


def add_counter_packet(data, counter):
    counter = chr(counter).encode('ascii')
    data = data + counter
    return data


def add_data_in_order(array, data, counter):
    array.insert(counter, data)
    print(array)
    return array


def get_size_of_file(path_to_file):
    file_size = os.path.getsize(path_to_file)/buffer_size
    file_size = math.ceil(file_size)
    return file_size


def create_empty_array(size_of_file):
    file_array = [None] * size_of_file
    return file_array


def get_missing_counters(array_of_counters, counters_to_remove):
    for counter in counters_to_remove:
        print(counter)
        array_of_counters.remove(counter)
    return array_of_counters
