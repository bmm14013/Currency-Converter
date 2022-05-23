# Author: Brendan MacIntyre
# Description: This program contains a currency converter microservice
#               that operates using a txt file as a communcation pipeline
#
# *This program uses the CurrencyConverter package. Must install package before
#  running

from currency_converter import CurrencyConverter
import time


def convert_currency():
    c = CurrencyConverter()

    while True:
        f = open("curr_converter.txt", "r")
        contents = f.read()
        f.close()

        if "convert" in contents:
            f = open("curr_converter.txt", "w")
            contents = contents.split()
            currency = contents[1]
            if currency not in c.currencies:
                f.write("Currency is not supported")
            else:
                conv = c.convert(1, 'USD', currency)
                f.write(str(conv))
            f.close()
        
        if "help" in contents:
            f = open("curr_converter.txt", "w")
            available_currencies = c.currencies
            for curr in available_currencies:
                f.write(curr + "\n")
            f.close()

        time.sleep(5)

if __name__ == '__main__':
    convert_currency()


        



