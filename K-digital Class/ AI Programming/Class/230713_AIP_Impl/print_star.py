
numberOfRows = int(input('Enter a number: '))

"""
입력이 5일때 출력 예시:
*++++
**+++
***++
****+
*****
****+
***++
**+++
*++++
"""

for i in range(numberOfRows):
    for j in range(i+1):
        print('*', end='')
    for j in range(numberOfRows-i-1):
        print('+', end='')
    print()
for i in range(numberOfRows):
    for j in range(numberOfRows-i-1):
        print('*', end='')
    for j in range(i+1):
        print('+', end='')
    print()