class DynamicArray:
    # must give default size to array
    def __init__(self, capacity=8):
        # keep tracking of how much we're using
        self.count = 0
        self.capacity = capacity
        # make 8 empty buckets to put items in
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        # check for free space
        if self.count == self.capacity:
            # TODO: increase size
            print("ERROR: Array is full!")
            return

        if index >= self.count:
            # TODO: better error handling
            print("ERROR: Index out of bounds")
            return

        # going to end of array, moving everything to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count == self.capacity:
            # TODO: increase size
            print("ERROR: Array is full!")
            return

        # self.count += 1
        # self.insert(self.count - 1) = value

        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        # changing the pointer
        self.storage = new_storage
