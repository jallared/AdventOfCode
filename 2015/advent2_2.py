import string

length=0
input = open('input_2.txt', 'r')
for rad in input:
	lista = rad.split('x')
	lista = map(int,lista)
	lista.sort()
	w, l, h = lista
	length += 2*w + 2*l + w*h*l
print length	
input.close()