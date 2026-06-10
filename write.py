f=open('rotator.html','r')
h=f.read()
f.close()
old=").join('');\n}\n\nf"
new=").join('');\naddActivityButtons();\n}\n\nf"
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')