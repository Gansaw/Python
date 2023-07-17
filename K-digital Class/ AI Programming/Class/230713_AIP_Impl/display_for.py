def displayWithLoop(file):
    infile = open(file, 'r')
    # for line in infile:
    #     print(line.rstrip())

    # listPres = [line.rstrip() for line in infile]

    line = infile.readline()
    while line != "":
        print(line.rstrip())
        line = infile.readline()

    infile.close()

    # print(listPres)

displayWithLoop('FirstPresidents.txt')
