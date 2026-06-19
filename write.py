f=open('index.html','r')
h=f.read()
f.close()
i=h.find('hero-cta') if h.find('hero-cta')>-1 else -1
print(i)
print(h[i-50:i+300] if i>-1 else "not found")