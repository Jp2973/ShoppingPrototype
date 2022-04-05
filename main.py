from .curses import cursesTest
from .basic import basicTest

def main():
    while 1:
        choice = input("For a basic test of functionality input B, to try Curses input C, to exit input X").lower()
        if (choice == "b"):
            basicTest()
        elif (choice == "c"):
            cursesTest()
        elif (choice == "x"):
            return


if __name__ == "__main__":
    main()