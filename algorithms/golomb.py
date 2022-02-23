import math

from algorithms.index_compression import IndexCompressionImplementor
from utils.binary_format import BinaryFormat

from algorithms.unary import UnaryCoder


class GolombCoder(IndexCompressionImplementor):
    def __init__(self, b: int) -> None:
        self.b = b

    def __str__(self) -> str:
        return f"GolombCoder(b={self.b})"

    def encode(self, number: int) -> BinaryFormat:
        q = number // self.b
        r = number % self.b

        unary_code = UnaryCoder().encode(q + 1)

        i = math.floor(math.log2(self.b))
        d = 2 ** (i + 1) - self.b

        if r >= d:
            r += d
            i += 1

        binary_code = BinaryFormat.create_from(r)
        while len(binary_code) < i:
            binary_code.appendleft(False)

        return unary_code + binary_code

    def decode(self, encoded: BinaryFormat) -> int:
        code_idx = 0
        while code_idx < len(encoded) and encoded[code_idx] == False:
            code_idx += 1

        q = code_idx
        i = math.floor(math.log2(self.b))
        d = 2 ** (i + 1) - self.b

        r = 0
        bit_shifts = i - 1
        idx = 0
        while idx < i:
            r += int(encoded[idx + code_idx + 1]) << bit_shifts
            bit_shifts -= 1
            idx += 1

        if r >= d:
            r = (r << 1) + int(encoded[idx + code_idx + 1]) - d

        return q * self.b + r
