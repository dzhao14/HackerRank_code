#https://www.hackerrank.com/contests/world-codesprint-9/challenges/grading

def round_(glist):
    out = []
    for raw_g in glist:
        mod5 = raw_g % 5
        if raw_g < 38:
            out.append(raw_g)
        elif mod5 == 0:
            out.append(raw_g)
        elif mod5 > 2:
            out.append(raw_g + 5 - mod5)
        else:
            out.append(raw_g)
    return out

if __name__ == '__main__':
    n = int(input())
    raw_grade = []
    for i in range(0,n):
        grade = int(input())
        raw_grade.append(grade)

    rounded_grade = round_(raw_grade)

    for i in range(0, n):
        print(rounded_grade[i])
    

    
