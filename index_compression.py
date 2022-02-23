import abc

from utils import BinaryFormat


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
    def encode(self, number: int) -> BinaryFormat:
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self, encoded: BinaryFormat) -> int:
        """Extract text from the data set"""
        raise NotImplementedError
