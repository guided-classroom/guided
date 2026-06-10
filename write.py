f=open('rotator.html','r')
h=f.read()
f.close()
lines=h.split('\n')
lines[365]=lines[365].split('<br><button')[0]+'</div>'
h='\n'.join(lines)
open('rotator.html','w').write(h)
print('done')
print('Get Activity:',h.count('Get Activity'))
