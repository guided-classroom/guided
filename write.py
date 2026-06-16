f=open('progress.html','r')
h=f.read()
f.close()
old='rdHome();\n</script>'
new='rdHome();\nwindow.doSignOut=async function(){localStorage.clear();window.location.href="login.html";};\n</script>'
print('found:',old in h)
h=h.replace(old,new)
open('progress.html','w').write(h)
print('done')