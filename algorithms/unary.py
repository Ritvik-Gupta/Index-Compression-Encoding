from index_compression import IndexCompressionImplementor
from utils import BinaryFormat, one, zero


class UnaryCoder(IndexCompressionImplementor):
    def encode(self, number: int) -> BinaryFormat:
        return zero() * (number - 1) + one()

    def decode(self, encoded: BinaryFormat) -> int:
        return encoded.count(False) + 1
