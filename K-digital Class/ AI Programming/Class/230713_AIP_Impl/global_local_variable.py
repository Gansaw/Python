x = 50
y = 20

def main():
    func()
    print('x :', x)

def func():
    global x, y    # 글로벌 변수임을 알린다
    print('x is', x)
    x = 10
    print('x is now', x)

print('Global x before main:', x)
main()
print('Global x after main:', x)



# def main():
#     x = 2
#     print(str(x) + ' in main')
#     trivial()
#     print(str(x) + ' in main')

# def trivial():
#     x = 3
#     print(str(x) + ' in trivial')

# main()




# x = 50

# def func(x):
#     print('x is', x)
#     x = 2
#     print('x is now', x)

# func(x)
# print('Global x is', x)




