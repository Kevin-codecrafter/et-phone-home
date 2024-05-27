from bitstring import ConstBitStream

with open('tux.bmp', 'rb') as binfile:
    stream = ConstBitStream(binfile.read())

print('bfType', chr(stream.read('u8')), chr(stream.read('u8')))
print('bfSize', stream.read('uintle32'))
stream.read('u32')
offset=stream.read('uintle32')
print('data offset', offset)
print('biSize', stream.read('uintle32'))
width=stream.read('intle32')
print('width', width)
# Might be bullshit but at least is somewhat works for this bitmap.
pos=stream.pos // 8
toskip = offset - pos 
print('Already read', pos, 'Bytes. So skipping', toskip)
for _ in range(toskip):
    stream.read('u8')

# Note we are going the wrong way around to tux will be headover...
count=0
while True:
    print('X' if stream.read('u1') else ' ', end='')
    count+=1
    if count>= width+4: #Why the heck? Seems I'm not the worlds best bitmap expert...
        print()
        count=0
# Also always end program by an exception, that's really good programming style...
