def notesneed(num): 

    arr = [500, 100, 50, 20, 10, 5, 2, 1]

    for i in range(len(arr)):
        rem = num%arr[i]
        note = (num - rem) / arr[i]
        num = rem
        if note == 0 :
         continue
        if arr[i] <= 5:
               
         print(note,"COIN OF",arr[i],)
        else:
         print(note,"Note OF",arr[i],)
notesneed(988)