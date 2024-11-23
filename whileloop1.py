num = 8

while num>2:
    if num!= 6:
        print(num)
    elif num ==4:
        break
    num= num-1
print("while loop execution is done")

##iteration , break(exits while loop) , continue(skip the remaining part and moves to next iteration)

it = 10

while it>1:
    if it == 8:
        it = it-1
        continue
    if it == 3:
        break
    print(it)

    it = it -1 
    
print ("final it is "+str(it))