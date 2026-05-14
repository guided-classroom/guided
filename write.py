f=open('readlead.html','r')
h=f.read()
f.close()
old='fetch("https://api.anthropic.com/v1/messages"'
new='fetch("/api/lesson"'
count=h.count(old)
print('replacing',count,'occurrences')
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done /api/lesson count:',h.count('/api/lesson'))