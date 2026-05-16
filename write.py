f=open('readlead.html','r')
h=f.read()
f.close()
old='max_tokens:2000,messages:[{role:"user",content:prompt}]'
new='max_tokens:3000,messages:[{role:"user",content:prompt}]'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')