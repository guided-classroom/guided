f=open('rotator.html','r')
h=f.read()
f.close()
old='div class="logo" id="setup-logo">Centre<span>Rotator</span></div>'
new='div class="logo" id="setup-logo" style="color:#1A1A2E">Centre<span style="color:#4ECDC4">Rotator</span></div>'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')