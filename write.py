f=open('readlead.html','r')
h=f.read()
f.close()
old='var students=[];\nvar _supabase=null;\nasync function initSupabase(){\nvar mod=await import("https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm");\n_supabase=mod.createClient("https://ynvgikozznybuuusxbhz.supabase.co","sb_publishable_tt1xUdoOfZ0Pf8rXuMxyqw_hRfCzxeZ");\nwindow._supabase=_supabase;\nvar {data:sess}=await _supabase.auth.getSession();\nif(!sess.session){window.location.href="login.html";return;}\nwindow._user=sess.session.user;\nawait loadStudents();\nawait loadDashCurrFromDB();\nrdDash();\nloadDashCurr();\n}'
new='var students=[];\nvar _supabase=null;\nfunction initSupabase(){\nwindow.addEventListener("sb-ready",async function(){\n_supabase=window._sbClient;\nwindow._supabase=_supabase;\nawait loadStudents();\nawait loadDashCurrFromDB();\nrdDash();\nloadDashCurr();\n});\n}'
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')