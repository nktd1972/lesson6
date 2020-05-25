stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = {a: prices[a] * (1 - stock[a] / 100) for a in prices.keys()}
print(total_price)
