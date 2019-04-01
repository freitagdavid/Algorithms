#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # min_price = prices[0]
    # max_profit = prices[1] - prices[0]
    # print('max profit', max_profit)

    for index, value in enumerate(prices):
        if index == 0:
            min_price = prices[0]
            max_profit = prices[1] - prices[0]
        else:
            if value < min_price:
                min_price = value
            else:
                working = value - min_price
                if working > max_profit:
                    max_profit = working

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

# DONE create variable for lowest price and maximum profit
# DONE iterate through list of prices
# DONE check if current price is lower than lowest price
# DONE if it is reassign lowest price
    # DONE move to next item
# DONE else subtract lowest price from current price
# DONE if it's higher than current max profit reassign max profit
# DONE else move to next item
