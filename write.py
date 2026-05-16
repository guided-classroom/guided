f=open('readlead.html','r')
h=f.read()
f.close()
old='<div class="lbl">CURRICULUM STANDARDS (OPTIONAL)</div>'
new='<div class="lbl">CURRICULUM EXPECTATIONS (OPTIONAL)</div>'
h=h.replace(old,new)
old='placeholder="Paste your district standards here"'
new='placeholder="Copy and paste specific curriculum expectations for this student (e.g. Reading 1.2: Uses phonics strategies to decode unknown words)"'
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')