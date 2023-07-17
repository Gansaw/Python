def createWithWrite(L, outfile):
    for s in L:
        outfile.write(s + '\n')
        # outfile.write(s)
    outfile.close()

L = ['aa', 'bb', 'cc']
L2 = ['aabbab', 'badfbb', 'csadfsadc']

outfile = open('outfile_01.txt', 'w')
createWithWrite(L, outfile)

outfile2 = open('outfile_02.txt', 'w')
createWithWrite(L2, outfile2)


