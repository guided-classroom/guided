f=open('readlead.html','r')
h=f.read()
f.close()
i1=h.find('function rdDash()')
i2=h.find('function rdErrs()')
old=h[i1:i2]
new='function rdDash(){\n'
new+='document.getElementById("dash-sub").textContent=students.length+" students";\n'
new+='var grps=bldGroups();\n'
new+='var html="";\n'
new+='students.forEach(function(s,i){\n'
new+='html+="<div class=\'srow\'>";\n'
new+='html+="<div class=\'row\'>";\n'
new+='html+="<div class=\'av\' style=\'width:40px;height:40px;background:"+AVC[i%6]+";font-size:15px\'>"+s.name[0]+"</div>";\n'
new+='html+="<div><div style=\'font-weight:700;font-size:14px\'>"+s.name+"</div>";\n'
new+='html+="<div style=\'font-size:12px;color:#999\'>"+s.grade+" - "+lb(s.level)+" - "+s.sessions.length+" sessions</div>";\n'
new+='html+="</div></div>";\n'
new+='html+="<div class=\'row\'>";\n'
new+='html+="<button class=\'btn\' id=\'btn-"+s.id+"\'>Start</button>";\n'
new+='html+="</div></div>";\n'
new+='});\n'
new+='document.getElementById("student-list").innerHTML=html;\n'
new+='students.forEach(function(s){\n'
new+='document.getElementById("btn-"+s.id).addEventListener("click",function(){startSess(s.id);});\n'
new+='});\n'
new+='}\n'
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')