import math

def add_digits(n):
    auxd = 0
    add=0

    while n != 0:
        digit = n % 10
        add += digit
        auxd += digit
        n //= 10
    return add

def most(a,b): 
    if (a>b): 
        return a
    else: 
        return b 

def least(a,b): 
    if(a < b):
        return a
    else: 
        return b 

#Funciones ahorcado:

def guess(word, guess):
    display = ""
    for letter in word:
        if letter in guess:
            display += letter
        else:
            display += "_"
    return display

#TP5
#1
def comprobation(dni):

    if (len(dni) == 7) or (len(dni) == 8):
        return True
    else:
        return False
    
#2
def word_lenght(word):
    last = str(word).split(" ")
    return len(last[-1])

#3
def wordselector(info, pos):
    split = str(info).split(" ")
    return str(split[pos])

def three_first_dni(dni):
    first= dni[0:3]
    return first

#4
def multiple(num, num2):
    if(num % num2 == 0):
        print(f"El primer numero ({num}) es multiplo de el segundo ({num2})")
    elif(num2 % num == 0):
        print(f"El segundo numero ({num2}) es multiplo de el primero ({num})")
    else:
        print("No son multiplos del otro. ")

#5
def temperature(min, max):
    average = (min + max)/2
    return average

#6
def spaces(phrase):
    final = ""
    for i in phrase:
        final += i + " "
    return final

#7
def min_max(nums):
    min_val = max_val = nums[0]
    for i in nums:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
    return min_val, max_val

#8 
def area_per_circle(radio):
    area = math.floor((math.pi * radio) **2)
    peri = math.floor(2 * math.pi * radio)
    return area, peri

#9
def login(user, password, count):
    if (user == "usuario1") and (password == "asdasd"):
        return True
    else:
        count += 1
        print(f"Usuario o contraseña incorrectos. Intente nuevamente. Ya ha intentado {count} veces. Recuerde q tiene 3 intentos.")
    return False

#10 HECERLOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def discount(dicc):

#11
def multi(num):
    return (num *2)

def list_func(list1, multi):
    ans = []
    for i in list1:
        num = multi(i)
        ans.append(num)
    return ans