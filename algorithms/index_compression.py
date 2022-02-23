import abc

from utils.binary_format import BinaryFormat


class IndexCompressionImplementor(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "encode")
            and callable(subclass.encode)
            and hasattr(subclass, "decode")
            and callable(subclass.decode)
            or NotImplemented
        )

    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def encode(self, number: int) -> BinaryFormat:
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self, encoded: BinaryFormat) -> int:
        raise NotImplementedError
