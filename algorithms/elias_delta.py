import math

from algorithms.index_compression import IndexCompressionImplementor
from utils.binary_format import BinaryFormat

from algorithms.elias_gamma import EliasGammaCoder


class EliasDeltaCoder(IndexCompressionImplementor):
    def __str__(self) -> str:
        return "EliasDeltaCoder()"

    def encode(self, number: int) -> BinaryFormat:
        gamma_code = EliasGammaCoder().encode(1 + math.floor(math.log2(number)))
        binary_code = BinaryFormat.create_from(number)
        binary_code.popleft()
        return gamma_code + binary_code

    def decode(self, encoded: BinaryFormat) -> int:
        code_idx = 0
        while code_idx < len(encoded) and encoded[code_idx] == False:
            code_idx += 1

        bit_shifts = code_idx
        num_bit_counter = 0
        for idx in range(code_idx, 2 * code_idx + 1):
            num_bit_counter += int(encoded[idx]) << bit_shifts
            bit_shifts -= 1

        num = 0
        bit_shifts = 0
        for idx in range(len(encoded) - 1, len(encoded) - num_bit_counter, -1):
            num += int(encoded[idx]) << bit_shifts
            bit_shifts += 1

        return num + (1 << bit_shifts)
