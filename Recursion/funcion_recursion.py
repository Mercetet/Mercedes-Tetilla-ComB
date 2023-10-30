#Tp8
import math

# 1
def count_dig(num):
    count = 0
    if num < 10:
        return 1
    else:
        return 1 + count_dig(num//10)

# 2
def power_num(n, b):
    if n == 1:
        return True
    if n < b:
        return False
    if n%b == 0:
        return power_num(n // b, b)
    else:
        return False
# 3
def search_str(a, b, start = 0):
    pos = a.find(b, start)

    if pos == -1:
        return []
    pos2 = [pos]
    pos2 += search_str(a,b,pos+1)

    return pos2

# 4
def even_num(num):
    if num==0:
        return True
    else:
        return uneven_num(num-1)

def uneven_num(num):
    if num == 0:
        return False
    else:
        return even_num(num-1)

# 5
def max_num(list_num, max_num_v = None, pos = 0):
    if pos == len(list_num):
        return max_num_v
    if max_num_v is None or list_num[pos] > max_num_v:
        max_num_v = list_num[pos]
    return max_num(list_num, max_num_v, pos+1)

# 6
def repeat_list(list_num, n):
    if not list_num:
        return []
    else:
        return [list_num[0]]*n + repeat_list(list_num[1:], n)

# 7
def add_mult(n, p):
    if n == 1:
        return p
    else:
        return n*p + add_mult(n-1, p)
    
# 8
def pascal(n, k):
    if k == 0 or k ==n:
        return 1
    else:
        return pascal(n-1, k-1)+pascal(n-1, k)

# 9
def conbinations(list_ch, k, new_str=""):
    if k==0:
        return [new_str]
    new_list =[]
    for i in list_ch:
        new_list.append(conbinations(list_ch, k-1, new_str+i))
    return new_list

# 10 
def paper_size(n):
    if n == 0:
        return (841, 1189)
    else:
        width, length = paper_size(n-1)
        return length//2, width