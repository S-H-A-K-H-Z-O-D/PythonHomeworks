def invest(amount, rate, years):
    a = 1
    P = amount

    while a <= years:
        P = P * (1 + rate/100)
        print(f"Year {a}: ${P:.2f}")
        a += 1

    print()


invest(100, 5, 4)