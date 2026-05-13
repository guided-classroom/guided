f=open('readlead.html','r')
h=f.read()
f.close()
insert='''function startSess(id){
cur=students.find(function(s){return s.id===id;});
rats=Object.assign({},(cur.sessions[0]&&cur.sessions[0].ratings)||{});
errs=[];ownText=false;lesson=null;pidx=0;
document.getElementById("obs-title").textContent="Session: "+cur.name;
document.getElementById("obs-sub").innerHTML=tag(cur.level,lc(cur.level))+" "+lb(cur.level)+" - "+cur.grade;
var tog=document.getElementById("tog");tog.classList.remove("on");
document.getElementById("tog-lbl").textContent="Using a ReadLead passage";
document.getElementById("tog-l").style.fontWeight="700";
document.getElementById("tog-l").style.color="#1A1A2E";
document.getElementById("tog-r").style.fontWeight="400";
document.getElementById("tog-r").style.color="#AAA";
document.getElementById("own-msg").style.display="none";
document.getElementById("passage-card").style.display="block";
document.getElementById("w-in").value="";
document.getElementById("s-in").value="";
document.getElementById("curr-in").value="";
document.getElementById("curr-badge").style.display="none";
document.getElementById("curr-msg").style.display="none";
rdErrs();rdRats();rdPass();
document.getElementById("gen-box").innerHTML="<div style=\'font-size:15px;font-weight:800;margin-bottom:4px\'>Generate Lesson Plan</div><div style=\'font-size:12px;color:#9999BB;margin-bottom:14px\'>Builds a personalized 15-min lesson targeting all 6 pillars.</div><button class=\'btn btn-teal\' style=\'width:100%;font-size:14px\' onclick=\'doGen()\'>Generate "+cur.name+" Lesson</button>";
go("observe");
}
'''
h=h.replace('function rdPass()',insert+'function rdPass()')
open('readlead.html','w').write(h)