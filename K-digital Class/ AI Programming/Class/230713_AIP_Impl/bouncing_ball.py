coef = float(input('Enter coefficient of resitution: '))
height = float(input('Enter initial height in meters: '))

# 공이 튕긴 전체 거리의 합
distance = height
num = 1

while height*coef > 0.1:
    height *= coef          # 튀어오를 높이
    distance += height*2.0  # 올라갔다 내려옴
    num += 1                # 튕긴 횟수 1 증가

print('Number of bounces: {}'.format(num))
print('Meters traveled: {:.2f}'.format(distance))