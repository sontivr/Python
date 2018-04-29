import re

s = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(m or ['-1']))


'''
rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
Explanation

ee is located between consonant  and . 
Ioo is located between consonant  and . 
Oeo is located between consonant  and . 
eeeee is located between consonant  and .
'''
