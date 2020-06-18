
s = input('Please enter your message:')

A = idx = s.find('h')
B = idx = s.rfind('h', idx)

x= (s[(A+1):B])

print(s[0:(A+1)], x.replace('h', 'H'), s[B:], sep='')


