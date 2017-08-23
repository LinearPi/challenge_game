file = open('D:\Program Files\ChromeGAE\data.txt')  
ans = ''  
tmp = file.read()  
for c in tmp:  
    if c.isalpha():  
        ans += c  
print ( ans ) 
