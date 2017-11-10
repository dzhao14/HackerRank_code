#https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/cost-balancing

if __name__ == "__main__":
    n, m = [int(_) for _ in input().strip().split()]
    people = [0] * m

    for i in range(n):
        ID, amt = [int(_) for _ in input().strip().split()]
        people[ID-1] += amt

    tot = sum(people)
    topay = tot // m
    
    if topay * m != tot:
        #do something useful
        diff = tot - (topay * m)
        print("1 {}".format(people[0] - (topay + diff)))
    else:
        print("1 {}".format(people[0] - topay))

    for i in range(1,m):
        diff = people[i] - topay
        print("{} {}".format(i+1, diff))
