f=open('rotator.html','r')
h=f.read()
f.close()
fn='async function genGroupActivity(name,skill,students){\n'
fn+='var btn=event.target;\n'
fn+='btn.textContent="Generating...";\n'
fn+='btn.disabled=true;\n'
fn+='var prompt="You are a reading teacher. Generate 3 specific literacy centre activities for a small group.\\n";\n'
fn+='prompt+="Group focus: "+skill+"\\n";\n'
fn+='prompt+="Students: "+students+"\\n";\n'
fn+='prompt+="Each activity should be hands-on, specific, and target "+skill+".\\n";\n'
fn+='prompt+="Reply ONLY with raw JSON: {\\"activities\\":[{\\"title\\":\\"...\\",\\"description\\":\\"...\\",\\"materials\\":\\"...\\"},{\\"title\\":\\"...\\",\\"description\\":\\"...\\",\\"materials\\":\\"...\\"},{\\"title\\":\\"...\\",\\"description\\":\\"...\\",\\"materials\\":\\"...\\"}]}";\n'
fn+='try{\n'
fn+='var res=await fetch("/api/lesson",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({model:"claude-sonnet-4-5",max_tokens:1000,messages:[{role:"user",content:prompt}]})});\n'
fn+='var data=await res.json();\n'
fn+='var text=(data.content||[]).filter(function(b){return b.type==="text";}).map(function(b){return b.text;}).join("").trim();\n'
fn+='var parsed;\n'
fn+='try{parsed=JSON.parse(text);}catch(e){var a=text.indexOf("{"),b=text.lastIndexOf("}");parsed=JSON.parse(text.slice(a,b+1));}\n'
fn+='var acts=parsed.activities||[];\n'
fn+='var box=document.createElement("div");\n'
fn+='box.style="margin-top:10px;background:#1A1A2E;border-radius:10px;padding:14px";\n'
fn+='box.innerHTML=acts.map(function(a){return"<div style=\'margin-bottom:10px;border-bottom:1px solid #333;padding-bottom:10px\'><div style=\'font-size:12px;font-weight:700;color:#A78BFA;margin-bottom:4px\'>"+a.title+"</div><div style=\'font-size:12px;color:#CCC;margin-bottom:4px\'>"+a.description+"</div><div style=\'font-size:11px;color:#888\'>Materials: "+a.materials+"</div></div>";}).join("");\n'
fn+='btn.parentNode.appendChild(box);\n'
fn+='btn.textContent="Get Activity Ideas";\n'
fn+='btn.disabled=false;\n'
fn+='}catch(e){\n'
fn+='btn.textContent="Error - Try Again";\n'
fn+='btn.disabled=false;\n'
fn+='}\n'
fn+='}\n'
h=h.replace('function addActivityButtons()',fn+'function addActivityButtons()')
open('rotator.html','w').write(h)
print('done genGroupActivity:','function genGroupActivity' in h)