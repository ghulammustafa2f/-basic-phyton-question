def notesneed(num=int): 
 
    arr = [500, 100, 50, 20, 10, 5, 2, 1]

    for i in range(len(arr)):
        rem = num%arr[i]
        note = (num - rem) / arr[i]
        num = rem
        print(arr[i] , note)


    # if  num>=500: 
    #     rem = num%500
    #     note = (num - rem) / 500
    #     num = rem
    #     print("500 = " , note)

    # if num>=100:
    #     rem = num%100
    #     note = (num - rem) / 100
    #     num = num - note*100
    #     print("100 = ",note) 
        
    # if  num>=50:
    #     rem = num%50
    #     note = (num - rem) / 50
    #     num = num - note*50
    #     print("50  = ",note)
        
    # if num>=20:
    #     rem = num%20
    #     note = (num - rem) / 20
    #     num = num - note*20
    #     print("20  = ",note)
        
    # if  num>=10: 
    #     rem = num%10
    #     note = (num - rem) / 10
    #     num = num - note*10
    #     print("10  = ",note)    
        
    # if num>=5:
    #     rem = num%5
    #     note = (num - rem) / 5
    #     num = num - note*5
    #     print("5  = ",note)

    # if  num>=2: 
    #     rem = num%2
    #     note = (num - rem) / 2
    #     num = num - note*2
    #     print("2   = ",note)
        
    # print("1   = ",num)  


notesneed(2234)
