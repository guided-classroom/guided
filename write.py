f=open('rotator.html','r')
h=f.read()
f.close()
i=h.find('const ALL_CENTRES')
j=h.find('];',i)
old=h[i:j+2]
new='const ALL_CENTRES = [\n{id:"teacher",name:"Teacher Table",emoji:"T"},\n{id:"tech",name:"Tech Station",emoji:"⌨"},\n{id:"word",name:"Word Work",emoji:"W"},\n{id:"read",name:"Read to Self",emoji:"R"},\n{id:"listen",name:"Listen to Reading",emoji:"♪"},\n{id:"writing",name:"Writing Station",emoji:"✍"}\n];'
h=h[:i]+new+h[j+2:]
open('rotator.html','w').write(h)
print('done')