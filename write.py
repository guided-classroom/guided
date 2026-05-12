f=open('readlead.html','r')
content=f.read()
f.close()

missing=''
missing+='function addStu(){\n'
missing+='var n=document.getElementById("new-name").value.trim();if(!n)return;\n'
missing+='students.push({id:Date.now(),name:n,grade:document.getElementById("new-grade").value,level:document.getElementById("new-level").value,sessions:[]});\n'
missing+='document.getElementById("new-name").value="";\n'
missing+='go("dash");\n'
missing+='}\n'
missing+='function showProg(id){\n'
missing+='var stu=students.find(function(s){return s.id===id;});\n'
missing+='cur=stu;\n'
missing+='document.getElementById("prog-h").textContent="Progress: "+stu.name;\n'
missing+='document.getElementById("prog-sub").innerHTML=tag(stu.level,lc(stu.level))+" "+lb(stu.level)+" - "+stu.sessions.length+" sessions";\n'
missing+='var sess=stu.sessions||[];\n'
missing+='if(!sess.length){document.getElementById("prog-out").innerHTML="<div class=\'card\' style=\'text-align:center;padding:40px\'><div style=\'font-weight:700;margin-bottom:10px\'>No sessions yet</div><button class=\'btn\' onclick=\'startSess("+stu.id+")\'>Start First Session</button></div>";}\n'
missing+='else{\n'
missing+='var bars=QR.map(function(r){var curr=sess[0].ratings[r.id]||75,prev=sess.length>1?(sess[1].ratings[r.id]||75):null,diff=prev!==null?curr-prev:null;var c=curr>=90?"#6BCB77":curr>=75?"#FFD166":"#FF6B6B";return"<div style=\'margin-bottom:12px\'><div style=\'display:flex;justify-content:space-between;margin-bottom:4px\'><span style=\'font-size:13px;font-weight:600\'>"+r.l+"</span><span style=\'font-weight:800;color:"+c+"\'>"+curr+"</span></div><div class=\'pbg\'><div class=\'pbar\' style=\'width:"+curr+"%;background:"+c+"\'></div></div></div>";}).join("");\n'
missing+='var hist=sess.map(function(s,i){return"<div style=\'padding:10px 0\'><div style=\'display:flex;justify-content:space-between;margin-bottom:6px\'><span style=\'font-weight:700;font-size:13px\'>"+s.date+"</span>"+tag(i===0?"Latest":"#"+(sess.length-i),i===0?"#4ECDC4":"#DDD")+"</div></div>";}).join("");\n'
missing+='document.getElementById("prog-out").innerHTML=(sess.length>=2?"<div class=\'card\'><div style=\'font-size:14px;font-weight:700;margin-bottom:12px\'>Latest vs Previous</div>"+bars+"</div>":"")+"<div class=\'card\'><div style=\'font-size:14px;font-weight:700;margin-bottom:12px\'>Session History</div>"+hist+"</div>";\n'
missing+='}\n'
missing+='go("progress");\n'
missing+='}\n'
missing+='function bldGroups(){\n'
missing+='var ws=students.filter(function(s){return s.sessions.length>0;});\n'
missing+='if(ws.length<2)return[];\n'
missing+='var tagged=ws.map(function(s){var r=s.sessions[0].ratings||{};var w=QR.reduce(function(min,q){return(r[q.id]||75)<(r[min.id]||75)?q:min;},QR[0]);return Object.assign({},s,{wid:w.id,wl:w.l,wa:avg(r)});});\n'
missing+='var bkts={};\n'
missing+='tagged.forEach(function(s){if(!bkts[s.wid])bkts[s.wid]=[];bkts[s.wid].push(s);});\n'
missing+='var pc={accuracy:"#FF6B6B",fluency:"#FFD166",decoding:"#FF9F43",selfmon:"#4ECDC4",comprehension:"#A78BFA"};\n'
missing+='return Object.entries(bkts).map(function(x){var q=QR.find(function(r){return r.id===x[0];});return{id:x[0],name:q.l+" Group",focus:q.l,members:x[1],color:pc[x[0]]||"#4ECDC4",avgScore:Math.round(x[1].reduce(function(a,s){return a+s.wa;},0)/x[1].length)};});\n'
missing+='}\n'

insert='async function doGrpLes'
content=content.replace(insert,missing+insert)
open('readlead.html','w').write(content)
print('done inserted',len(missing),'chars')