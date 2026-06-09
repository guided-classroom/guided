f=open('readlead.html','r')
h=f.read()
f.close()
old='students[idx].level=l;\nstudents[idx].grade=LM[l][0];\nsaveStudents();\ndocument.body.removeChild(overlay);\nrdDash();\nloadDashCurr();'
new='students[idx].level=l;\nstudents[idx].grade=LM[l][0];\nsaveStudents();\ndocument.body.removeChild(overlay);\nif(cur&&cur.id==id){cur=students[idx];pidx=0;}\nrdDash();\nloadDashCurr();'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')