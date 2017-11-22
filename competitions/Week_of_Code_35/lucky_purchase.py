#https://www.hackerrank.com/contests/w35/challenges/lucky-purchase

def validPrice(price):
    sevens = 0
    fours = 0
    for c in price:
        if c == "7":
            sevens += 1
        elif c == "4":
            fours += 1
        else:
            return False
    return sevens == fours
            

if __name__ == "__main__":
    min_price = -1
    best_name = -1
    n = int(input())
    for i in range(n):
        line = input().strip().split()
        name = line[0]
        price = int(line[1])
        valid = validPrice(str(price))
        if valid:
            if min_price == -1:
                min_price = price
                best_name = name
            else:
                if price < min_price:
                    min_price = price
                    best_name = name
    print (best_name)
        
            
