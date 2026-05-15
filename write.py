f=open('index.html','r')
h=f.read()
f.close()
old='<button class="app-btn" style="background:rgba(255,255,255,0.06);color:#8B8BA8;border:1px solid rgba(255,255,255,0.1);">Coming Soon</button>'
new='<a href="progress.html" style="display:inline-block;background:linear-gradient(135deg,#A78BFA,#8B5CF6);color:#fff;padding:14px 28px;border-radius:12px;font-weight:700;text-decoration:none;font-size:15px">Open App →</a>'
print('found:',old in h)
h=h.replace(old,new)
open('index.html','w').write(h)
print('done')