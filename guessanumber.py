import random2
num = random2.randint(0,100)
times = 0

print "Number(0,100) guess game"
print "You will have 10 times to guess"
print "Guess out of range will game over immediately!"

guess = int(raw_input("guess a number:"))
times = times + 1

while 0 <= guess <= 100:
    if times == 10:
        if guess > num:
            print "Too high,The number is",num
            print "Guess times over,game over!"
        elif guess < num:
            print "Too Low,The number is",num
            print "Guess times over,game over!"
        else:
            print "You guess it.The number is:",num
            score = 10*(11-times)
            print "times is:",times
            print "Your score is",score
        break
    else:
        if guess > num:
            print "Too high,guess again!"
        elif guess < num:
            print "Too Low,guess again!"
        else:
            print "You guess it.The number is:",num
            score = 10*(11-times)
            print "times is:",times
            print "Your score is",score
            break
        guess = int(raw_input("guess a number:"))
        times = times + 1
else:
    print "Your guess is out of range!Game over!"