f=open('readlead.html','r')
h=f.read()
f.close()
old='<div id="student-list"></div>'
new='<div id="student-list"></div><button onclick="startSess(1)" style="background:red;color:white;padding:20px;font-size:20px">TEST START MARCUS</button>'
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')