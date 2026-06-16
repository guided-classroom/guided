f=open('readlead.html','r')
h=f.read()
f.close()
old='function saveDashCurr(){\nvar joined=dashCurrItems.filter(function(v){return v.trim().length>0;}).join("\\n");\ntry{localStorage.setItem("guided_curriculum",joined);}catch(e){}'
new='async function saveDashCurr(){\nvar joined=dashCurrItems.filter(function(v){return v.trim().length>0;}).join("\\n");\ntry{localStorage.setItem("guided_curriculum",joined);}catch(e){}\ntry{\nif(window._user){\nawait _supabase.from("curriculum").upsert({user_id:window._user.id,content:joined,updated_at:new Date().toISOString()},{onConflict:"user_id"});\n}\n}catch(e){console.error("curriculum save error",e);}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')