from utils.binary_format import BinaryFormat, one, zero

from algorithms.index_compression import IndexCompressionImplementor


class UnaryCoder(IndexCompressionImplementor):
    def __str__(self) -> str:
        return f"UnaryCoder()"

    def encode(self, number: int) -> BinaryFormat:
        return zero() * (number - 1) + one()  # join (N-1) zeroes then a one

    def decode(self, encoded: BinaryFormat) -> int:
        return encoded.count(False) + 1  # counting the number of zeroes + 1
