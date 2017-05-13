import os

path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path, 'Coding_605_Sandimirova.html')

f = open(path,'w')
f.write('<!DOCTYPE html>\n')
f.write('<html>\n')
f.write("<head>\n<meta charset='utf-8'>\n<title>Multiplication Table</title>\n</head>\n")
f.write('<body>\n')
f.write('<h1>Multiplication Table</h1>\n')
n = ''
for i in range(1, 11):
    f.write('<p>')
    for j in range(1, 11):
        if(j == 1):#для красоты
            n = str(i) + ' x ' + str(j) + ' = ' + str(i)
            f.write(n)
        else:
            n = '</br>' + str(i) + ' x ' + str(j) + ' = ' + str(i * j)
            f.write(n)
    f.write('</p>\n')
f.write('</body>\n')
f.write('<html>')
f.close()
