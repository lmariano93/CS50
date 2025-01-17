class Jar:
    def __init__(self, capacity=12):
        if type(capacity) != int or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if type(n) != int or n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies! Exceeds the jar's capacity.")
        self._size += n

    def withdraw(self, n):
        if type(n) != int or n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer")
        if self._size < n:
            raise ValueError("Not enough cookies to withdraw.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
