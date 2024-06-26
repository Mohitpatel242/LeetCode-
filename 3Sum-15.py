# nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0,0]
a = []
b = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                a.append([nums[i], nums[j], nums[k]])

for k in range(len(a)):
    a[k].sort()
    
if len(a) > 1:
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            b.append(a[i])
            print(b)
else:
    print(a)
    
        
    
               
                

