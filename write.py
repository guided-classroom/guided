f=open('rotator.html','r')
h=f.read()
f.close()
old='<div style="font-weight:700;color:${g.color};font-size:13px">${g.name}</div>\n<div style="font-size:11px;color:#AAA">'
new='<div style="font-weight:700;color:${g.color};font-size:16px">${g.name}</div>\n<div style="font-size:14px;color:#AAA">'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')