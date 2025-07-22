CustomerID=[1001,1002,1003,1004,1005,1006,1007,1008]
key=int(input("Enter a Customer-ID:"))
flag=0
for i in CustomerID:
    if(i==key):      
        flag=1
        
    else:
        flag=0
if(flag==1):
    print(f"Customer ID FOUND",{i})
else:
    print(f"Customer ID Not Found",{key})