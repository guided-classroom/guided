f=open('readlead.html','r')
h=f.read()
f.close()
h=h.replace(
'headers:{"content-type":"application/json","anthropic-dangerous-direct-browser-access":"true"}',
'headers:{"content-type":"application/json","anthropic-dangerous-direct-browser-access":"true","x-api-key":"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"}'
)
open('readlead.html','w').write(h)
print('done count:',h.count('x-api-key'))