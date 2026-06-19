f=open('progress.html','r')
h=f.read()
f.close()
old='rdHome();\nwindow.doSignOut=async function(){localStorage.clear();window.location.href="login.html";};'
new='initApp();\nwindow.doSignOut=async function(){if(_sb)await _sb.auth.signOut();window.location.href="login.html";};'
print('found:',old in h)
h=h.replace(old,new)
open('progress.html','w').write(h)
print('done')