def kaupk_aritmetika(*args, operacija="suma"):
    if len(args) < 2:
        return args
        return sum(args)
    elif operacija == "atimtis":
        return args[0] - sum(args[1:])


print(kaupk_aritmetika(1, 4, 5, operacija="suma"))
print(kaupk_aritmetika(10, 5, 2, operacija="atimtis"))
print(kaupk_aritmetika(10, 3, 2, operacija="dalyba"))
print(kaupk_aritmetika(10, 3, 2, operacija="daugyba"))