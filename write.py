
f=open('rotator.html','r')
h=f.read()
f.close()
old='<script>\n'
new='<script type="module">\nimport { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm";\nconst supabase = createClient("https://ynvgikozznybuuusxbhz.supabase.co","sb_publishable_tt1xUdoOfZ0Pf8rXuMxyqw_hRfCzxeZ");\nconst { data: { session } } = await supabase.auth.getSession();\nif(!session) window.location.href="login.html";\nconst user = session.user;\n</script>\n<script>\n'
print('found:',old in h)
h=h.replace(old,new,1)
open('rotator.html','w').write(h)
print('done')