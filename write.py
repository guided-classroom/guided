f=open('readlead.html','r')
h=f.read()
f.close()
fn='function saveSessionOnly(){\n'
fn+='if(!cur)return;\n'
fn+='var rec={date:new Date().toLocaleDateString(),ratings:Object.assign({},rats),errors:errs.slice()};\n'
fn+='var idx=students.findIndex(function(s){return s.id===cur.id;});\n'
fn+='students[idx].sessions=[rec].concat(students[idx].sessions).slice(0,10);\n'
fn+='cur=students[idx];\n'
fn+='saveStudents();\n'
fn+='document.getElementById("gen-box").innerHTML="<div style=\'font-size:14px;font-weight:800;color:#4ECDC4;margin-bottom:8px\'>Session Saved!</div><div style=\'font-size:12px;color:#9999BB;margin-bottom:12px\'>Data saved to student profile.</div><button class=\'btn btn-teal\' style=\'width:100%;font-size:14px;margin-bottom:8px\' onclick=\'doGen()\'>Generate Lesson</button><button class=\'btn-ghost\' style=\'width:100%;font-size:13px\' onclick=\'saveSessionOnly()\'>Save Again</button>";\n'
fn+='}\n'
h=h.replace('function addStu()',fn+'function addStu()')
open('readlead.html','w').write(h)
print('done saveSessionOnly:','function saveSessionOnly' in h)