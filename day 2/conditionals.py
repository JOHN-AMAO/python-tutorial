def inspect(x):
    if x == 0:
        print("X is Zero")
    elif x == 1:
        print("X is one")
    elif x == 2:
        print("X is two")
    else:
        print("X is greater than 2")


def to_smash(total_candies):
    print("splitting", total_candies, "candy" if total_candies == 1 else "candies" )
    return total_candies % 3

to_smash(93)
to_smash(1)