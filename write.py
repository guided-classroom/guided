f=open('progress.html','r')
h=f.read()
f.close()
old='var currList=[];\nif(curriculum){\nvar lines=curriculum.split("\\n").map(function(l){return l.trim();}).filter(function(l){return l.length>10;});\ncurrList=lines.slice(0,10);\n}\nvar allOutcomes=currList.length?currList.concat(defaults):defaults;\noutcomes=allOutcomes.map(function(o){return{text:o,status:"none"};});\nrenderOutcomes();'
new='var currList=[];\nif(curriculum){\nvar lines=curriculum.split("\\n").map(function(l){return l.trim();}).filter(function(l){return l.length>15;});\ncurrList=lines.slice(0,12);\n}\nvar allOutcomes=currList.length?currList:defaults;\noutcomes=allOutcomes.map(function(o){return{text:o,status:"none"};});\nrenderOutcomes();'
print('found:',old in h)
h=h.replace(old,new)
open('progress.html','w').write(h)
print('done')