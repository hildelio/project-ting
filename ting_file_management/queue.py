from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.data.append(value)
        self.__length += 1

    def dequeue(self):
        if self.__length > 0:
            self.__length -= 1
            return self.data.pop(0)

    def search(self, index):
        if 0 <= index < self.__length:
            return self.data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
