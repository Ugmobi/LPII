string = "hello world"  
a = len(string)  
for x in range(a):  
 ans1=x & 127 
print("AND OPERATION",ans1) 
for y in range(a):  
 ans2=y | 127  
print("OR OPERATION]", ans2)  
for z in range(a): 
 ans3=2 ^ 127  
print("EXOR OPERATION", ans3)