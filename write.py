f=open('rotator.html','r')
h=f.read()
f.close()
old='.logo{font-family:\'Playfair Display\',serif;font-size:20px;font-weight:900;}'
new='.logo{font-family:\'Playfair Display\',serif;font-size:22px;font-weight:900;color:#fff;}'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')