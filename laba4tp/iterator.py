from collections.abc import Iterator, Iterable

class CustomIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            value = self._collection[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

class CustomIterable(Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return CustomIterator(self._collection)

if __name__ == "__main__":
    items = ["item1", "item2", "item3"]
    iterable = CustomIterable(items)

    for item in iterable:
        print(item)
