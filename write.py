f=open('readlead.html','r')
h=f.read()
f.close()
old='rdErrs();rdRats();rdPass();'
new='rdErrs();rdRats();rdPass();loadSavedCurriculum();'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')