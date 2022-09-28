#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    import calculator_1 as me

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, me.add(a, b)))
    print("{} - {} = {}".format(a, b, me.sub(a, b)))
    print("{} * {} = {}".format(a, b, me.mul(a, b)))
    print("{} / {} = {}".format(a, b, me.div(a, b)))
