if __name__ == '__main__':
    n=int(input())
    a=list()
    for _ in range(n):
        name = input()
        score = float(input())
        a.append([score,name])
    a.sort()
    marks=list()
    for i in range(0,n):
        if a[0][0] == a[i][0]:
            marks.append(a[i][0])
    
    
    for i in range(0,len(marks)):
        if marks[i]==a[i][0]:
            a.remove(a[i])
            
    for i in range(0,len(a)):
        if a[0][0]==a[i][0]:
            print(a[i][1])
        