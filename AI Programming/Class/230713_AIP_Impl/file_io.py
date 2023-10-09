file1 = open('file1.txt', 'w')
file1.write('100')
file1.close()

file2 = open('file2.dat', 'wb')
file2.write('100'.encode())
file2.close()