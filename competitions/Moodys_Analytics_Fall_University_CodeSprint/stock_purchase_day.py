#https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/stock-purchase-day

def bruteforce(q, prices, days):
    min_price = min(prices)
    for _ in range(q):
        top = int(input())
        if top < min_price:
            print("-1")
            continue
        for i in range(days-1, -1, -1):
            if prices[i] <= top:
                print(i+1)
                break



if __name__ == "__main__":
    days = int(input())
    prices = [int(_) for _ in input().strip().split()]
    q = int(input())
    bruteforce(q, prices, days)
