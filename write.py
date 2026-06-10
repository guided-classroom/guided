f=open('rotator.html','r')
h=f.read()
f.close()
lines=h.split('\n')
lines[365]='<div style="font-size:11px;color:#8B949E">${g.students.join(", ")}${currentMode==="skill"?" · "+g.weakSkill:""}</div>'
h='\n'.join(lines)
open('rotator.html','w').write(h)
print('done')