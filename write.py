f=open('readlead.html','r')
h=f.read()
f.close()
old='<div class="lbl">COMPREHENSION QUESTIONS</div>\n<div id="p-qs"></div></div>\n'
new='<div class="lbl">COMPREHENSION QUESTIONS</div>\n<div id="p-qs"></div></div>\n<div id="err-guide" style="margin-top:10px;padding-top:10px;border-top:1px solid #F0F0F0"></div>\n'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')