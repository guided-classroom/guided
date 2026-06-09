f=open('readlead.html','r')
h=f.read()
f.close()
while h.count('</body>')>1:
    i=h.find('</body>')
    h=h[:i]+h[i+7:]
while h.count('</html>')>1:
    i=h.find('</html>')
    h=h[:i]+h[i+7:]
while h.count('</script>')>1:
    i=h.find('</script>')
    h=h[:i]+h[i+9:]
open('readlead.html','w').write(h)
print('done')
print('</body>:',h.count('</body>'))
print('</html>:',h.count('</html>'))
print('</script>:',h.count('</script>'))