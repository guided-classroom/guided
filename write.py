f=open('readlead.html','r')
h=f.read()
f.close()
h=h.rstrip()
h+='\n</script>\n</body>\n</html>\n'
open('readlead.html','w').write(h)
print('done')
print('last 50 chars:',repr(h[-50:]))