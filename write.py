f=open('readlead.html','r')
h=f.read()
f.close()
h=h.replace(
'fetch("https://api.anthropic.com/v1/messages",{method:"POST",headers:{"content-type":"application/json","anthropic-dangerous-direct-browser-access":"true"}',
'fetch("/api/lesson",{method:"POST",headers:{"content-type":"application/json"}'
)
open('readlead.html','w').write(h)
print('done count:',h.count('/api/lesson'))