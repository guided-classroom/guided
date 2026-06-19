f=open('index.html','r')
h=f.read()
f.close()
old='<button class="btn-secondary">Watch Demo</button>'
print('found:',old in h)
h=h.replace(old,'')
open('index.html','w').write(h)
print('done')