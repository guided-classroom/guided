h=open('rotator.html','w')
h.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>CentreRotator — Guided</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:"DM Sans",sans-serif;background:#1A1A2E;color:#fff;min-height:100vh;}
.nav{background:#12122A;padding:16px 28px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #2A2A4A;}
.logo{font-family:"Playfair Display",serif;font-size:20px;font-weight:700;color:#fff;}
.logo span{color:#6C63FF;}
.nav-links{display:flex;gap:12px;align-items:center;}
.nav-btn{background:#6C63FF;color:#fff;border:none;border-radius:8px;padding:8px 16px;font-size:13px;font-weight:700;cursor:pointer;}
.nav-btn-outline{background:transparent;color:#aaa;border:1px solid #444;border-radius:8px;padding:7px 14px;font-size:13px;cursor:pointer;}
.main{padding:28px;}
.setup-panel{background:#12122A;border-radius:20px;padding:28px;max-width:700px;margin:0 auto 28px;}
.setup-title{font-family:"Playfair Display",serif;font-size:22px;margin-bottom:20px;color:#fff;}
.setup-row{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;}
.setup-label{font-size:11px;font-weight:800;color:#6C63FF;letter-spacing:.05em;display:block;margin-bottom:6px;}
.setup-input{width:100%;padding:10px 14px;background:#1A1A2E;border:2px solid #2A2A4A;border-radius:10px;color:#fff;font-size:14px;font-family:"DM Sans",sans-serif;}
.setup-input:focus{outline:none;border-color:#6C63FF;}
.timer-row{display:flex;gap:10px;align-items:center;margin-bottom:20px;}
.timer-btn{background:#2A2A4A;color:#fff;border:none;border-radius:8px;padding:8px 16px;font-size:14px;font-weight:700;cursor:pointer;}
.timer-btn.active{background:#6C63FF;}
.start-btn{width:100%;padding:16px;background:#6C63FF;color:#fff;border:none;border-radius:12px;font-size:16px;font-weight:800;cursor:pointer;}
.display-panel{display:none;}
.centres-grid{display:grid;gap:20px;margin-bottom:28px;}
.centre-card{background:#12122A;border-radius:20px;padding:28px;border:3px solid #2A2A4A;text-align:center;transition:border-color .3s;}
.centre-card.teacher{border-color:#FFD700;background:#1A1800;}
.centre-name{font-size:22px;font-weight:800;color:#fff;margin-bottom:16px;}
.group-badge{display:inline-block;padding:10px 20px;border-radius:99px;font-size:18px;font-weight:800;margin:4px;}
.timer-display{text-align:center;margin-bottom:28px;}
.timer-number{font-family:"Playfair Display",serif;font-size:96px;font-weight:900;color:#fff;line-height:1;}
.timer-number.warning{color:#FF6B6B;}
.timer-label{font-size:16px;color:#aaa;margin-top:8px;}
.rotate-btn{display:block;width:100%;max-width:400px;margin:0 auto;padding:20px;background:#6C63FF;color:#fff;border:none;border-radius:16px;font-size:20px;font-weight:800;cursor:pointer;}
.rotate-btn:disabled{background:#2A2A4A;color:#666;cursor:not-allowed;}
.edit-btn{display:block;width:100%;max-width:400px;margin:12px auto 0;padding:12px;background:transparent;color:#aaa;border:1px solid #444;border-radius:12px;font-size:14px;cursor:pointer;}
.alert-overlay{position:fixed;inset:0;background:rgba(108,99,255,.9);display:none;align-items:center;justify-content:center;z-index:999;flex-direction:column;}
.alert-text{font-family:"Playfair Display",serif;font-size:48px;font-weight:900;color:#fff;margin-bottom:24px;text-align:center;}
.alert-btn{background:#fff;color:#6C63FF;border:none;border-radius:14px;padding:16px 40px;font-size:20px;font-weight:800;cursor:pointer;}
</style>
</head>
<body>
<nav class="nav">
  <div class="logo">Guided <span>CentreRotator</span></div>
  <div class="nav-links">
    <a href="readlead.html" class="nav-btn-outline">ReadLead</a>
    <a href="progress.html" class="nav-btn-outline">Progress</a>
    <button class="nav-btn-outline" onclick="doSignOut()">Sign Out</button>
  </div>
</nav>

<div class="main">
  <!-- SETUP PANEL -->
  <div class="setup-panel" id="setup-panel">
    <div class="setup-title">Set Up Your Centres</div>
    
    <div style="margin-bottom:20px">
      <label class="setup-label">CENTRE NAMES (one per line, up to 5)</label>
      <textarea id="centre-names" class="setup-input" rows="5" placeholder="Independent Reading&#10;Work with Teacher&#10;Word Study&#10;Tech Time&#10;Fluency Practice"></textarea>
    </div>

    <div style="margin-bottom:20px">
      <label class="setup-label">GROUP NAMES (one per line, up to 5)</label>
      <textarea id="group-names" class="setup-input" rows="5" placeholder="Group 1&#10;Group 2&#10;Group 3&#10;Group 4&#10;Group 5"></textarea>
    </div>

    <div style="margin-bottom:20px">
      <label class="setup-label">WHICH CENTRE IS "WORK WITH TEACHER"?</label>
      <input id="teacher-centre" class="setup-input" placeholder="Work with Teacher" value="Work with Teacher"/>
    </div>

    <div style="margin-bottom:20px">
      <label class="setup-label">ROTATION TIME</label>
      <div class="timer-row">
        <button class="timer-btn" onclick="setTime(10,this)">10 min</button>
        <button class="timer-btn active" onclick="setTime(15,this)">15 min</button>
        <button class="timer-btn" onclick="setTime(20,this)">20 min</button>
        <button class="timer-btn" onclick="setTime(25,this)">25 min</button>
        <button class="timer-btn" onclick="setTime(30,this)">30 min</button>
      </div>
    </div>

    <button class="start-btn" onclick="startRotator()">Start Centres ▶</button>
  </div>

  <!-- DISPLAY PANEL -->
  <div class="display-panel" id="display-panel">
    <div class="timer-display">
      <div class="timer-number" id="timer-display">15:00</div>
      <div class="timer-label">until next rotation</div>
    </div>
    <div class="centres-grid" id="centres-grid"></div>
    <button class="rotate-btn" id="rotate-btn" onclick="startTimer()" disabled>▶ Start Timer</button>
    <button class="edit-btn" onclick="showSetup()">⚙ Edit Setup</button>
  </div>
</div>

<!-- ALERT OVERLAY -->
<div class="alert-overlay" id="alert-overlay">
  <div class="alert-text">⏰ Time to Rotate!</div>
  <button class="alert-btn" onclick="doRotate()">Rotate Groups ▶</button>
</div>

<audio id="bell" src="data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAA..." preload="auto"></audio>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
<script>
var _sb=supabase.createClient("https://ynvgikozznybuuusxbhz.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inludmdpa296em55YnV1dXN4Ymh6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk4NTk2NzMsImV4cCI6MjAyNTQzNTY3M30.oCjedoInIqBkJjUb7tTGPdE5_L7yWNj6EFtQyEtxb1w");

var _centres=[];
var _groups=[];
var _rotation=[];
var _timerMinutes=15;
var _timerSeconds=0;
var _timerInterval=null;
var _teacherCentre="Work with Teacher";
var GROUP_COLORS=["#6C63FF","#FF6B9D","#4ECDC4","#FFD700","#FF8C42"];

async function init(){
  var result=await _sb.auth.getSession();
  if(!result.data.session){window.location.href="login.html";return;}
  loadSaved();
}

function loadSaved(){
  var saved=localStorage.getItem("guided_rotator_v2");
  if(saved){
    var data=JSON.parse(saved);
    _centres=data.centres||[];
    _groups=data.groups||[];
    _timerMinutes=data.minutes||15;
    _teacherCentre=data.teacherCentre||"Work with Teacher";
    _rotation=data.rotation||[];
    if(_centres.length&&_groups.length){
      document.getElementById("centre-names").value=_centres.join("\\n");
      document.getElementById("group-names").value=_groups.join("\\n");
      document.getElementById("teacher-centre").value=_teacherCentre;
      document.querySelectorAll(".timer-btn").forEach(function(btn){
        btn.classList.remove("active");
        if(btn.textContent===_timerMinutes+" min")btn.classList.add("active");
      });
    }
  }
}

function setTime(min,btn){
  _timerMinutes=min;
  document.querySelectorAll(".timer-btn").forEach(function(b){b.classList.remove("active");});
  btn.classList.add("active");
}

function startRotator(){
  var centreText=document.getElementById("centre-names").value.trim();
  var groupText=document.getElementById("group-names").value.trim();
  _teacherCentre=document.getElementById("teacher-centre").value.trim()||"Work with Teacher";
  _centres=centreText.split("\\n").map(function(s){return s.trim();}).filter(Boolean).slice(0,5);
  _groups=groupText.split("\\n").map(function(s){return s.trim();}).filter(Boolean).slice(0,5);
  if(_centres.length<2||_groups.length<2){alert("Please enter at least 2 centres and 2 groups.");return;}
  if(_rotation.length===0){
    _rotation=_groups.slice();
  }
  saveData();
  renderDisplay();
  document.getElementById("setup-panel").style.display="none";
  document.getElementById("display-panel").style.display="block";
  resetTimer();
}

function renderDisplay(){
  var grid=document.getElementById("centres-grid");
  var cols=_centres.length<=2?2:_centres.length<=4?2:3;
  grid.style.gridTemplateColumns="repeat("+cols+",1fr)";
  grid.innerHTML=_centres.map(function(centre,ci){
    var isTeacher=centre===_teacherCentre;
    var groupIdx=_rotation.indexOf(_groups[ci%_groups.length]);
    var html="<div class=\\"centre-card"+(isTeacher?" teacher":"")+"\\">";
    html+="<div class=\\"centre-name\\">"+(isTeacher?"⭐ ":"")+centre+"</div>";
    _groups.forEach(function(g,gi){
      if(_rotation[gi]===_groups[ci%_groups.length]||(ci<_groups.length&&_rotation[ci]===g)){
        // show group at this centre
      }
    });
    // Assign groups to centres
    if(ci<_groups.length){
      var g=_rotation[ci];
      var gi=_groups.indexOf(g);
      var color=GROUP_COLORS[gi%GROUP_COLORS.length];
      html+="<span class=\\"group-badge\\" style=\\"background:"+color+"\\">"+g+"</span>";
    }
    html+="</div>";
    return html;
  }).join("");
}

function resetTimer(){
  _timerSeconds=_timerMinutes*60;
  updateTimerDisplay();
  document.getElementById("rotate-btn").disabled=false;
  document.getElementById("rotate-btn").textContent="▶ Start Timer";
}

function startTimer(){
  if(_timerInterval){clearInterval(_timerInterval);_timerInterval=null;document.getElementById("rotate-btn").textContent="▶ Start Timer";return;}
  document.getElementById("rotate-btn").textContent="⏸ Pause";
  _timerInterval=setInterval(function(){
    _timerSeconds--;
    updateTimerDisplay();
    if(_timerSeconds<=0){
      clearInterval(_timerInterval);_timerInterval=null;
      showAlert();
    }
  },1000);
}

function updateTimerDisplay(){
  var m=Math.floor(_timerSeconds/60);
  var s=_timerSeconds%60;
  var str=m+":"+(s<10?"0":"")+s;
  var el=document.getElementById("timer-display");
  el.textContent=str;
  el.className="timer-number"+(m===0&&s<=30?" warning":"");
}

function showAlert(){
  document.getElementById("alert-overlay").style.display="flex";
  try{new Audio("data:audio/wav;base64,//uQRAAAAWMSLwUIYAAsYkXgoQwAEaYLWfkWgAI0wWs/ItAAAGDgYtAgAyN+QWaAAihwMWm4G8QQRDiMcCBcH3Cc+CDv/7xA4Tvh9Rz/y8QADBwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWGluZQAAAA8AAAACAAACcQCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA").play();}catch(e){}
}

function doRotate(){
  document.getElementById("alert-overlay").style.display="none";
  var last=_rotation.pop();
  _rotation.unshift(last);
  saveData();
  renderDisplay();
  resetTimer();
}

function showSetup(){
  if(_timerInterval){clearInterval(_timerInterval);_timerInterval=null;}
  document.getElementById("display-panel").style.display="none";
  document.getElementById("setup-panel").style.display="block";
}

function saveData(){
  localStorage.setItem("guided_rotator_v2",JSON.stringify({
    centres:_centres,groups:_groups,minutes:_timerMinutes,
    teacherCentre:_teacherCentre,rotation:_rotation
  }));
}

async function doSignOut(){
  await _sb.auth.signOut();
  window.location.href="login.html";
}

init();
</script>
</body>
</html>''')
h.close()
print('done')