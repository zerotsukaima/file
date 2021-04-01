f = open('test_2.txt', 'w')
a = [1,7,9,5,3]
for i in a:
    f.write(str(i) + '\n')
f.close()