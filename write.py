f=open('rotator.html','r')
h=f.read()
f.close()
old='<div style="font-size:17px;font-weight:800;margin-bottom:4px">Ready to generate?</div>'
new='<div style="font-size:17px;font-weight:800;margin-bottom:4px;color:#fff">Ready to generate?</div>'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')