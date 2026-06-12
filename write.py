f=open('readlead.html','r')
h=f.read()
f.close()
fn='function deleteStu(id){\n'
fn+='var stu=students.find(function(s){return s.id==id;});\n'
fn+='if(!stu)return;\n'
fn+='var overlay=document.createElement("div");\n'
fn+='overlay.style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:999;display:flex;align-items:center;justify-content:center;";\n'
fn+='var box=document.createElement("div");\n'
fn+='box.style="background:#fff;border-radius:16px;padding:28px;width:320px;text-align:center;";\n'
fn+='box.innerHTML="<div style=\'font-size:18px;font-weight:700;margin-bottom:8px\'>Delete "+stu.name+"?</div><div style=\'font-size:13px;color:#888;margin-bottom:20px\'>This will permanently delete all session data for this student.</div>";\n'
fn+='var delBtn=document.createElement("button");\n'
fn+='delBtn.textContent="Yes, Delete";\n'
fn+='delBtn.style="background:#FF6B6B;color:#fff;border:none;border-radius:10px;padding:11px 20px;font-size:14px;font-weight:700;cursor:pointer;width:100%;margin-bottom:8px;";\n'
fn+='delBtn.addEventListener("click",function(){\n'
fn+='students=students.filter(function(s){return s.id!=id;});\n'
fn+='saveStudents();\n'
fn+='document.body.removeChild(overlay);\n'
fn+='rdDash();\n'
fn+='loadDashCurr();\n'
fn+='});\n'
fn+='var cancelBtn=document.createElement("button");\n'
fn+='cancelBtn.textContent="Cancel";\n'
fn+='cancelBtn.style="width:100%;padding:10px;border:none;border-radius:10px;background:#F5F3EE;font-weight:700;cursor:pointer;";\n'
fn+='cancelBtn.addEventListener("click",function(){document.body.removeChild(overlay);});\n'
fn+='box.appendChild(delBtn);\n'
fn+='box.appendChild(cancelBtn);\n'
fn+='overlay.appendChild(box);\n'
fn+='document.body.appendChild(overlay);\n'
fn+='}\n'
h=h.replace('function addStu()',fn+'function addStu()')
open('readlead.html','w').write(h)
print('done deleteStu:','function deleteStu' in h)