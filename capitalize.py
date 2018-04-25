#!/usr/bin/python2.6
import re
import string

def capitalize(string):
    # str = string.split()
    #return ' '.join([str[i][0].upper() + str[i][1:] for i in range(len(str))])
    #def repl(m):
    #   return m.group(0).upper()

    return re.sub(r"(^|\s)[a-z]", lambda m: m.group(0).upper(), string)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)


