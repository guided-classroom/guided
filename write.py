f=open('index.html','r')
h=f.read()
f.close()
old='<button class="nav-link">Pricing</button>\n<button class="nav-cta">Get Started Free</button>'
new='<button class="nav-link">Pricing</button>\n<a href="login.html" class="nav-link" style="text-decoration:none;display:inline-block">Sign In</a>\n<a href="login.html" class="nav-cta" style="text-decoration:none;display:inline-block">Get Started Free</a>'
print('found:',old in h)
h=h.replace(old,new)
open('index.html','w').write(h)
print('done')