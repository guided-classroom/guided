f=open('readlead.html','r')
h=f.read()
f.close()
i=h.find('function printP()')
j=h.find('function selP')
fn="function printP(){"
fn+="var ps=PASSAGES[cur.level]||PASSAGES['Level 5']||[];"
fn+="var p=ps[pidx%ps.length];"
fn+="var w=window.open();"
fn+="w.document.write('<html><body style=\"font-family:Georgia,serif;max-width:600px;margin:40px auto\"><h1>'+p.title+'</h1><div style=\"white-space:pre-line;font-size:16px;line-height:2.2\">'+p.text+'</div></body></html>');"
fn+="w.document.close();"
fn+="w.print();"
fn+="}\n"
h=h[:i]+fn+h[j:]
open('readlead.html','w').write(h)
print('done')