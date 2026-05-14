f=open('readlead.html','r')
h=f.read()
f.close()
import re
h=re.sub(r'sk-ant-[A-Za-z0-9_\-]+','REMOVED',h)
open('readlead.html','w').write(h)
print('done remaining:',h.count('sk-ant'))