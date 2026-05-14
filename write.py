f=open('readlead.html','r')
h=f.read()
f.close()
old='<button onclick="startSess(1)" style="background:red;color:white;padding:20px;font-size:20px">TEST START MARCUS</button>'
h=h.replace(old,'')
open('readlead.html','w').write(h)
print('done removed:',old not in h)