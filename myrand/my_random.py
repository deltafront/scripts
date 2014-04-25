import sys

__author__ = 'charlie'
from random import randint

filename = "rand.txt"
def get_rand(upper):
    upper_limit = int(float(upper))
    lines = read()
    num = randint(0,upper_limit)
    while in_list(num,lines):
        num = randint(0,upper_limit)
    write(num)
    print(num)

def write(num):
    file = open(filename,"a+")
    file.write("%s\n" % num)
    file.close()

def read():
    file = open(filename,"a+")
    file.close()
    file = open(filename,"r")
    lines= file.readlines()
    file.close()
    print lines
    return lines

def in_list(num,list):
    found = False
    for number in list:
        if str(num) == number.strip():
            found = True
            break
    return found


if __name__ == "__main__":
    get_rand(sys.argv[1])