f=open('rotator.html','r')
h=f.read()
f.close()
i=h.find('function loadGroupsFromStorage')
j=h.find('function getDefaultGroups')
fn=''
fn+='function loadGroupsFromStorage(){\n'
fn+='try{\n'
fn+='var raw=localStorage.getItem("guided_students");\n'
fn+='if(!raw)return getDefaultGroups();\n'
fn+='var students=JSON.parse(raw);\n'
fn+='if(!students.length)return getDefaultGroups();\n'
fn+='var colors=["#FF6B6B","#FFD166","#4ECDC4","#6BCB77","#A78BFA","#FF9F43"];\n'
fn+='var skillNames={accuracy:"Accuracy",fluency:"Fluency",decoding:"Decoding",selfmon:"Self-Monitoring",comprehension:"Comprehension"};\n'
fn+='var groups={};\n'
fn+='students.forEach(function(s){\n'
fn+='var key="no-data";var focus="No Session Data";\n'
fn+='if(s.sessions&&s.sessions.length>0){\n'
fn+='var rats=s.sessions[0].ratings||{};\n'
fn+='var keys=Object.keys(rats);\n'
fn+='if(keys.length>0){\n'
fn+='var weak=keys.reduce(function(a,b){return rats[a]<rats[b]?a:b;});\n'
fn+='key=weak;focus=skillNames[weak]||weak;\n'
fn+='}\n'
fn+='}\n'
fn+='if(!groups[key])groups[key]={name:focus+" Group",focus:focus,students:[],color:colors[Object.keys(groups).length%6]};\n'
fn+='groups[key].students.push(s.name+" ("+s.level+")");\n'
fn+='});\n'
fn+='var result=Object.values(groups).map(function(g,gi){return{id:gi+1,name:g.name,emoji:"📚",color:g.color,students:g.students,focus:g.focus,level:"Mixed",weakSkill:g.focus};});\n'
fn+='if(result.length===1&&result[0].focus==="No Session Data")return getDefaultGroups();\n'
fn+='return result;\n'
fn+='}catch(e){return getDefaultGroups();}\n'
fn+='}\n'
h=h[:i]+fn+h[j:]
open('rotator.html','w').write(h)
print('done')