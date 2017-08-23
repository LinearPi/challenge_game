import re  
file = open('D:\Program Files\ChromeGAE\data2.txt')  
ans = ''  
tmp = file.read()  
pattern = "[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"  
temp = ''  
for match in re.findall(pattern,tmp):  
    temp += match[4]  
print (temp  )
