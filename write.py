f=open('rotator.html','r')
h=f.read()
f.close()
old='}</div>\n</div>\n</div>`)\n<button onclick="genGroupActivity(\'${g.name}\',\'${g.weakSkill}\',\'${g.students.toString()}\')" style="background:#A78BFA;color:#1A1A2E;border:none;border-radius:8px;padding:6px 14px;font-size:11px;font-weight:700;cursor:pointer;margin-top:8px">Get Activity Ideas</button>\n</div>\n</div>`.join'
new='}<br><button onclick="genGroupActivity(\'${g.name}\',\'${g.weakSkill}\',\'${g.students.toString()}\')" style="background:#A78BFA;color:#1A1A2E;border:none;border-radius:8px;padding:6px 14px;font-size:11px;font-weight:700;cursor:pointer;margin-top:6px">Get Activity Ideas</button></div>\n</div>\n</div>`.join'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')