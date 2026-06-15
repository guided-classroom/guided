f=open('readlead.html','r')
h=f.read()
f.close()
old='populateLvl();\nrdDash();'
new='populateLvl();\nrdDash();\nwindow.doSignOut=async function(){\nvar sb=window._supabase;\nif(sb)await sb.auth.signOut();\nlocalStorage.clear();\nwindow.location.href="login.html";\n}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')