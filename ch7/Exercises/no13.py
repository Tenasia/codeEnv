def easter_date(year):

    if year < 1900 or year > 2099:
        return 'date out of range'

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    special_years = [1954, 1981, 2049, 2076]

    if year in special_years:
        date_of_easter = (22 + d + e) - 7
    else:
        date_of_easter = 22 + d + e

    return date_of_easter

def main():

    print(easter_date(3000))

if __name__ == '__main__':
    main()