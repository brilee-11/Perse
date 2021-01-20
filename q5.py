a = ['wibble', 'wobble', 'wibble', 'wobble', 'jelly', 'on', 'the', 'plate']
word = input()
x = a.index(word)
print(' '.join(a[x+1:x+int(input())+1]))
#correct