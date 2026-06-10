f=open('rotator.html','r')
h=f.read()
f.close()
old='function addActivityButtons(){\nvar preview=document.getElementById("groups-preview");\nif(!preview)return;\nvar cards=preview.querySelectorAll("div[style]");\nREADLEAD_GROUPS.forEach(function(g,i){\nif(!cards[i])return;\nvar btn=document.createElement("button");\nbtn.textContent="Get Activity Ideas";\nbtn.style="background:#A78BFA;color:#1A1A2E;border:none;border-radius:8px;padding:6px 14px;font-size:11px;font-weight:700;cursor:pointer;margin-top:8px;display:block;";\nbtn.onclick=function(){genGroupActivity(g.name,g.weakSkill,g.students.join(","));}\ncards[i].appendChild(btn);\n});\n}'
new='function addActivityButtons(){\nvar preview=document.getElementById("groups-preview");\nif(!preview)return;\nvar cards=Array.from(preview.children);\nREADLEAD_GROUPS.forEach(function(g,i){\nif(!cards[i])return;\nvar btn=document.createElement("button");\nbtn.textContent="Get Activity Ideas";\nbtn.style="background:#A78BFA;color:#1A1A2E;border:none;border-radius:8px;padding:6px 14px;font-size:11px;font-weight:700;cursor:pointer;margin-top:8px;display:block;width:100%;";\nbtn.addEventListener("click",function(){genGroupActivity(g.name,g.weakSkill,g.students.join(","));});\ncards[i].appendChild(btn);\n});\n}'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')