f=open('readlead.html','r')
h=f.read()
f.close()
old='students[idx].sessions=[rec].concat(students[idx].sessions).slice(0,10);\ncur=students[idx];\nsaveStudents();'
new='students[idx].sessions=[rec].concat(students[idx].sessions).slice(0,10);\ncur=students[idx];\nsaveStudents();\ntry{\nawait _supabase.from("students").update({sessions:students[idx].sessions}).eq("id",cur.id);\n}catch(e){console.error("session save error",e);}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')