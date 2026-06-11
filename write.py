f=open('rotator.html','r')
h=f.read()
f.close()
old=").join('');\n}"
new=").join('');\nsetTimeout(addActivityButtons,500);\n}"
print('found:',old in h)
h=h.replace(old,new,1)
open('rotator.html','w').write(h)
print('done')