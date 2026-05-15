f=open('rotator.html','r')
h=f.read()
f.close()
i=h.find('const READLEAD_GROUPS')
j=h.find('const ALL_CENTRES')
old=h[i:j]
new='function loadGroupsFromStorage(){\ntry{\nvar raw=localStorage.getItem("guided_students");\nif(!raw)return getDefaultGroups();\nvar students=JSON.parse(raw);\nif(!students.length)return getDefaultGroups();\nvar colors=["#FF6B6B","#FFD166","#4ECDC4","#6BCB77","#A78BFA","#FF9F43"];\nvar skillNames={accuracy:"Accuracy",fluency:"Fluency",decoding:"Decoding",selfmon:"Self-Monitoring",comprehension:"Comprehension"};\nvar groups={};\nstudents.forEach(function(s){\nvar key="all";\nvar focus="Mixed Skills";\nif(s.sessions&&s.sessions.length>0){\nvar rats=s.sessions[0].ratings||{};\nvar keys=Object.keys(rats);\nif(keys.length>0){\nvar weak=keys.reduce(function(a,b){return rats[a]<rats[b]?a:b;});\nkey=weak;\nfocus=skillNames[weak]||weak;\n}\n}\nif(!groups[key])groups[key]={name:focus+" Group",focus:focus,students:[],color:colors[Object.keys(groups).length%6]};\ngroups[key].students.push(s.name);\n});\nreturn Object.values(groups).map(function(g,i){return{id:i+1,name:g.name,emoji:"📚",color:g.color,students:g.students,focus:g.focus,level:"Mixed",weakSkill:g.focus};});\n}catch(e){return getDefaultGroups();}\n}\nfunction getDefaultGroups(){\nreturn[\n{id:1,name:"Group 1",emoji:"📚",color:"#FF6B6B",students:["Add students in ReadLead"],focus:"Reading Skills",level:"Mixed",weakSkill:"Fluency"}\n];\n}\nconst READLEAD_GROUPS=loadGroupsFromStorage();\n'
h=h[:i]+new+h[j:]
open('rotator.html','w').write(h)
print('done')