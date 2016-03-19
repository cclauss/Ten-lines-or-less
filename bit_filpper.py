# coding: utf-8

# https://forum.omz-software.com/topic/2943/trying-to-make-an-encrypted-message-system
# a poor man's encryption

def bit_flipper(s):
    return ''.join([chr(ord(x) ^ 1) for x in s])

s = 'Pythonista rules!   ¥€$ īt döèš'
print(s)
s = bit_flipper(s)
print(s)
s = bit_flipper(s)
print(s)
