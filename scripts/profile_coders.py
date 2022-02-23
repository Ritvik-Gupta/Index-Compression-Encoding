import sys

import pandas as pd
from algorithms.elias_delta import EliasDeltaCoder
from algorithms.elias_gamma import EliasGammaCoder
from algorithms.golomb import GolombCoder
from algorithms.index_compression import IndexCompressionImplementor
from algorithms.unary import UnaryCoder
from tabulate import tabulate


def main(args: list[str]):
    max_num_check = int(args[0])
    default_b_value = int(args[1])

    data = []
    coders: list[IndexCompressionImplementor] = [
        UnaryCoder(),
        EliasGammaCoder(),
        EliasDeltaCoder(),
        GolombCoder(b=default_b_value),
    ]
    for coder in coders:
        for n in range(1, max_num_check + 1):
            encoded = coder.encode(n)
            data.append(
                {
                    "Coder Name": str(coder),
                    "Number": n,
                    "Encoded Message": str(encoded),
                    "Message Size": len(encoded),
                }
            )

    df = pd.DataFrame(data)
    df.to_csv("docs/profile_coders.csv")

    del df["Encoded Message"]
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))


if __name__ == "__main__":
    main(sys.argv[1:])