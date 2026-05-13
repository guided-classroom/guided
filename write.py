f=open('readlead.html','r')
h=f.read()
f.close()
h=h.replace('function startSess(id){','function startSess(id){alert("startSess called! id="+id);')
open('readlead.html','w').write(h)
print('done'