f = open('\data\temp_fich', 'wb+')
f.write(b'0123456789abcdef')
16
f.seek(5,0)
5
f.read(2)
b'56'
f.seek(-2,1)
5
f.read(4)
b'5678'
f.tell()
9
f.seek(-5, 2)
11
f.read(2)
b'bc'
f.close()
