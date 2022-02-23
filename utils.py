from typing import Deque


class BinaryFormat(Deque[bool]):
    @staticmethod
    def create_from(number: int):
        code = BinaryFormat()
        while number > 0:
            code.appendleft(bool(number % 2))
            number //= 2
        return code

    def as_binary_str(self) -> str:
        binary = ""
        for bit in self:
            binary += str(int(bit))
        return binary


def zero() -> BinaryFormat:
    return BinaryFormat([False])


def one() -> BinaryFormat:
    return BinaryFormat([True])
