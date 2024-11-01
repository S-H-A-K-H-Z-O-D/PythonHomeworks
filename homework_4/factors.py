def isFactor(X: int):
    a = 1

    while a <= X:
        if X % a == 0:
            print(f"{a} is a factor of {X}")

        a += 1

    print()

isFactor(200)