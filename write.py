f=open('rotator.html','r')
h=f.read()
f.close()
old='body{font-family:\'DM Sans\',sans-serif;background:#1E2A3A;color:#fff;min-height:100vh;}'
new='body{font-family:\'DM Sans\',sans-serif;background:#F5F7FF;color:#1A1A2E;min-height:100vh;}'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')