f=open('readlead.html','r')
h=f.read()
f.close()
old='headers:{"content-type":"application/json"}'
new='headers:{"content-type":"application/json","anthropic-dangerous-direct-browser-access":"true"}'
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done fixed:',h.count('anthropic-dangerous-direct-browser-access'))