
import random


def randlist(upTo = 1000):

    randlist = []

    for _ in range(100):
        randomInt = random.randrange(upTo)

        randlist.append(randomInt)

    return randlist
def main():
    a = randlist()
    print(a)
if __name__ == '__main__':
    main()