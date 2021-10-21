
def differentiate(r):

    def inner(dict):
        point = dict.get("point")
        seed = dict.get("seed")
        return r * point**(r-1) * seed

    return inner


if __name__ == "__main__":
    # Run this to test your code locally.
    r = 4
    x = 3
    seed = 1
    dict = {"point":x, "seed":seed}
    pow = differentiate(r)
    print(pow(dict))
