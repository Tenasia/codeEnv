

def translator():

    with open('D:\Downloads\codeEnv\ch12\Exercises\pirate_words.txt', 'r') as words:

        
        
        every_pair = []

        for row in words:
            
            list_pair = row.rstrip('\n').split()
            
            if len(list_pair) > 2:
                pair = [list_pair[0]] + [list_pair[1] + ' ' + list_pair[2]]
            else:
                pair = [list_pair[0]] + [list_pair[1]]

            every_pair.append(pair)

        dict_pair = {} 
        
        for pair in every_pair:
            dict_pair[pair[0]] = pair[1] 

        input_word = input('Translate your sentences into Pirate: ').lower()
        input_list = input_word.split()
        

        final_string = ''
        
        for word in input_list:
            if word in dict_pair.keys():
                final_string += dict_pair[word] + ' '
            else:
                final_string += word + ' '

        print(final_string)

def main():
    translator()


if __name__ == '__main__':
    main()