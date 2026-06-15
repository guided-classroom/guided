f=open('rotator.html','r')
h=f.read()
f.close()
old='<div class="logo" id="sched-logo" style="margin-left:4px">CentreRotator</div>'
new='<div class="logo" id="sched-logo" style="margin-left:4px;color:#1A1A2E">Centre<span style="color:#A78BFA">Rotator</span></div>'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')