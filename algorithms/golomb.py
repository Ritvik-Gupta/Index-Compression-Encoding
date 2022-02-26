import math

from utils.binary_format import BinaryFormat

from algorithms.index_compression import IndexCompressionImplementor
from algorithms.unary import UnaryCoder


class GolombCoder(IndexCompressionImplementor):
    def __init__(self, golomb_rice_param: int) -> None:
        # The `b` parameter is a shorthand for the "Golomb-Rice parameter"
        self.golomb_rice_param = golomb_rice_param

    def __str__(self) -> str:
        return f"GolombCoder(b={self.golomb_rice_param})"

    def encode(self, number: int) -> BinaryFormat:
        q = number // self.golomb_rice_param  # Quotient
        r = number % self.golomb_rice_param  # Remainder

        # Golomd Encoder is split into 2 phases one being performing a Unary Encoding
        unary_code = UnaryCoder().encode(q + 1)

        # i = |_ log2(b) _| or Nearest power of 2 smaller than or equal to `b`
        i = math.floor(math.log2(self.golomb_rice_param))
        # j is then the next power of 2 greater than `b` and
        # d = j - b
        d = 2 ** (i + 1) - self.golomb_rice_param
        # Where, 2^i <= b < 2*j

        # As a combined Step 1 and 2
        # If r >= 2^(i+1)-b
        if r >= d:
            r += d  # r += 2^(i+1)-b
            i += 1  # Increment i to next place in power of 2

        binary_code = BinaryFormat.create_from(r)
        while len(binary_code) < i:  # For the binary format of `r`
            binary_code.appendleft(False)  # prefix with additional zeroes if required

        return unary_code + binary_code

    def decode(self, encoded: BinaryFormat) -> int:
        # Compute the Initial Zeroes in the message as Z
        code_idx = 0
        while code_idx < len(encoded) and encoded[code_idx] == False:
            code_idx += 1

        q = code_idx  # q would be the number of initial zeroes
        i = math.floor(math.log2(self.golomb_rice_param))  # i =|_ log2(b) _|
        d = 2 ** (i + 1) - self.golomb_rice_param  # Same formulae for d

        r = 0  # To compute r from the next `i` bits
        bit_shifts = i - 1
        idx = 0
        while idx < i:
            # Start after the initial zeroes
            r += int(encoded[idx + code_idx + 1]) << bit_shifts
            bit_shifts -= 1
            idx += 1

        if r >= d:  # Testing for Case 2 during encoding
            r = (r << 1) + int(encoded[idx + code_idx + 1]) - d

        return q * self.golomb_rice_param + r
