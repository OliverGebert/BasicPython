#!/usr/bin/python

import math
import random as rand
import time


def factorial(n):
    """returns the factorial frm 1 up to provided number"""
    return 1 if n==0 else n*factorial(n-1)

def fibonacci(n):
    """returns the fibonacci number at position n"""
    i=n-1
    a=0
    b=1
    while i!=0:
        a, b = b, a+b
        i=i-1
    return a        

def golden(n):
    """returns the golden ratio at position n"""
    return fibonacci(n)/fibonacci(n+1)

def umfang(n):
    """returns the umfang of a circle with radius n"""""
    return n*math.pi

def flaeche(n):
    """returns the flaeche of a circle with radius n"""""
    return math.pi*n**2

def quersumme(n):
    """returns the sum of the digits of a number"""""
    crosssum = 0
    digits = str(n)
    for digit in digits:
        crosssum += int(digit)
    return crosssum

def bmi(h, w):
    """returns the bmi of a person with height h and weight w"""
    return float(w)/(h/100)**2

def bmi_rating(bmi):
    """returns the bmi rating of a person with bmi"""
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 35:
        return "Übergewicht"
    else:
        return "Adipositas"

def remainder(n):
    """returns the remainder of a division of n by 2"""
    return n%2 == 0

def leapyear(n):
    """returns whether a year is a leapyear or not"""
    leap = False
    if n%4 == 0:
        leap = True
        if n%100 == 0:
            leap = False
            if n%400 == 0:
                leap = True
    return leap

def returnRandom(n):
    return rand.randint(1,n)

def returnState(n):
    bundesland = ["Berlin", "Hamburg", "Bremen",
                  "Bayern", "Sachsen", "Brandenburg",
                  "Mecklenburg Vorpommern", "Saarland",
                  "Niedersachsen", "Thüringen",
                  "Rheinland Pfalz", "Hessen",
                  "Nordrheinwestpfahlen", "Baden-Württemberg",
                  "Sachsen Anhalt","Schleswig-Holstein"]
    return bundesland[n-1].title()    # capitalize each first letter

def mittelwert(werte):
    sum = 0
    for wert in werte:
        sum += wert
    return sum/len(werte)

def fizzbuzz(last):
    answer = "\n"
    for i in range(1,last+1):
        if i%3==0 and i%5==0:
            answer += "FizzBuzz\n"
        elif i%3==0:
            answer += "Fizz\n"
        elif i%5==0:
            answer += "Buzz\n"
        else:
            answer += str(i) + "\n"
    return answer

def password(l, s, n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>/?`~"
    numbers = "1234567890"
    pwd = ""
    schema = 'l'*l + 's'*s + 'n'*n
    while schema:
        t = rand.choice(schema)        # this would also work with a list and the random.shuffle(list) function
        schema = schema.replace(t,'',1)
        if t == 'l':
            pwd += rand.choice(letters)
        if t == 's':
            pwd += rand.choice(symbols)
        if t == 'n':
            pwd += rand.choice(numbers)
    return pwd

def encode(shift, cypher):
    tableList = list("abcdefghijklmnopqrstuvwxyz0123456789")
    cypherList = list(cypher.lower())
    for position in range(len(cypherList)):
        if cypherList[position] in tableList: # only cypher if part of tableList, keep symbols
            cypherList[position] = tableList[(tableList.index(cypherList[position])+shift)%len(tableList)]
    return "".join(cypherList)

def prime(number):
    return all((number%x != 0) for x in range(3, number-1, 2))


# ----- MAIN -----

print("die aktuelle Uhrzeit: " + time.asctime() + "\n")
print("(1) give factorial numer")
print("(2) give fibonacci number")
print("(3) give golden number based on fibunacci")
print("(4) Kreisumfang von Radius")
print("(5) Kreisflaeche von Radius")
print("(6) Quersumme")
print("(7) Body mass index (h, w)")
print("(8) number is odd")
print("(9) ist es ein Schaltjahr")
print("(a) Zufallszahl von 1..n")
print("(b) Bundesland zurück geben")
print("(c) Mittelwert bestimmen [int]")
print("(d) provide fizzbuzz to n")
print("(e) generate pwd with letters, symbols and numbers")
print("(f) en/decode (+/-) cesar cipher")
print("(g) check prime number")
choice = input("what to do? ")
param = input("input parameter(s): ").split()

match choice:
    case '1':
        print ("factorial is:", factorial(int(param[0])))
    case '2':
        print ("fibonacci is:", fibonacci(int(param[0])))
    case '3':
        print ("goldene zahl : ", golden(int(param[0])))
    case '4':
        print (f"umfang : {umfang(int(param[0])):.2f}")
    case '5':
        print (f"flaeche : {flaeche(int(param[0])):.2f}")
    case '6':
        print ("quersumme : ", quersumme(int(param[0])))
    case '7':
        print (f"BMI: {round(bmi(int(param[0]), int(param[1])),2)}")
        print (f"BMI Rating: {bmi_rating(bmi(int(param[0]), int(param[1])))}")
    case '8':
        print (f"number is odd: {remainder(int(param[0]))}")
    case '9':
        print ("is leap year: {}".format(leapyear(int(param[0]))))
    case 'a':
        print(f"die Zufallszahl lautet :{returnRandom(int(param[0])):->20}")
    case 'b':
        print(f"das Bundesland ist :{returnState(int(param[0])):.>25}")
    case 'c':
        print(f"der Mittelwert ist :{mittelwert(int(param[0])):.2f}")
    case 'd':
        print(f"fizzbuzz numbers: {fizzbuzz(int(param[0]))}")
    case 'e':
        print(f"das passwort lautet: {password(int(param[0]), int(param[1]), int(param[2]))}")
    case 'f':
        print(f"the en/decoded text is: {encode(int(param[0]), param[1])}")
    case 'g':
        print(f"the number is prime number: {prime(int(param[0]))}")
    case default:
        print ("falsche Auswahl, code terminates")