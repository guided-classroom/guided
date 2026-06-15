f=open('rotator.html','r')
h=f.read()
f.close()
old='box.innerHTML=acts.map(function(a){return"<div style=\'margin-bottom:10px;border-bottom:1px solid #333;padding-bottom:10px\'><div style=\'font-size:12px;font-weight:700;color:#A78BFA;margin-bottom:4px\'>"+a.title+"</div><div style=\'font-size:12px;color:#CCC;margin-bottom:4px\'>"+a.description+"</div><div style=\'font-size:11px;color:#888\'>Materials: "+a.materials+"</div></div>";}).join("");\nbtn.parentNo'
new='var closeBtn="<button onclick=\'this.parentNode.remove()\' style=\'float:right;background:none;border:1px solid #555;color:#AAA;border-radius:6px;padding:2px 8px;font-size:11px;cursor:pointer;margin-bottom:8px\'>Close x</button>";\nbox.innerHTML=closeBtn+"<div style=\'clear:both;display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px\'>"+acts.map(function(a){return"<div style=\'background:#2A3A4A;border-radius:8px;padding:10px\'><div style=\'font-size:12px;font-weight:700;color:#A78BFA;margin-bottom:4px\'>"+a.title+"</div><div style=\'font-size:11px;color:#CCC;margin-bottom:6px;line-height:1.4\'>"+a.description+"</div><div style=\'font-size:10px;color:#888;border-top:1px solid #444;padding-top:4px\'>"+a.materials+"</div></div>";}).join("")+"</div>";\nbtn.parentNo'
print('found:',old in h)
h=h.replace(old,new)
open('rotator.html','w').write(h)
print('done')