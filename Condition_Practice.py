n = 13894560
count_100 = 0
count_50 = 0
count_20 = 0
count_1 = 0
while(n!=0):
    count_100 = n//100
    n = n - (100*count_100)
    if (n>50):
        count_50 = n//50
        n = n-(50*count_50)
    if (n>20):
        count_20 = n//20
        n = n-(20*count_20)
    count_1 = n
    break


print("100: ", count_100, "50 :", count_50, "20: ", count_20, "1", count_1)