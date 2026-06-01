f=open('readlead.html','r')
h=f.read()
f.close()
fn='function editLevel(id){\n'
fn+='var stu=students.find(function(s){return s.id==id;});\n'
fn+='if(!stu)return;\n'
fn+='var newLevel=prompt("Current level: "+stu.level+"\\nEnter new level (e.g. Level 5):");\n'
fn+='if(!newLevel)return;\n'
fn+='newLevel=newLevel.trim();\n'
fn+='if(!LM[newLevel]){alert("Invalid level. Please use format: Level 1 through Level 21");return;}\n'
fn+='var idx=students.findIndex(function(s){return s.id==id;});\n'
fn+='students[idx].level=newLevel;\n'
fn+='students[idx].grade=LM[newLevel][0];\n'
fn+='saveStudents();\n'
fn+='rdDash();\n'
fn+='loadDashCurr();\n'
fn+='}\n'
h=h.replace('function addStu(){\n',fn+'function addStu(){\n')
open('readlead.html','w').write(h)
print('done editLevel:','function editLevel' in h)