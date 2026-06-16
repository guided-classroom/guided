f=open('readlead.html','r')
h=f.read()
f.close()
i=h.find('async function editLevel')
j=h.find('\nasync function ',i+1)
print('removing lines',h[:i].count('\n')+1,'to',h[:j].count('\n')+1)
h=h[:i]+h[j:]
open('readlead.html','w').write(h)
print('done editLevel count:',h.count('function editLevel'))