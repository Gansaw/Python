def main():
    try:
        fileName = input('Enter a file name: ')
        infile = open(fileName, 'r')
        num = float(infile.readline())
        print(1/num)
    except Exception as exc:
        print('{} is occured'.format(exc.__class__.__name__))
        print(exc)
    else:
        print('No error occured')
    finally:
        infile.close()
        print('Try statement is finished')

main()



    # except FileNotFoundError as exc1:
    #     print('FileNotFoundError')
    #     print(exc1)
    # except ValueError as exc2:
    #     print('ValueError')
    #     print(exc2)
    # except ZeroDivisionError as exc3:
        # print('ZeroDivisionError')
    #     print(exc3)