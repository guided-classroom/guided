f=open('progress.html','r')
h=f.read()
f.close()
old='prompt+="Reading Level: "+cur.level+"\\n";\n'
print('found:',old in h)
h=h.replace(old,'')
open('progress.html','w').write(h)
print('done')