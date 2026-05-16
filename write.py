f=open('readlead.html','r')
h=f.read()
f.close()
old='try{les=JSON.parse(text);}catch(e){try{les=JSON.parse(text.replace(/```json/gi,"").replace(/```/g,"").trim());}catch(e2){var a=text.indexOf("{"),b=text.lastIndexOf("}");les=JSON.parse(text.slice(a,b+1));}}'
new='try{les=JSON.parse(text);}catch(e){try{var clean=text.replace(/```json/gi,"").replace(/```/g,"").trim();les=JSON.parse(clean);}catch(e2){try{var a=text.indexOf("{"),b=text.lastIndexOf("}");les=JSON.parse(text.slice(a,b+1));}catch(e3){les={lessonTitle:"Lesson Plan",focusSummary:"Generated lesson",hasCurriculumAlignment:false,segments:[{pillar:"phonics",title:"Phonics Practice",timeRange:"0-5 min",minutes:5,emphasis:true,teacherDoes:"Work on phonics skills",studentDoes:"Practice with teacher",materials:"Whiteboard",tip:"Focus on target sounds",standard:""},{pillar:"fluency",title:"Fluency Building",timeRange:"5-10 min",minutes:5,emphasis:true,teacherDoes:"Model fluent reading",studentDoes:"Echo read",materials:"Levelled text",tip:"Focus on expression",standard:""},{pillar:"comprehension",title:"Comprehension Check",timeRange:"10-15 min",minutes:5,emphasis:false,teacherDoes:"Ask questions",studentDoes:"Retell the story",materials:"Reading passage",tip:"Use questioning strategies",standard:""}],afterLesson:"Continue practising these skills daily."};}}}' 
print('old found:',old in h)
h=h.replace(old,new)
open('readlead.html','w').write(h)
print('done')