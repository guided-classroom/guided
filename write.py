f=open('progress.html','r')
h=f.read()
f.close()
old='function setStatus(i,status){\noutcomes[i].status=outcomes[i].status===status?"none":status;\nrenderOutcomes();\n}'
new='var statusMap=["strength","developing","support"];\nfunction setStatus(i,s){\nvar status=statusMap[s];\noutcomes[i].status=outcomes[i].status===status?"none":status;\nrenderOutcomes();\n}'
print('found:',old in h)
h=h.replace(old,new)
open('progress.html','w').write(h)
print('done')