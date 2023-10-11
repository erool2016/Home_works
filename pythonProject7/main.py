class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.number = 0
        # self.stop = len(list_of_list)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count ==len(self.list_of_list):
            raise StopIteration
        if self.number < len(self.list_of_list[self.count]) - 1:
            item = self.list_of_list[self.count][self.number]
            self.number += 1
            return item
        elif self.number == len(self.list_of_list[self.count]) - 1:
            item = self.list_of_list[self.count][self.number]
            self.number = 0
            self.count += 1
            return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

import types


def flat_generator(list_of_lists):
    for items in list_of_lists:
        for item in items:
            yield item

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()