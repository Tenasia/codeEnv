
from PIL import Image
def grocery():
    total = 0
    count = 0
    moreItems = True

    while moreItems:
        price = float(input('Enter the price of item (0 when done): '))
        if price < 0:
            print('not a valid price')
        elif price != 0:
            total += price
            count += 1
        else:
            moreItems = False
    if count == 0:
        return 'cannot compute without data'
    else:
        
        average = total/count


    print(f"your total shopping costs is: {total}")
    print(f"your total shopping item is: {count}")
    print(f"your total shopping average cost is: {average}")
        

def get_yes_or_no(message):
    valid_input = False
    answer = input(message)
    while not valid_input:
        answer = answer.upper()
        
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            answer = input(f'Please Enter Y for yes and N for no. {message}')
    
    return answer




def main():
    pixel_gen()
   

if __name__ == '__main__':
    main()
