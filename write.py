f=open('rotator.html','r')
h=f.read()
f.close()
old="join('');\ndocument.getElementById('skill-features')"
new="join('');\nsetTimeout(addActivityButtons,100);\ndocument.getElementById('skill-features')"
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')