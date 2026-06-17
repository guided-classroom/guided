f=open('readlead.html','r')
h=f.read()
f.close()
old='PASSAGES["Level 1"]'
new='var PASSAGES={};\nPASSAGES["Level 1"]'
print('found:',old in h)
h=h.replace(old,new,1)
open('readlead.html','w').write(h)
print('done')