import sys
import requests
import logging
import pandas as pd
import numpy as np
from time import sleep

logging.basicConfig(filename="00_log.txt", level=logging.INFO, format="%(message)s")

""" Ignore the next two lines and keep them as they are. """
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"


def FeatureExtractionFromAddress(address):
    return {"key_one": 12, "key_two": "Dummy value", "fake_field": "fake_value"}


def main():

    df = pd.read_csv("../../MargedAddresses.csv")

    df.drop(df.columns[0], axis=1, inplace=True)

    print(df.columns)

    new_df = pd.DataFrame()

    """
    Index no. from which the features will start being extracted. Initially set to zero.
    But if program crashes for some reason, then put the index where the program crashed
    as the value of 'START_FROM' variable when you are going to run the program again. 
    """
    START_FROM = 0

    print("Loop starting...")

    for index, address in enumerate(df["Address"].to_list()):

        print(LINE_UP, end=LINE_CLEAR)
        print(f"At index: {index}")

        if index < START_FROM:
            continue

        try:
            features = FeatureExtractionFromAddress(address)

            row = {"address": address, **features}

            new_df = pd.concat([new_df, pd.DataFrame(row, index=[index])])

            new_df.to_csv("ethereum_scam_dataset.csv")

        except Exception as e:
            print(f"Error: {e.args}")
            sleep(2)
            print(LINE_UP, end=LINE_CLEAR)
            logging.info(f"At index: {index} \t Address: {address}")


if __name__ == "__main__":
    main()
