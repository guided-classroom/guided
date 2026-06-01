f=open('progress.html','r')
h=f.read()
f.close()
old='var rStr=QR.map(function(r){var v=rats[r.id]||0;return r.l+": "+v+"%";}).join(", ");'
new='var rStr=QR.map(function(r){var v=rats[r.id]||0;var level=v>=90?"strong":v>=75?"developing well":v>=60?"developing":"working toward";return r.l+": "+level;}).join(", ");'
print('found:',old in h)
h=h.replace(old,new)
open('progress.html','w').write(h)
print('done')