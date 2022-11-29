
def readposint():
    try:
        
        pos_number = int(input('Pick a positive number: \n'))
        
        if pos_number < 0:
            raise ArithmeticError
        elif pos_number != int:
            raise ValueError
        elif pos_number == 0:
            print('neither a negative or a positive integer')
        else:
            print(f'{pos_number} is indeed a positive integer')

    except ArithmeticError as e:
        print('That is a negative number and is not a positive number')
    except ValueError as e:
        print('That is a string and not a positive number')
        print(e)
    except KeyboardInterrupt as e:
        print('Exited the input')

        


def main():
    readposint()

if __name__ == "__main__":
    main()