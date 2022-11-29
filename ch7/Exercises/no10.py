
def is_rightangled(a, b):

    x = a ** 2 + b ** 2
    y = findHypot(a, b) ** 2

    if abs(x - y) < 0.001:
        return True
    else: 
        return False

def is_righangled1(a, b, c):
    x = a ** 2 + b ** 2
    y = c ** 2

    if abs(x - y) < 0.001:
        return True
    else: 
        return False

def findHypot(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def main():
    
    print(is_rightangled(3, 4))
    print(is_righangled1(3, 4, 5))
    
    

if __name__ == '__main__':
    main()