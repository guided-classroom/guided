f=open('rotator.html','r')
h=f.read()
f.close()
old='.centre-card{background:#1A1A2E;border:2px solid #4ECDC433;border-radius:12px;padding:16px;cursor:pointer;transition:all .15s;}'
new='.centre-card{background:#1A1A2E;border:2px solid #4ECDC433;border-radius:12px;padding:16px;cursor:pointer;transition:all .15s;color:#fff;}'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')