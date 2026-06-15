f=open('rotator.html','r')
h=f.read()
f.close()
old='const ALL_CENTRES = [\n{id:"teacher",name:"Teacher Table",emoji:"T"},\n{id:"tech",name:"Tech Station",emoji:"⌨"},\n{id:"word",name:"Word Work",emoji:"W"},\n{id:"read",name:"Read to Self",emoji:"R"},\n{id:"listen",name:"Listen to Reading",emoji:"♪"},\n{id:"writing",name:"Writing Station",emoji:"✍"}\n];'
new='const ALL_CENTRES = [\n{id:"teacher",name:"Teacher Table",emoji:"👥"},\n{id:"tech",name:"Tech Station",emoji:"🖥"},\n{id:"word",name:"Word Work",emoji:"🔤"},\n{id:"read",name:"Read to Self",emoji:"📖"},\n{id:"listen",name:"Listen to Reading",emoji:"🎵"},\n{id:"writing",name:"Writing Station",emoji:"📝"}\n];'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')