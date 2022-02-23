from index_compression import IndexCompressionImplementor
from utils import BinaryFormat, zero


class EliasGammaCoder(IndexCompressionImplementor):
    def encode(self, number: int) -> BinaryFormat:
        bianry_code = BinaryFormat.create_from(number)
        initial_zeroes = zero() * (len(bianry_code) - 1)
        return initial_zeroes + bianry_code

    def decode(self, encoded: BinaryFormat) -> int:
        code_idx = 0
        while code_idx < len(encoded) and encoded[code_idx] == False:
            code_idx += 1

        bit_shifts = code_idx
        num = 0
        while code_idx < len(encoded):
            num += int(encoded[code_idx]) << bit_shifts
            bit_shifts -= 1
            code_idx += 1

        return num
