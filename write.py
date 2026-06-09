f=open('readlead.html','r')
h=f.read()
f.close()
old='function showProg(id){\nvar stu=students.find(function(s){return s.id===id;});\n'
new='function showProg(id){\nconsole.log("showProg called with id:",id);\nvar stu=students.find(function(s){return s.id===id;});\nconsole.log("student found:",stu?stu.name:"not found");\n'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')