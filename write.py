f=open('readlead.html','r')
h=f.read()
f.close()
fn='function flipToggle(){\n'
fn+='ownText=!ownText;\n'
fn+='var tog=document.getElementById("tog");tog.classList.toggle("on",ownText);\n'
fn+='document.getElementById("tog-lbl").textContent=ownText?"Using classroom book or decodable":"Using a ReadLead passage";\n'
fn+='document.getElementById("tog-l").style.fontWeight=ownText?"400":"700";\n'
fn+='document.getElementById("tog-l").style.color=ownText?"#AAA":"#1A1A2E";\n'
fn+='document.getElementById("tog-r").style.fontWeight=ownText?"700":"400";\n'
fn+='document.getElementById("tog-r").style.color=ownText?"#1A1A2E":"#AAA";\n'
fn+='document.getElementById("own-msg").style.display=ownText?"block":"none";\n'
fn+='document.getElementById("passage-card").style.display=ownText?"none":"block";\n'
fn+='}\n'
h=h.replace('function addErr()',fn+'function addErr()')
open('readlead.html','w').write(h)
print('done flipToggle:','function flipToggle' in h)