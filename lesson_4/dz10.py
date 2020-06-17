
s = 'Adverts make children pester their parents to buy things for them.'

idx = s.find('h')
print(idx)
idx = s.rfind('h', idx)
print(idx)

x= (s[15:62])

print(s[0:15], x.replace('h', 'H'), s[62:], sep='')

