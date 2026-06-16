f=open('readlead.html','r')
h=f.read()
f.close()
old='function initSupabase(){\nif(window._sbClient){\n_supabase=window._sbClient;\nwindow._supabase=_supabase;\nloadStudents().then(function(){loadDashCurrFromDB().then(function(){rdDash();loadDashCurr();});});\n}else{\nwindow.addEventListener("sb-ready",function(){\n_supabase=window._sbClient;\nwindow._supabase=_supabase;\nloadStudents().then(function(){loadDashCurrFromDB().then(function(){rdDash();loadDashCurr();});});\n});\n}\n}'
new='function initSupabase(){\n_supabase=supabase.createClient("https://ynvgikozznybuuusxbhz.supabase.co","sb_publishable_tt1xUdoOfZ0Pf8rXuMxyqw_hRfCzxeZ");\nwindow._supabase=_supabase;\n_supabase.auth.getSession().then(function(result){\nvar session=result.data.session;\nif(!session){window.location.href="login.html";return;}\nwindow._user=session.user;\nloadStudents().then(function(){loadDashCurrFromDB().then(function(){rdDash();loadDashCurr();});});\n});\n}'
print('found:',old in h)
h=h.replace(old,new)