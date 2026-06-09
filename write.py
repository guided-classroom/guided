f=open('readlead.html','r')
h=f.read()
f.close()
old='var ebtn=document.getElementById("ebtn-"+s.id);if(ebtn){ebtn.addEventListener("click",function(){editLevel(s.id);});}'
new='var ebtn=document.getElementById("ebtn-"+s.id);if(ebtn){ebtn.addEventListener("click",function(){editLevel(s.id);});}var pbtn=document.getElementById("pbtn-"+s.id);if(pbtn&&s.sessions&&s.sessions.length>0){pbtn.addEventListener("click",function(){showProg(s.id);});}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')