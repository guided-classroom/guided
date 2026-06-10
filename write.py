f=open('rotator.html','r')
h=f.read()
f.close()
i=h.find('weakSkill}')
j=h.find('.join',i)
insert_pos=j
btn='\n<button onclick="genGroupActivity(\'${g.name}\',\'${g.weakSkill}\',\'${g.students.toString()}\')" style="background:#A78BFA;color:#1A1A2E;border:none;border-radius:8px;padding:6px 14px;font-size:11px;font-weight:700;cursor:pointer;margin-top:8px">Get Activity Ideas</button>\n</div>\n</div>`'
h=h[:insert_pos]+btn+h[insert_pos:]
open('rotator.html','w').write(h)
print('done')
print('Get Activity Ideas count:',h.count('Get Activity Ideas'))