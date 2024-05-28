#! /usr/bin/env python3

import sys

SPECIAL_LIST = 'NUL,SOH,STX,ETX,EOT,ENQ,ACK,BEL,BS,HT,LF,VT,FF,CR,SO,SI,DLE,DC1,DC2,DC3,DC4,NAK,SYN,ETB,CAN,EM,SUB,ESC,FS,GS,RS,US'.split(',')
SPECIALS = {k: v for k,v in enumerate(SPECIAL_LIST)}
SPECIALS[0x7f]='DEL'

def chr_or_name(charcode: int) -> str:
    if charcode in SPECIALS:
        return SPECIALS[charcode]
    return chr(charcode)

def format_hexdigit(digit: int) -> str:
    if digit >= 0x10:
        return f'{digit-0x10>>4:1x}_'
    return f'_{digit:1x}'

def headline(is_landscape: bool) -> str:
    num_cols = 0x0F if is_landscape else 0x07
    width = 4 * (num_cols + 2)
    return \
        f'{"ASCII-Table":^{width}}\n' + \
        '='*width
        
landscape = '-l' in sys.argv

one_range, other_range =  (0x10,0x80+1,0x10), (0x0,0x0F+1,0x01)
if not landscape:
    one_range, other_range = other_range, one_range

print()
print()
print(headline(landscape))
print()
print('   ', end='')
for other_hexdigit in range(*other_range):
    print(f' {format_hexdigit(other_hexdigit)} ', end='')
for one_hexdigit in range(*one_range):
    print(f'\n{format_hexdigit(one_hexdigit)}:', end='')
    for other_hexdigit in range(*other_range):    
        print(f' {chr_or_name(one_hexdigit + other_hexdigit - 0x10):^3s}', end='')
print()
