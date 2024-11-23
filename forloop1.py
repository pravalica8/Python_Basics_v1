# for loop -- List
obj = [6,2,3,4,7,9]
intsum = 0
for i in obj:
    #print(i)
    intsum = intsum+i

print("Sum of values in the list is "+str(intsum))

# sum of first 5 Natural numbers
sumNnum = 0
# range(i,j) - > i to j-1
for j in range(1,6):
    sumNnum = sumNnum +j
    
print("Sum of first five natutarl numbers is "+str(sumNnum))
print("**************************************")
for k in range(1,10,2):
    print(k)

print("*****************Skipping first index********************")
for m in range(8):
    print(m)