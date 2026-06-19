f=open('index.html','r')
h=f.read()
f.close()
old='<button class="btn-primary">Start Free Today →</button>'
new='<a href="login.html" class="btn-primary" style="text-decoration:none;display:inline-block;text-align:center">Get Lifetime Access →</a>'
print('found:',old in h)
h=h.replace(old,new)
open('index.html','w').write(h)
print('done')