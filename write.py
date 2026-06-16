f=open('readlead.html','r')
h=f.read()
f.close()
old='delBtn.addEventListener("click",function(){\nstudents=students.filter(function(s){return s.id!=id;});\nsaveStudents();\ndocument.body.removeChild(overlay);\nrdDash();\nloadDashCurr();\n});'
new='delBtn.addEventListener("click",async function(){\ntry{\nawait _supabase.from("students").delete().eq("id",id);\nstudents=students.filter(function(s){return s.id!=id;});\n}catch(e){console.error("delete error",e);}\ndocument.body.removeChild(overlay);\nrdDash();\nloadDashCurr();\n});'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')