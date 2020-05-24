# s = '1,2,3,6,7,8,10,12\n 9,10,20\n 21,31,24'
# with open('Digtal.txt','w') as fp:
#     fp.write(s)
# with open('Digtal.txt') as fp:
#     print(fp.read())

# with open('Digtal.txt','r') as fp:
#     txt = fp.readlines()
#     print(txt)
# txt = [line.strip() for line in txt]
# print(txt)
# txt = ','.join(txt)
# print(txt)
# txt = txt.split(',')
# print(txt)
# txt = [int(item) for item in txt]
# print(txt)
# txt.sort()
# print(txt)
# txt = ','.join(map(str,txt))
# print(txt)
# with open('Digtal.txt','w') as fp:
#     fp.write(txt)

with open('Digtal.txt') as fp:
    txt = fp.readlines()
txt = [line.strip() for line in txt]
txt = ','.join(txt)
txt = txt.split(',')
txt = list(map(int, txt))
txt.sort()
txt = list(map(str, txt))
txt = ','.join(txt)
print(txt)

