N = int(input())
a = 1;
for i in range(1, N+1):
    for j in range(i):
        print(a, end=" ")
        a += 1
    print("")
