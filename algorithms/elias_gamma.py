from utils.binary_format import BinaryFormat, zero

from algorithms.index_compression import IndexCompressionImplementor


class EliasGammaCoder(IndexCompressionImplementor):
    def __str__(self) -> str:
        return "EliasGammaCoder()"

    def encode(self, number: int) -> BinaryFormat:
        # Convert the number into a binary format
        bianry_code = BinaryFormat.create_from(number)
        # Having a length of B get the B-1 zeroes
        initial_zeroes = zero() * (len(bianry_code) - 1)
        return initial_zeroes + bianry_code  # adding zeroes at the front.

    def decode(self, encoded: BinaryFormat) -> int:
        # Compute the Initial Zeroes in the message as Z
        code_idx = 0
        while code_idx < len(encoded) and encoded[code_idx] == False:
            code_idx += 1

        # The next Z + 1 bits are for the number and we can perform bit shifts
        # Eg: (1001)bin = 1*8 + 0*4 + 0*2 + 1*1 = (9)dec
        # Or, (1001)bin = 1<<3 + 0<<2 + 0<<1 + 1<<0 = (9)dec
        bit_shifts = code_idx
        num = 0
        while code_idx < len(encoded):
            # Perform a bit shift for the given bit
            num += int(encoded[code_idx]) << bit_shifts
            bit_shifts -= 1
            code_idx += 1

        return num
