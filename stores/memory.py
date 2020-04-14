class MemStore:
    def __init__(self):
        self.__store = dict()

    def set(self, key, value):
        self.__store[key] = value

    def get(self, key):
        return self.__store.get(key)