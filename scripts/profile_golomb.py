import sys

import pandas as pd
from algorithms.golomb import GolombCoder
from tabulate import tabulate


def main(args: list[str]):
    max_num_check = int(args[0])
    max_b_value = int(args[1])

    data = []
    for b in range(1, max_b_value + 1):
        coder = GolombCoder(b)
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
    df.to_csv("docs/profile_golomb.csv")

    del df["Encoded Message"]
    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main(sys.argv[1:])
