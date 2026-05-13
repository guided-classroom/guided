f=open('readlead.html','r')
h=f.read()
f.close()
old='cur=students.find(function(s){return s.id===id;});'
new='cur=students.find(function(s){return s.id==id;});'
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done fixed:','s.id==id' in h)