f=open('readlead.html','r')
h=f.read()
f.close()
h=h.replace(
'students.push({id:Date.now(),name:n,grade:document.getElementById("new-grade").value,level:document.getElementById("new-level").value,sessions:[]});\ndocument.getElementById("new-name").value="";\ngo("dash");',
'students.push({id:Date.now(),name:n,grade:document.getElementById("new-grade").value,level:document.getElementById("new-level").value,sessions:[]});\nsaveStudents();\ndocument.getElementById("new-name").value="";\ngo("dash");'
)
h=h.replace(
'students[idx].sessions=[rec].concat(students[idx].sessions).slice(0,10);\ncur=students[idx];',
'students[idx].sessions=[rec].concat(students[idx].sessions).slice(0,10);\ncur=students[idx];\nsaveStudents();'
)
open('readlead.html','w').write(h)
print('done saveStudents calls:',h.count('saveStudents()'))