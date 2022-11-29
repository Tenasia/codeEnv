

def main():

    cols = range(1, 13)
    rows = range(1, 13)
    

    Column = ''
    Row = ''
    for col in cols:
        Column += f'\t {col}'
        
    for row in rows:
        Row += f'\n {row}'
        for multp in range(1, 13):
            Row += f'\t {row * multp}'

            
    print(Column)
    print(Row)

if __name__ == '__main__':
    main()