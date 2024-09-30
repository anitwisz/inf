from unittest import skipIf


def funk1 ():
    for i in range (1,11):
        print(i)


def funk2 (N):
    for i in range (1, N+1):
        print(i)


def funk3 ():
    for i in range (5, 16, 2):
        print(i)


def funk4 (N):
    for i in range (1, N+1):
        print(i, i**2)




def funk5 (odkial, pokial):
    for i in range (odkial, pokial+1):
        print(i, round (i**0.5, 2))




def funk6 ():
    for i in range (1,21):
        x = i
        if x == 3:
            y = "funkcia je nedefinovana"

        else:
            y = (x ** 2 - 1) / (x - 3)
        print (x, y)


def funk7 (N):
    for i in range (1, N+1):
        if i % 3 == 0:
            print(i)


def funk8 ():
    for i in range (1,21):
        if i % 2 == 0:
            print(i)


def funk9 (z, k):
    for i in range (z, k+1):
        if i % 2 != 0:
            print(i)



def funk10 (N):
    for i in reversed(range (1, N+1)):
        print(i)


def funk11 (N):
    for i in range (0, N+1):
        if i % 4== 0 or i % 7 == 0:
            print(i)



def funk12 (N):
    for i in range (1, N+1):
      x = ()
      print(x)



funk12(5)

