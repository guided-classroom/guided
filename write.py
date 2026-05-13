f=open('readlead.html','r')
h=f.read()
f.close()
insert='function rdErrs(){\n'
insert+='var el=document.getElementById("err-list");\n'
insert+='if(!errs.length){el.innerHTML="<div style=\'font-size:12px;color:#CCC\'>No errors logged yet</div>";return;}\n'
insert+='el.innerHTML=errs.map(function(e,i){return"<div class=\'erow\'><div class=\'row\'>"+tag(e.type,"#FF9F43")+"<span style=\'font-size:12px;font-weight:700\'>"+e.word+"</span>"+(e.said?"<span style=\'font-size:12px;color:#888\'>said "+e.said+"</span>":"")+"</div><button style=\'background:none;border:none;color:#CCC;cursor:pointer;font-size:18px\' onclick=\'rmErr("+i+")\'>x</button></div>";}).join("");\n'
insert+='}\n'
insert+='function rmErr(i){errs.splice(i,1);rdErrs();}\n'
h=h.replace('function rdRats()',insert+'function rdRats()')
open('readlead.html','w').write(h)
print('done rdErrs:','function rdErrs' in h)