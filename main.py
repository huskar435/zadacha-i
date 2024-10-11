input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
b = 0
if a > 0:
    for i in range (1,a+1):
        b = b + i
else:
    if a < 0:
        for i in range (a,2):
         b = b + i
l = str(b)
output_data = open("output.txt","w")
output_data.write (l)
input_data.close()
output_data.close()       



    
