f=open('readlead.html','r')
h=f.read()
f.close()
old='"<div style=\'font-size:15px;font-weight:800;margin-bottom:4px\'>Generate Lesson Plan</div><button class=\'btn btn-teal\' style=\'width:100%;font-size:14px\' onclick=\'doGen()\'>Generate "+cur.name+" Lesson</button>"'
new='"<div style=\'font-size:15px;font-weight:800;margin-bottom:4px\'>Generate Lesson Plan</div><button class=\'btn btn-teal\' style=\'width:100%;font-size:14px;margin-bottom:8px\' onclick=\'doGen()\'>Generate "+cur.name+" Lesson</button><button class=\'btn-ghost\' style=\'width:100%;font-size:13px;margin-top:4px\' onclick=\'saveSessionOnly()\'>Save Session Without Lesson</button>"'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')