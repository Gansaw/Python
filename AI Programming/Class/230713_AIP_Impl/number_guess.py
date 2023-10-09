number = 23
running = True

while running:
    guess = int(input('Number: '))

    if guess == number:
        print('Good')
        running = False
        # break
    elif guess < number:
        print('higher')
    else:
        print('lower')
else:
    print('The while loop is over.')

print('Done')