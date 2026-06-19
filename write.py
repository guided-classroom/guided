f=open('rotator.html','r')
h=f.read()
f.close()
old="function init() {\n// Mode card features"
new="function init() {\ninitAuth();\n// Mode card features"
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')