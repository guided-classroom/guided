f=open('readlead.html','r')
h=f.read()
f.close()
old='function initSupabase(){\nwindow.addEventListener("sb-ready",async function(){\n_supabase=window._sbClient;\nwindow._supabase=_supabase;\nawait loadStudents();\nawait loadDashCurrFromDB();\nrdDash();\nloadDashCurr();\n});\n}'
new='function initSupabase(){\nif(window._sbClient){\n_supabase=window._sbClient;\nwindow._supabase=_supabase;\nloadStudents().then(function(){loadDashCurrFromDB().then(function(){rdDash();loadDashCurr();});});\n}else{\nwindow.addEventListener("sb-ready",function(){\n_supabase=window._sbClient;\nwindow._supabase=_supabase;\nloadStudents().then(function(){loadDashCurrFromDB().then(function(){rdDash();loadDashCurr();});});\n});\n}\n}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')