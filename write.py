f=open('readlead.html','r')
h=f.read()
f.close()
old="w.document.write(\"<html><body style='font-family:Georgia,serif;max-width:600px;margin:40px auto'><h1>\"+p.title+\"</h1><div style='white-space:pre-line;font-size:16px;line-height:2.2;margin-bottom:20px'>\"+p.text+\"</div>\""
new="w.document.write(\"<html><body style='font-family:Georgia,serif;max-width:700px;margin:40px auto'><h1 style='font-size:32px'>\"+p.title+\"</h1><div style='white-space:pre-line;font-size:24px;line-height:2.4;margin-bottom:30px'>\"+p.text+\"</div>\""
print('found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')