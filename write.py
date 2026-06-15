f=open('rotator.html','r')
h=f.read()
f.close()
old='.proj{display:none;position:fixed;inset:0;background:#1E2A3A;z-index:200;padding:24px;overflow-y:auto;}'
new='.proj{display:none;position:fixed;inset:0;background:#1E2A3A;color:#fff;z-index:200;padding:24px;overflow-y:auto;}'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')