f=open('readlead.html','r')
h=f.read()
f.close()
fn='function startSess(id){\n'
fn+='cur=students.find(function(s){return s.id===id;});\n'
fn+='rats=Object.assign({},(cur.sessions[0]&&cur.sessions[0].ratings)||{});\n'
fn+='errs=[];ownText=false;lesson=null;pidx=0;\n'
fn+='document.getElementById("obs-title").textContent="Session: "+cur.name;\n'
fn+='document.getElementById("obs-sub").innerHTML=tag(cur.level,lc(cur.level))+" "+lb(cur.level)+" - "+cur.grade;\n'
fn+='document.getElementById("tog").classList.remove("on");\n'
fn+='document.getElementById("tog-lbl").textContent="Using a ReadLead passage";\n'
fn+='document.getElementById("tog-l").style.fontWeight="700";\n'
fn+='document.getElementById("tog-r").style.fontWeight="400";\n'
fn+='document.getElementById("own-msg").style.display="none";\n'
fn+='document.getElementById("passage-card").style.display="block";\n'
fn+='document.getElementById("w-in").value="";\n'
fn+='document.getElementById("s-in").value="";\n'
fn+='document.getElementById("curr-in").value="";\n'
fn+='document.getElementById("curr-badge").style.display="none";\n'
fn+='rdErrs();rdRats();rdPass();\n'
fn+='document.getElementById("gen-box").innerHTML="<div style=\'font-size:15px;font-weight:800;margin-bottom:4px\'>Generate Lesson Plan</div><button class=\'btn btn-teal\' style=\'width:100%;font-size:14px\' onclick=\'doGen()\'>Generate "+cur.name+" Lesson</button>";\n'
fn+='go("observe");\n'
fn+='}\n'
h=h.replace('populateLvl();',fn+'populateLvl();')
open('readlead.html','w').write(h)
print('done startSess in file:','startSess(id)' in h)