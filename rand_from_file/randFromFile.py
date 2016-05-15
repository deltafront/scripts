import sys

__author__ = 'charlie'
from random import randint

def main(args):
    filename = args[1]
    remove = args[3]
    num_to_remove = int(args[2])
    remove = True if remove.upper().find("T") != -1 else False
    print("Filename: %s\nRemove: %s \nNumber to remove: %s" % (filename,remove,str(num_to_remove)))
    lines = get_lines(filename)
    outputs = []
    for i in range(0,num_to_remove):
        output = get_random_line(lines, bool(remove))
        lines = output[1]
        outputs.append(output[0])
    write_lines(lines,filename)
    print_lines(outputs)


def get_lines(filename):
    f = open(filename)
    lines = f.readlines()
    #print("Returning %s lines from %s\n%s" % (len(lines),filename,str(lines)))
    return lines


def write_lines(lines, filename):
    print("Writing %s lines to %s\n%s" % (len(lines),filename,str(lines)))
    f = open(filename,"w")
    f.writelines(lines)
    f.close()

def get_random_line(lines,remove=True):
    num = randint(0, len(lines)-1)
    #print("Removing item number %s" % str(num))
    out = lines[num]
    if remove:
        del lines[num]
    #print("Returning value %s" % out)
    return out,lines

def print_lines(lines):
    out = ""
    for line in lines:
        out += "%s" % line
    print out

if __name__ == "__main__":
    main(sys.argv)
