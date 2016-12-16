import string

area=0
input = open('input_2.txt', 'r')
for rad in input:
	lista = rad.split('x')
	lista = map(int,lista)
	lista.sort()
	w, l, h = lista
	area += w*l + 2*l*w + 2*w*h + 2*h*l
print area	
input.close()