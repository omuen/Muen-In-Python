import random
g=random.randint(1,10)
f=int(input('Guess a number between 1 and 10 : '))
while f != g:
    if f>g:
        print(f,' was too high')
    if f<g:
        print(f,' was too low')
    f=int(input('Guess again: '))
print(f,'is the number.Well Done.')