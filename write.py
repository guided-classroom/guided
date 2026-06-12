f=open('rotator.html','r')
h=f.read()
f.close()
old='.lbl{font-size:11px;font-weight:800;color:#AAA;display:block;margin-bottom:8px;letter-spacing:.06em;'
new='.lbl{font-size:14px;font-weight:800;color:#AAA;display:block;margin-bottom:8px;letter-spacing:.06em;'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')