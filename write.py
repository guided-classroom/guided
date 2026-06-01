f=open('readlead.html','r')
h=f.read()
f.close()
old='if(scr==="dash")rdDash();\n'
new='if(scr==="dash"){rdDash();loadDashCurr();}\n'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')