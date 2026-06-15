f=open('rotator.html','r')
h=f.read()
f.close()
old='id="setup-logo" style="color:#1A1A2E">Centre<span style="color:#4ECDC4">Rotator</span>'
new='id="setup-logo" style="color:#fff">Centre<span style="color:#A78BFA">Rotator</span>'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')