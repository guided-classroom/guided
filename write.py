f=open('readlead.html','r')
h=f.read()
f.close()
old='var newLevel=prompt("Current level: "+stu.level+"\\nEnter new level (e.g. Level 5):");\nif(!newLevel)return;\nnewLevel=newLevel.trim();\nif(!LM[newLevel]){alert("Invalid level. Please use format: Level 1 through Level 21");return;}'
new='var options=Object.keys(LM).map(function(l){return l+" ("+LM[l][0]+")";}).join("\\n");\nvar newLevel=prompt("Current: "+stu.level+" ("+LM[stu.level][0]+")\\n\\nChoose a new level:\\n"+options);\nif(!newLevel)return;\nnewLevel=newLevel.trim();\nif(newLevel.indexOf("(")<0&&!LM[newLevel]){\nnewLevel="Level "+newLevel.replace(/[^0-9]/g,"");\n}\nif(newLevel.indexOf("(")>0)newLevel=newLevel.split("(")[0].trim();\nif(!LM[newLevel]){alert("Invalid. Please type exactly e.g. Level 5");return;}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')