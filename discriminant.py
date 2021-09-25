# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# this program asks the user for three coefficients and finds the discriminant


def main():
    # this function calcuates the discriminant and if there are any real solutions

    # input
    a = int(input("Enter the coefficient for a: "))
    b = int(input("Enter the coefficient for b: "))
    c = int(input("Enter the coefficient for c: "))
    print("")

    # process & output
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        print(
            "The discriminant equals {0}, thus there are TWO real solutions.".format(
                discriminant
            )
        )

    elif discriminant == 0:
        print(
            "The discriminant equals {0}, thus there is ONE real solution.".format(
                discriminant
            )
        )

    else:
        print(
            "The discriminant equals {0}, thus there are NO real solutions.".format(
                discriminant
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
