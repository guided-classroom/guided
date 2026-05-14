f=open('readlead.html','r')
h=f.read()
f.close()
old='var text=(data.content||[]).filter(function(b){return b.type==="text";}).map(function(b){return b.text;}).join("").trim();'
new='var text=(data.content||[]).filter(function(b){return b.type==="text";}).map(function(b){return b.text;}).join("").trim();console.log("API response:",JSON.stringify(data).substring(0,200));console.log("text:",text.substring(0,200));'
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')