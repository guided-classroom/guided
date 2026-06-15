f=open('index.html','r')
h=f.read()
f.close()

# Replace ReadLead emoji with SVG book icon
old1='background:rgba(78,205,196,0.12);border:1px solid rgba(78,205,196,0.25);">📖</d'
new1='background:rgba(78,205,196,0.12);border:1px solid rgba(78,205,196,0.25);"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4ECDC4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></d'

# Replace CentreRotator emoji with SVG rotate icon
old2='background:rgba(255,209,102,0.12);border:1px solid rgba(255,209,102,0.25);">🔄</d'
new2='background:rgba(167,139,250,0.12);border:1px solid rgba(167,139,250,0.25);"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg></d'

# Make logo bigger
old3='.logo-icon{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,#4ECDC4,#A78BFA);display:flex;align-items:center;justify-content:center;font-size:16px;}'
new3='.logo-icon{width:42px;height:42px;border-radius:11px;background:linear-gradient(135deg,#4ECDC4,#A78BFA);display:flex;align-items:center;justify-content:center;font-size:20px;}'

old4='.logo-text{font-family:\'Playfair Display\',serif;font-size:20px;font-weight:9'
new4='.logo-text{font-family:\'Playfair Display\',serif;font-size:24px;font-weight:9'

print('ReadLead icon found:',old1 in h)
print('Rotator icon found:',old2 in h)
print('Logo size found:',old3 in h)
h=h.replace(old1,new1)
h=h.replace(old2,new2)
h=h.replace(old3,new3)
h=h.replace(old4,new4)
open('index.html','w').write(h)
print('done')