f=open('readlead.html','r')
h=f.read()
f.close()
fn='function rdPass(){\n'
fn+='var ps=PASSAGES[cur.level]||PASSAGES["Level 5"]||[];\n'
fn+='if(!ps.length)return;\n'
fn+='var p=ps[pidx%ps.length];\n'
fn+='var lv=lc(cur.level);\n'
fn+='document.getElementById("p-tabs").innerHTML=ps.map(function(x,i){return"<button onclick=\'selP("+i+")\' style=\'background:"+(pidx===i?lv:"#F5F3EE")+";color:"+(pidx===i?"#fff":"#777")+";border:none;border-radius:6px;padding:4px 10px;font-size:11px;font-weight:600;cursor:pointer\'>"+x.title+"</button>";}).join("");\n'
fn+='document.getElementById("p-text").textContent=p.text;\n'
fn+='document.getElementById("p-qs").innerHTML=p.qs.map(function(q,i){return"<div style=\'font-size:12px;color:#666;margin-bottom:4px;display:flex;gap:6px\'><span style=\'font-weight:700;color:"+lv+";flex-shrink:0\'>"+(i+1)+".</span><span>"+q+"</span></div>";}).join("");\n'
fn+='}\n'
fn+='function selP(i){pidx=i;rdPass();}\n'
fn+='function addErr(){\n'
fn+='var w=document.getElementById("w-in").value.trim();if(!w)return;\n'
fn+='errs.push({word:w,said:document.getElementById("s-in").value.trim(),type:document.getElementById("t-in").value});\n'
fn+='document.getElementById("w-in").value="";\n'
fn+='document.getElementById("s-in").value="";\n'
fn+='rdErrs();\n'
fn+='}\n'
fn+='function rmErr(i){errs.splice(i,1);rdErrs();}\n'
h=h.replace('async function doGen()',fn+'async function doGen()')
open('readlead.html','w').write(h)
print('done rdPass:','function rdPass' in h,'addErr:','function addErr' in h)