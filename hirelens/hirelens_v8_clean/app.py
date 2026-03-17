
def render_scores(r):
    if not st.session_state.get("_fx_injected"):
        st.session_state["_fx_injected"] = True
        st.markdown("""
        <script>
        (function(){
          if(document.getElementById('hl-fx')) return;
          var m=document.createElement('div'); m.id='hl-fx'; document.body.appendChild(m);
          var colors=['rgba(0,255,178,.6)','rgba(61,155,255,.5)','rgba(255,184,48,.45)',
                      'rgba(157,127,255,.45)','rgba(0,229,255,.5)','rgba(255,61,107,.4)'];
          for(var i=0;i<28;i++){
            var p=document.createElement('div'); p.className='hl-particle';
            var sz=(Math.random()*2.4+.8).toFixed(1);
            var col=colors[i%colors.length];
            var op=(Math.random()*.28+.07).toFixed(2);
            var dur=(Math.random()*24+12).toFixed(1)+'s';
            var del=-(Math.random()*22).toFixed(1)+'s';
            var dx=((Math.random()-.5)*160).toFixed(0)+'px';
            p.style.cssText='width:'+sz+'px;height:'+sz+'px;background:'+col+
              ';left:'+(Math.random()*100).toFixed(1)+'%;bottom:-10px'+
              ';--op:'+op+';--dur:'+dur+';--del:'+del+';--dx:'+dx+
              ';box-shadow:0 0 '+(parseFloat(sz)*4)+'px '+col;
            document.body.appendChild(p);
          }
        })();
        </script>
        """, unsafe_allow_html=True)

    SCORE_DATA = [
        ("Overall",    r.get("coordinator",{}).get("overall_score",0),    "Weighted",   "#00FFB2",
         "M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"),
        ("ATS Score",  r.get("ats",{}).get("ats_score",0),                "Compliance", "#3D9BFF",
         "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"),
        ("Skills",     r.get("skills",{}).get("match_score",0),           "Gap Match",  "#A78BFA",
         "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"),
        ("Experience", r.get("experience",{}).get("experience_score",0),  "Relevance",  "#F5A623",
         "M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"),
        ("HM Gut",     r.get("hiring_manager",{}).get("gut_score",0),     "Hiring Mgr", "#22D3EE",
         "M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"),
    ]

    cols = st.columns(5, gap="small")
    for col, (label, score, sub, accent, icon_d) in zip(cols, SCORE_DATA):
        grade  = "A" if score>=85 else "B" if score>=70 else "C" if score>=55 else "D" if score>=40 else "F"
        gc     = "#00FFB2" if grade in ("A","B") else "#FFB830" if grade=="C" else "#FF3D6B"
        r_val  = 34; circum = round(2*3.14159*r_val); offset = round(circum*(1-score/100))
        with col:
            st.markdown(f"""
            <div class="scale-in" style="
                 background:linear-gradient(145deg,rgba(255,255,255,.04),rgba(255,255,255,.015));
                 border:1px solid rgba(255,255,255,.07);border-radius:20px;
                 padding:20px 12px 16px;text-align:center;position:relative;overflow:hidden;
                 cursor:default;transition:all .25s cubic-bezier(.4,0,.2,1);"
                 onmouseenter="this.style.transform='translateY(-5px) scale(1.02)';this.style.boxShadow='0 16px 40px rgba(0,0,0,.5),0 0 30px {accent}22';this.style.borderColor='{accent}44';"
                 onmouseleave="this.style.transform='';this.style.boxShadow='';this.style.borderColor='';">
              <div style="position:absolute;top:0;left:0;right:0;height:2px;
                          background:linear-gradient(90deg,transparent,{accent},transparent);
                          box-shadow:0 0 12px {accent};"></div>
              <div style="position:absolute;top:-20px;left:50%;transform:translateX(-50%);
                          width:80px;height:80px;border-radius:50%;
                          background:radial-gradient(circle,{accent}10 0%,transparent 70%);
                          pointer-events:none;"></div>
              <div style="width:28px;height:28px;margin:0 auto 8px;
                          background:{accent}18;border:1px solid {accent}33;border-radius:8px;
                          display:flex;align-items:center;justify-content:center;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
                     stroke="{accent}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="{icon_d}"/>
                </svg>
              </div>
              <div style="font-family:'JetBrains Mono',monospace;font-size:8px;
                          text-transform:uppercase;letter-spacing:2px;
                          color:var(--muted);margin-bottom:12px;">{label}</div>
              <div style="position:relative;width:80px;height:80px;margin:0 auto 10px;">
                <svg viewBox="0 0 80 80" width="80" height="80" style="transform:rotate(-90deg)">
                  <circle cx="40" cy="40" r="{r_val}" fill="none"
                          stroke="rgba(255,255,255,.05)" stroke-width="6"/>
                  <circle cx="40" cy="40" r="{r_val}" fill="none" stroke="{accent}" stroke-width="6"
                          stroke-dasharray="{circum}" stroke-dashoffset="{offset}" stroke-linecap="round"
                          style="transition:stroke-dashoffset 1.2s cubic-bezier(.4,0,.2,1);
                                 filter:drop-shadow(0 0 6px {accent})"/>
                </svg>
                <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
                  <div data-score="{score}" style="font-family:'Sora',sans-serif;font-size:24px;
                       font-weight:800;color:{accent};line-height:1;
                       text-shadow:0 0 20px {accent}80;">0</div>
                </div>
              </div>
              <div style="font-family:'JetBrains Mono',monospace;font-size:8.5px;
                          color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">{sub}</div>
              <div style="background:rgba(255,255,255,.04);border-radius:3px;height:3px;margin:0 6px 8px;">
                <div style="width:{score}%;height:100%;background:linear-gradient(90deg,{accent}88,{accent});
                            border-radius:3px;transition:width 1.2s ease;box-shadow:0 0 6px {accent}66;"></div>
              </div>
              <div style="display:inline-flex;align-items:center;justify-content:center;
                          width:22px;height:22px;border-radius:6px;
                          background:{accent}18;border:1px solid {accent}44;
                          font-family:'Sora',sans-serif;font-size:11px;font-weight:800;
                          color:{gc};">{grade}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <script>
    (function(){
      setTimeout(function(){
        document.querySelectorAll('[data-score]').forEach(function(el){
          var target=parseInt(el.getAttribute('data-score'));
          if(isNaN(target)) return;
          var dur=900, startT=null;
          (function step(t){
            if(!startT) startT=t;
            var p=Math.min((t-startT)/dur,1);
            el.textContent=Math.round((1-Math.pow(1-p,3))*target);
            if(p<1) requestAnimationFrame(step);
          })(performance.now());
        });
      }, 200);
    })();
    </script>
    """, unsafe_allow_html=True)
"""
HireLens AI — Multi-Agent Job Rejection Analyzer
Run: streamlit run app.py
"""

import os
import json
import time
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="HireLens AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════
# SAFE IMPORTS
# ══════════════════════════════════════════════════════
_errs = []

try:
    import plotly.graph_objects as go
    import pandas as pd
    CHARTS = True
except Exception as e:
    CHARTS = False; _errs.append(f"plotly: {e}")

try:
    from utils.pdf_parser import extract_text_from_pdf
except Exception:
    def extract_text_from_pdf(f): return ""

try:
    from utils.report_generator import generate_pdf_report
except Exception:
    def generate_pdf_report(*a, **k): return b""  # noqa: E731

try:
    from analytics.mock_data import MOCK_RESULT
    HAS_MOCK = True
except Exception as e:
    HAS_MOCK = False; MOCK_RESULT = {}; _errs.append(f"mock: {e}")

try:
    from analytics.section_scorer import compute_all_section_scores
    HAS_SECTION_SCORER = True
except Exception:
    HAS_SECTION_SCORER = False

try:
    from analytics.recruiter_simulator import simulate_recruiter_decision
    HAS_RECRUITER = True
except Exception:
    HAS_RECRUITER = False

try:
    from analytics.comparison import run_comparison
    HAS_COMPARISON = True
except Exception:
    HAS_COMPARISON = False

try:
    from analytics.interview_predictor import predict_interview_questions
    HAS_INTERVIEW = True
except Exception:
    HAS_INTERVIEW = False

try:
    from analytics.cover_letter import generate_cover_letter
    HAS_COVER_LETTER = True
except Exception:
    HAS_COVER_LETTER = False

try:
    from analytics.bullet_improver import improve_bullets, extract_bullets_from_result
    HAS_BULLET_IMPROVER = True
except Exception:
    HAS_BULLET_IMPROVER = False

# ══════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600&display=swap');

:root {
  --bg:#030508; --bg2:#070B12; --bg3:#0A1018; --bg4:#0E1520;
  --b1:rgba(255,255,255,.06); --b2:rgba(255,255,255,.10); --b3:rgba(255,255,255,.16);
  --emerald:#00FFB2; --emerald2:#00D48F;
  --sapphire:#3D9BFF; --amber:#FFB830; --crimson:#FF3D6B;
  --violet:#9D7FFF; --cyan:#00E5FF;
  --text:#F0F4FF; --dim:#8898B4; --muted:#3D5270;
  --r-sm:8px; --r-md:12px; --r-lg:18px;
  /* backward compat aliases */
  --green:var(--emerald); --green2:var(--emerald2); --red:var(--crimson);
  --blue:var(--sapphire); --border:var(--b1); --border2:var(--b2);
}

html,body,.stApp{background:var(--bg)!important;color:var(--text)!important;font-family:'Inter',sans-serif!important;}
#MainMenu,footer,header{visibility:hidden!important;}
.block-container{padding:1rem 2.5rem 6rem!important;max-width:1520px!important;}

.stApp::before{
  content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 80% 50% at 0% 0%,   rgba(0,255,178,.06) 0%,transparent 60%),
    radial-gradient(ellipse 60% 45% at 100% 100%,rgba(61,155,255,.06) 0%,transparent 60%),
    radial-gradient(ellipse 50% 40% at 50% -5%,  rgba(157,127,255,.04) 0%,transparent 60%),
    radial-gradient(ellipse 35% 30% at 80% 30%,  rgba(0,229,255,.03)  0%,transparent 55%);
  animation:atmBreath 16s ease-in-out infinite alternate;
}
@keyframes atmBreath{0%{opacity:.7;transform:scale(1)}100%{opacity:1;transform:scale(1.02)}}
.stApp::after{
  content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:radial-gradient(rgba(0,255,178,.07) 1px,transparent 1px);
  background-size:32px 32px;
  mask-image:radial-gradient(ellipse 100% 100% at 50% 50%,black 30%,transparent 80%);
  opacity:.3;
}

[data-testid="stSidebar"]{
  background:linear-gradient(175deg,#040810 0%,#020406 100%)!important;
  border-right:1px solid var(--b1)!important;
  box-shadow:8px 0 60px rgba(0,0,0,.8)!important;
}
[data-testid="stSidebar"] .block-container{padding:.9rem 1.1rem 2rem!important;}
[data-testid="stSidebar"]::after{
  content:'';position:absolute;top:0;right:0;width:1px;height:100%;
  background:linear-gradient(180deg,transparent 0%,rgba(0,255,178,.35) 20%,rgba(61,155,255,.35) 50%,rgba(157,127,255,.25) 80%,transparent 100%);
  animation:sidebarBeam 6s ease-in-out infinite alternate;
}
@keyframes sidebarBeam{0%{opacity:.1}50%{opacity:.35}100%{opacity:.12}}

.stTextArea textarea,.stTextInput input{
  background:var(--bg3)!important;border:1px solid var(--b2)!important;
  color:var(--text)!important;border-radius:var(--r-sm)!important;
  font-family:'Inter',sans-serif!important;font-size:13px!important;
  transition:border-color .2s,box-shadow .2s,background .2s!important;
}
.stTextArea textarea:focus,.stTextInput input:focus{
  border-color:var(--emerald)!important;
  box-shadow:0 0 0 3px rgba(0,255,178,.08)!important;
  background:var(--bg4)!important;
}

[data-testid="stFileUploader"]{
  background:var(--bg3)!important;border:1.5px dashed var(--b2)!important;
  border-radius:var(--r-md)!important;transition:all .2s ease!important;
}
[data-testid="stFileUploader"]:hover{
  border-color:var(--emerald)!important;background:rgba(0,255,178,.025)!important;
  box-shadow:0 0 24px rgba(0,255,178,.07)!important;transform:translateY(-1px)!important;
}

.stButton > button{
  background:linear-gradient(135deg,var(--emerald) 0%,var(--emerald2) 100%)!important;
  color:#030508!important;border:none!important;border-radius:var(--r-sm)!important;
  font-family:'JetBrains Mono',monospace!important;font-weight:600!important;
  font-size:11px!important;letter-spacing:1.8px!important;text-transform:uppercase!important;
  padding:.7rem 1.4rem!important;
  box-shadow:0 0 20px rgba(0,255,178,.25),0 4px 16px rgba(0,0,0,.4)!important;
  transition:all .2s cubic-bezier(.4,0,.2,1)!important;
  position:relative!important;overflow:hidden!important;
}
.stButton > button::before{
  content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.3),transparent);
  transform:skewX(-20deg);transition:left .4s ease;
}
.stButton > button:hover{
  transform:translateY(-2px)!important;
  box-shadow:0 0 40px rgba(0,255,178,.5),0 8px 24px rgba(0,0,0,.5)!important;
}
.stButton > button:hover::before{left:150%;}
.stButton > button:active{transform:translateY(0)!important;}

.stDownloadButton > button{
  background:transparent!important;color:var(--emerald)!important;
  border:1px solid rgba(0,255,178,.25)!important;border-radius:var(--r-sm)!important;
  font-family:'JetBrains Mono',monospace!important;font-size:10px!important;
  letter-spacing:1.2px!important;text-transform:uppercase!important;
  transition:all .18s ease!important;animation:none!important;
}
.stDownloadButton > button:hover{
  background:rgba(0,255,178,.07)!important;border-color:var(--emerald)!important;
  box-shadow:0 0 16px rgba(0,255,178,.15)!important;transform:translateY(-1px)!important;
}

[data-baseweb="select"] > div{
  background:var(--bg3)!important;border:1px solid var(--b2)!important;
  border-radius:var(--r-sm)!important;transition:border-color .18s!important;
}
[data-baseweb="select"] > div:hover{border-color:var(--amber)!important;}

.stTabs [data-baseweb="tab-list"]{
  background:var(--bg2)!important;border:1px solid var(--b1)!important;
  border-radius:var(--r-lg)!important;padding:4px!important;gap:2px!important;
  box-shadow:0 2px 16px rgba(0,0,0,.25)!important;
}
.stTabs [data-baseweb="tab"]{
  background:transparent!important;color:var(--muted)!important;
  border-radius:var(--r-md)!important;font-family:'JetBrains Mono',monospace!important;
  font-size:10px!important;letter-spacing:1.2px!important;text-transform:uppercase!important;
  padding:8px 16px!important;border:none!important;transition:all .15s ease!important;
}
.stTabs [data-baseweb="tab"]:hover{color:var(--dim)!important;background:rgba(255,255,255,.04)!important;}
.stTabs [aria-selected="true"]{
  background:linear-gradient(135deg,var(--emerald),var(--emerald2))!important;
  color:#030508!important;font-weight:700!important;
  box-shadow:0 0 16px rgba(0,255,178,.25)!important;
}

.stProgress > div > div > div > div{
  background:linear-gradient(90deg,var(--emerald),var(--cyan),var(--sapphire))!important;
  background-size:200% 100%!important;border-radius:4px!important;
  box-shadow:0 0 8px rgba(0,255,178,.4)!important;
  animation:progressShimmer 1.2s linear infinite!important;
}
@keyframes progressShimmer{0%{background-position:100% 0}100%{background-position:-100% 0}}

[data-testid="stExpander"]{
  background:var(--bg2)!important;border:1px solid var(--b1)!important;
  border-radius:var(--r-md)!important;transition:border-color .2s!important;
}
[data-testid="stExpander"] summary{
  font-family:'JetBrains Mono',monospace!important;font-size:11px!important;
  color:var(--dim)!important;letter-spacing:.5px!important;
}
[data-testid="stCheckbox"] label{color:var(--dim)!important;font-size:13px!important;}

::-webkit-scrollbar{width:3px;height:3px;}
::-webkit-scrollbar-track{background:transparent;}
::-webkit-scrollbar-thumb{background:var(--b2);border-radius:3px;}
hr{border-color:var(--b1)!important;margin:20px 0!important;opacity:1!important;}

.card{
  background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(255,255,255,.015));
  border:1px solid var(--b1);border-radius:var(--r-lg);
  padding:18px 20px;margin-bottom:10px;
  position:relative;overflow:hidden;backdrop-filter:blur(4px);
  transition:border-color .2s,box-shadow .2s,transform .2s;
}
.card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,255,178,.18),transparent);
}
.card:hover{
  border-color:rgba(0,255,178,.16);
  box-shadow:0 8px 32px rgba(0,0,0,.35),0 0 0 1px rgba(0,255,178,.04);
  transform:translateY(-2px);
}
.card-g{border-left:3px solid var(--emerald)!important;}
.card-r{border-left:3px solid var(--crimson)!important;}
.card-a{border-left:3px solid var(--amber)!important;}
.card-b{border-left:3px solid var(--sapphire)!important;}
.card-v{border-left:3px solid var(--violet)!important;}

.sec{
  font-family:'JetBrains Mono',monospace;font-size:9.5px;
  text-transform:uppercase;letter-spacing:3px;color:var(--muted);
  border-bottom:1px solid var(--b1);padding-bottom:8px;margin:24px 0 14px;
  display:flex;align-items:center;gap:10px;
}
.sec::before{
  content:'';display:block;width:2px;height:16px;flex-shrink:0;
  background:linear-gradient(180deg,var(--emerald) 0%,var(--sapphire) 100%);
  border-radius:2px;box-shadow:0 0 8px rgba(0,255,178,.4);
}
.lbl{
  font-family:'JetBrains Mono',monospace;font-size:9.5px;
  text-transform:uppercase;letter-spacing:1.8px;color:var(--muted);margin-bottom:4px;
}

.chip{
  display:inline-flex;align-items:center;padding:3px 10px;border-radius:20px;
  font-family:'JetBrains Mono',monospace;font-size:9.5px;
  margin:2px;letter-spacing:.3px;border:1px solid;transition:all .15s;cursor:default;
}
.chip:hover{transform:translateY(-1px);filter:brightness(1.2);}
.chip-g{background:rgba(0,255,178,.07);color:var(--emerald);border-color:rgba(0,255,178,.25);}
.chip-r{background:rgba(255,61,107,.07);color:var(--crimson);border-color:rgba(255,61,107,.25);}
.chip-a{background:rgba(255,184,48,.07);color:var(--amber);border-color:rgba(255,184,48,.25);}
.chip-b{background:rgba(61,155,255,.07);color:var(--sapphire);border-color:rgba(61,155,255,.25);}
.chip-v{background:rgba(157,127,255,.07);color:var(--violet);border-color:rgba(157,127,255,.25);}
.chip-c{background:rgba(0,229,255,.07);color:var(--cyan);border-color:rgba(0,229,255,.25);}

.al{
  border-radius:var(--r-md);padding:10px 14px;margin-bottom:8px;
  border-left:3px solid;font-size:13px;line-height:1.6;
  position:relative;overflow:hidden;transition:transform .15s;
}
.al:hover{transform:translateX(3px);}
.al-g{background:rgba(0,255,178,.045);border-color:var(--emerald);color:#7FFFD4;}
.al-a{background:rgba(255,184,48,.045);border-color:var(--amber);color:#FFD68A;}
.al-r{background:rgba(255,61,107,.045);border-color:var(--crimson);color:#FFB3C1;}
.al-b{background:rgba(61,155,255,.045);border-color:var(--sapphire);color:#A8D4FF;}

.glow-dot{
  width:6px;height:6px;border-radius:50%;background:var(--emerald);display:inline-block;
  animation:sonar 2.2s ease-out infinite;
}
@keyframes sonar{
  0%{box-shadow:0 0 0 0 rgba(0,255,178,.7);}
  70%{box-shadow:0 0 0 10px rgba(0,255,178,0);}
  100%{box-shadow:0 0 0 0 rgba(0,255,178,0);}
}

.tag{
  background:rgba(255,255,255,.03);border:1px solid var(--b1);
  border-radius:20px;padding:4px 12px;font-family:'JetBrains Mono',monospace;
  font-size:10px;color:var(--muted);letter-spacing:.4px;
  transition:all .15s;cursor:default;display:inline-block;
}
.tag:hover{border-color:var(--emerald);color:var(--emerald);}

.stat-pill{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(255,255,255,.03);border:1px solid var(--b1);
  border-radius:20px;padding:5px 14px;
  font-family:'JetBrains Mono',monospace;font-size:10px;
}

.verdict-badge{
  display:inline-flex;align-items:center;gap:6px;
  padding:6px 16px;border-radius:20px;border:1px solid;
  font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:600;
  letter-spacing:1px;text-transform:uppercase;
}

@keyframes fadeInUp{from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}
@keyframes fadeInScale{from{opacity:0;transform:scale(.94);}to{opacity:1;transform:scale(1);}}
@keyframes borderGlow{
  0%,100%{border-color:rgba(0,255,178,.1);}
  50%{border-color:rgba(0,255,178,.4);box-shadow:0 0 24px rgba(0,255,178,.12);}
}
.fade-in{animation:fadeInUp .4s ease both;}
.fade-in-2{animation:fadeInUp .4s ease .08s both;}
.fade-in-3{animation:fadeInUp .4s ease .16s both;}
.fade-in-4{animation:fadeInUp .4s ease .24s both;}
.scale-in{animation:fadeInScale .35s ease both;}

@keyframes floatUp{
  0%{transform:translateY(0) translateX(0) scale(1);opacity:0;}
  8%{opacity:var(--op);}
  92%{opacity:var(--op);}
  100%{transform:translateY(-100vh) translateX(var(--dx)) scale(.5);opacity:0;}
}
.hl-particle{position:fixed;border-radius:50%;pointer-events:none;z-index:0;animation:floatUp var(--dur) linear var(--del) infinite;}

@media(max-width:768px){
  .block-container{padding:.8rem 1rem 4rem!important;}
  .stTabs [data-baseweb="tab"]{padding:7px 10px!important;font-size:9px!important;}
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# INTRO — JS localStorage gates it to truly first visit only
# ══════════════════════════════════════════════════════
def maybe_show_intro():
    """Replaced by render_empty hero page — kept for backward compat."""
    return


# ══════════════════════════════════════════════════════
# CHART HELPERS
# ══════════════════════════════════════════════════════
def _sc(s): return "#10B981" if s>=70 else "#F59E0B" if s>=45 else "#EF4444"

def _gauge(score, title, size=210):
    if not CHARTS: return None
    c = _sc(score)
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=score,
        title={"text":title,"font":{"size":11,"color":"#64748B","family":"JetBrains Mono"}},
        number={"font":{"size":28,"color":c,"family":"JetBrains Mono"},"suffix":"/100"},
        gauge={
            "axis":{"range":[0,100],"tickwidth":1,"tickcolor":"#1E293B"},
            "bar":{"color":c,"thickness":.28}, "bgcolor":"#0E1420","borderwidth":0,
            "steps":[{"range":[0,45],"color":"#0F172A"},{"range":[45,70],"color":"#0F1F2A"},{"range":[70,100],"color":"#0F2A1F"}],
            "threshold":{"line":{"color":c,"width":3},"thickness":.78,"value":score},
        },
    ))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
                      height=size,margin=dict(l=16,r=16,t=28,b=8))
    return fig

def _bar(missing):
    if not CHARTS or not missing: return None
    df = pd.DataFrame(missing).sort_values("learn_time_days",ascending=True)
    colors = [{"Critical":"#EF4444","High":"#F59E0B","Medium":"#3B82F6"}.get(i,"#3B82F6") for i in df.get("importance",[])]
    fig = go.Figure(go.Bar(
        x=df.get("learn_time_days",[]),y=df.get("skill",[]),orientation="h",
        marker=dict(color=colors,line=dict(width=0)),
        text=[f"{d}d" for d in df.get("learn_time_days",[])],
        textposition="outside",textfont=dict(color="#64748B",size=10,family="JetBrains Mono"),
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
        height=max(180,len(df)*44),
        xaxis=dict(title=dict(text="Days to Learn",font=dict(color="#64748B",size=10)),color="#1E293B",gridcolor="#1E293B"),
        yaxis=dict(color="#94A3B8",tickfont=dict(size=10,family="JetBrains Mono")),
        margin=dict(l=8,r=56,t=8,b=36),font={"color":"#64748B","family":"JetBrains Mono"},
    )
    return fig

def _radar(matched):
    if not CHARTS or not matched or len(matched)<3: return None
    pm={"Beginner":25,"Intermediate":50,"Advanced":75,"Expert":100}
    items=matched[:8]; labels=[s.get("skill","")[:16] for s in items]
    vals=[pm.get(s.get("proficiency","Intermediate"),50) for s in items]
    labels.append(labels[0]); vals.append(vals[0])
    fig=go.Figure(go.Scatterpolar(r=vals,theta=labels,fill="toself",
        fillcolor="rgba(16,185,129,.1)",line=dict(color="#10B981",width=2),marker=dict(color="#10B981",size=5)))
    fig.update_layout(polar=dict(
        radialaxis=dict(visible=True,range=[0,100],color="#1E293B",gridcolor="#1E293B",tickfont={"size":8}),
        angularaxis=dict(color="#64748B",gridcolor="#1E293B",tickfont={"size":9}),bgcolor="rgba(0,0,0,0)"),
        paper_bgcolor="rgba(0,0,0,0)",showlegend=False,
        height=290,margin=dict(l=36,r=36,t=16,b=16),font={"color":"#64748B","family":"JetBrains Mono","size":9})
    return fig

def _chips(items,cls="g"):
    if not items: return '<span style="color:#64748B;font-size:12px;">None</span>'
    return "".join(f'<span class="chip chip-{cls}">{i}</span>' for i in items)

def _pc(fig):
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})


# ══════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════
def render_sidebar():
    # ── Role templates for JD autofill ──────────────────
    ROLE_TEMPLATES = {
        "": "",
        "Software Engineer — Backend": """We are looking for a Backend Software Engineer to join our team.

Requirements:
- 3+ years of experience with Python, Java, or Go
- Strong knowledge of REST API design and microservices
- Experience with SQL and NoSQL databases (PostgreSQL, MongoDB)
- Familiarity with Docker, Kubernetes, and CI/CD pipelines
- Experience with AWS, GCP, or Azure cloud services
- Proficiency in Git and Agile development practices

Responsibilities:
- Design and build scalable backend services
- Own end-to-end delivery of features from design to production
- Write clean, tested, well-documented code
- Collaborate with frontend and product teams
- Participate in code reviews and system design discussions""",

        "Software Engineer — Frontend": """We are looking for a Frontend Engineer to join our product team.

Requirements:
- 2+ years of experience with React, Vue, or Angular
- Strong JavaScript/TypeScript skills
- Experience with CSS, responsive design, and performance optimization
- Familiarity with REST APIs and GraphQL
- Experience with testing frameworks (Jest, Cypress)
- Understanding of accessibility (WCAG) standards

Responsibilities:
- Build and maintain high-quality web interfaces
- Collaborate with designers to implement pixel-perfect UIs
- Optimize for performance, SEO, and cross-browser compatibility
- Write unit and integration tests
- Participate in sprint planning and code reviews""",

        "Data Scientist": """We are seeking a Data Scientist to join our Analytics team.

Requirements:
- 3+ years of experience in data science or ML
- Proficiency in Python (pandas, scikit-learn, numpy)
- Experience with machine learning models and statistical analysis
- SQL proficiency for data extraction and analysis
- Experience with ML platforms (TensorFlow, PyTorch, or similar)
- Familiarity with cloud data platforms (Databricks, BigQuery, Redshift)
- Strong communication skills for presenting findings

Responsibilities:
- Build and deploy predictive models
- Analyze large datasets to surface business insights
- Partner with product and engineering teams
- Design A/B experiments and interpret results
- Document and maintain ML pipelines""",

        "Product Manager": """We are looking for a Product Manager to drive our core product roadmap.

Requirements:
- 3+ years of PM experience in a tech company
- Proven track record of shipping successful products
- Strong analytical skills — comfortable with data and metrics
- Experience writing PRDs and managing stakeholder alignment
- Excellent communication and cross-functional collaboration skills
- Familiarity with Agile/Scrum methodologies
- Technical background or ability to work closely with engineers

Responsibilities:
- Define and prioritize the product roadmap
- Write clear product requirements and user stories
- Collaborate with design, engineering, and business stakeholders
- Define success metrics and own product outcomes
- Conduct user research and synthesize insights""",

        "DevOps / SRE Engineer": """We are seeking a DevOps / Site Reliability Engineer to join our infrastructure team.

Requirements:
- 3+ years of DevOps or SRE experience
- Strong experience with Kubernetes and Docker
- Proficiency with Terraform or similar IaC tools
- Hands-on AWS, GCP, or Azure experience
- Experience with CI/CD pipelines (GitHub Actions, Jenkins, ArgoCD)
- Familiarity with monitoring tools (Prometheus, Grafana, Datadog)
- Scripting skills in Python or Bash

Responsibilities:
- Own and improve CI/CD pipelines and deployment automation
- Manage infrastructure as code
- Ensure system reliability, scalability, and security
- Respond to incidents and drive post-mortems
- Partner with engineering teams on platform needs""",

        "Machine Learning Engineer": """We are looking for an ML Engineer to productionise machine learning systems.

Requirements:
- 3+ years of ML engineering experience
- Strong Python skills (PyTorch, TensorFlow, scikit-learn)
- Experience deploying ML models to production at scale
- Familiarity with MLOps platforms (MLflow, Kubeflow, SageMaker)
- Experience with data pipelines and feature engineering
- Understanding of model monitoring and drift detection
- Knowledge of containerisation (Docker, Kubernetes)

Responsibilities:
- Build and maintain ML training and inference pipelines
- Deploy models to production with monitoring and rollback
- Collaborate with data scientists to productionise research
- Optimise model performance and resource efficiency
- Design scalable ML infrastructure""",

        "Data Engineer": """We are hiring a Data Engineer to build and maintain our data platform.

Requirements:
- 3+ years of data engineering experience
- Strong SQL and Python skills
- Experience with data warehouses (Snowflake, BigQuery, Redshift)
- Proficiency with Apache Spark, dbt, or Airflow
- Familiarity with streaming systems (Kafka, Kinesis)
- Experience with cloud data platforms (AWS, GCP, or Azure)
- Understanding of data modelling best practices

Responsibilities:
- Build reliable, scalable ETL/ELT pipelines
- Design and maintain data warehouse schemas
- Ensure data quality, freshness, and observability
- Enable self-service analytics for business teams
- Collaborate with data scientists and analysts""",

        "UI/UX Designer": """We are looking for a UI/UX Designer to shape user experiences across our products.

Requirements:
- 3+ years of product design experience
- Expert proficiency in Figma
- Portfolio demonstrating end-to-end product design process
- Experience with user research, usability testing, and A/B testing
- Strong understanding of accessibility and responsive design
- Ability to communicate design decisions to technical and business stakeholders
- Experience in an Agile product environment

Responsibilities:
- Own design from discovery through delivery
- Conduct user research and translate insights into designs
- Create wireframes, prototypes, and high-fidelity mocks
- Collaborate closely with engineers for implementation fidelity
- Maintain and evolve the design system""",

        "Cybersecurity Analyst": """We are seeking a Cybersecurity Analyst to protect our infrastructure and data.

Requirements:
- 3+ years of cybersecurity or information security experience
- Experience with SIEM tools (Splunk, Sentinel, or similar)
- Knowledge of network security, vulnerability management, and threat analysis
- Familiarity with cloud security (AWS/Azure/GCP security services)
- Understanding of OWASP, NIST, and ISO 27001 frameworks
- Security certifications (CISSP, CEH, CompTIA Security+) preferred
- Scripting ability in Python or PowerShell

Responsibilities:
- Monitor systems for security incidents and threats
- Conduct vulnerability assessments and penetration tests
- Respond to and investigate security incidents
- Develop and enforce security policies
- Educate teams on security best practices""",

        "Marketing Manager": """We are looking for a Marketing Manager to lead our growth marketing function.

Requirements:
- 4+ years of B2B or B2C marketing experience
- Proven experience managing paid media (Google Ads, Meta, LinkedIn)
- Strong analytical skills — comfortable with attribution and funnel metrics
- Experience with marketing automation tools (HubSpot, Marketo, or similar)
- Excellent copywriting and content strategy skills
- Data-driven mindset with focus on ROI
- Experience working cross-functionally with sales and product teams

Responsibilities:
- Own the end-to-end marketing funnel from awareness to conversion
- Run and optimise paid acquisition campaigns
- Lead content marketing, SEO, and email programmes
- Analyse campaign performance and report to leadership
- Manage agency and contractor relationships""",
    }

    with st.sidebar:
        # ── Header ───────────────────────────────────────
        st.markdown("""
        <style>
        @keyframes logoSpin {
          0%   { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        @keyframes logoPulse {
          0%,100% { box-shadow: 0 0 16px rgba(0,217,163,.15), 0 0 32px rgba(0,217,163,.05); }
          50%      { box-shadow: 0 0 28px rgba(0,217,163,.35), 0 0 56px rgba(0,217,163,.12); }
        }
        .hl-logo-ring {
          animation: logoPulse 3s ease-in-out infinite;
        }
        .hl-sidebar-step {
          display: flex; align-items: flex-start; gap: 10px;
          padding: 8px 0; border-bottom: 1px solid var(--border);
        }
        .hl-step-num {
          width: 20px; height: 20px; border-radius: 50%;
          background: linear-gradient(135deg, var(--green), var(--blue));
          color: #020810; font-family: 'JetBrains Mono', monospace;
          font-size: 10px; font-weight: 700;
          display: flex; align-items: center; justify-content: center;
          flex-shrink: 0; margin-top: 2px;
        }
        .hl-step-label { font-size: 11px; color: var(--muted); line-height: 1.5; }
        </style>
        <div style="padding:10px 0 20px;border-bottom:1px solid var(--border2);margin-bottom:18px;">
          <div style="display:flex;align-items:center;gap:10px;">
            <div class="hl-logo-ring" style="width:36px;height:36px;
                        background:linear-gradient(145deg,#0D1F30,#060E18);
                        border-radius:10px;border:1px solid rgba(0,217,163,.35);
                        display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <svg width="20" height="20" viewBox="0 0 46 46" fill="none">
                <circle cx="23" cy="23" r="11" fill="rgba(0,217,163,.1)" stroke="#00D9A3" stroke-width="1.5"/>
                <line x1="23" y1="16" x2="23" y2="19.5" stroke="#00D9A3" stroke-width="1.5" stroke-linecap="round"/>
                <line x1="23" y1="26.5" x2="23" y2="30" stroke="#00D9A3" stroke-width="1.5" stroke-linecap="round"/>
                <line x1="16" y1="23" x2="19.5" y2="23" stroke="#00D9A3" stroke-width="1.5" stroke-linecap="round"/>
                <line x1="26.5" y1="23" x2="30" y2="23" stroke="#00D9A3" stroke-width="1.5" stroke-linecap="round"/>
                <circle cx="23" cy="23" r="2.5" fill="#00D9A3"/>
                <line x1="31" y1="31" x2="37" y2="37" stroke="#00D9A3" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </div>
            <div>
              <div style="font-family:'Outfit',sans-serif;font-size:17px;font-weight:800;
                          background:linear-gradient(135deg,#00D9A3,#4D9EFF);
                          -webkit-background-clip:text;background-clip:text;color:transparent;
                          letter-spacing:-.4px;line-height:1.1;">HireLens AI</div>
              <div style="font-family:'JetBrains Mono',monospace;font-size:8px;
                          color:var(--muted);letter-spacing:1.5px;text-transform:uppercase;">
                5-Agent Analyzer</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Step 1: Resume ─────────────────────────────
        st.markdown("""
        <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--green);
                    text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;
                    display:flex;align-items:center;gap:6px;">
          <span style="width:16px;height:16px;background:var(--green);color:#020810;
                       border-radius:50%;display:inline-flex;align-items:center;
                       justify-content:center;font-size:9px;font-weight:700;">1</span>
          Resume PDF
        </div>""", unsafe_allow_html=True)
        uploaded = st.file_uploader("resume", type=["pdf"], label_visibility="collapsed")
        if uploaded:
            kb = uploaded.size // 1024
            st.markdown(
                f'<div style="display:flex;align-items:center;gap:8px;background:rgba(0,255,178,.06);'
                f'border:1px solid rgba(0,255,178,.25);border-radius:8px;padding:7px 12px;margin-top:4px;">'
                f'<span style="color:var(--green);font-size:16px;">✓</span>'
                f'<div><div style="font-size:12px;color:var(--text);font-weight:500;">{uploaded.name}</div>'
                f'<div style="font-size:10px;color:var(--muted);">{kb} KB · Ready</div></div>'
                f'</div>',
                unsafe_allow_html=True)

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        # ── Step 2: Company ────────────────────────────
        st.markdown("""
        <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--blue);
                    text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;
                    display:flex;align-items:center;gap:6px;">
          <span style="width:16px;height:16px;background:var(--blue);color:#020810;
                       border-radius:50%;display:inline-flex;align-items:center;
                       justify-content:center;font-size:9px;font-weight:700;">2</span>
          Target Company
        </div>""", unsafe_allow_html=True)
        company = st.text_input("company", placeholder="Google · Stripe · Infosys · TCS…",
                                label_visibility="collapsed")

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        # ── Step 3: Role template selector ─────────────
        st.markdown("""
        <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--amber);
                    text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;
                    display:flex;align-items:center;gap:6px;">
          <span style="width:16px;height:16px;background:var(--amber);color:#020810;
                       border-radius:50%;display:inline-flex;align-items:center;
                       justify-content:center;font-size:9px;font-weight:700;">3</span>
          Role Template <span style="color:var(--muted);font-size:8px;margin-left:4px;">(optional)</span>
        </div>""", unsafe_allow_html=True)

        role_choice = st.selectbox(
            "role_template",
            options=list(ROLE_TEMPLATES.keys()),
            format_func=lambda x: "— Select a role to auto-fill JD —" if x == "" else x,
            label_visibility="collapsed",
            key="role_selector",
        )

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        # ── Step 4: Job Description ─────────────────────
        st.markdown("""
        <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--violet);
                    text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;
                    display:flex;align-items:center;gap:6px;">
          <span style="width:16px;height:16px;background:var(--violet);color:#020810;
                       border-radius:50%;display:inline-flex;align-items:center;
                       justify-content:center;font-size:9px;font-weight:700;">4</span>
          Job Description
        </div>""", unsafe_allow_html=True)

        jd_placeholder = ROLE_TEMPLATES.get(role_choice, "")
        jd = st.text_area(
            "jd",
            height=200,
            placeholder="Paste the full job description here, or select a role template above…",
            value=jd_placeholder,
            label_visibility="collapsed",
        )
        if jd:
            word_count = len(jd.split())
            color = "var(--green)" if word_count >= 80 else "var(--amber)" if word_count >= 30 else "var(--red)"
            st.markdown(
                f'<div style="font-family:JetBrains Mono,monospace;font-size:10px;'
                f'color:{color};text-align:right;margin-top:2px;">'
                f'{word_count} words {"✓ good length" if word_count >= 80 else "· add more detail for better analysis"}'
                f'</div>',
                unsafe_allow_html=True)

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        # ── Brutal mode ─────────────────────────────────
        brutal = st.checkbox("💀 Brutal Honesty Mode", value=False)
        if brutal:
            st.markdown("""
            <div style="background:rgba(255,61,107,.07);border:1px solid rgba(255,61,107,.35);
                        border-left:3px solid #FF3D6B;border-radius:8px;
                        padding:9px 13px;margin-top:5px;">
              <div style="font-family:'JetBrains Mono',monospace;font-size:10px;
                          color:#FF3D6B;text-transform:uppercase;letter-spacing:1px;
                          margin-bottom:3px;">⚠ Brutal Mode Active</div>
              <div style="font-size:11px;color:#FF8FAB;line-height:1.5;">
                Zero diplomatic softening. Every failure named explicitly.
              </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        # ── Analyze button ──────────────────────────────
        analyze = st.button("🔍  Analyze Application", use_container_width=True)

        # ── Results stats + New Analysis ───────────────
        if st.session_state.get("done"):
            results_ss = st.session_state.get("results", {})
            if results_ss:
                coord_ss  = results_ss.get("coordinator", {})
                ats_ss    = results_ss.get("ats", {})
                overall   = coord_ss.get("overall_score", 0)
                prob_ss   = coord_ss.get("rejection_probability", "High")
                prob_c_ss = {"Very High":"#EF4444","High":"#EF4444",
                             "Medium":"#F59E0B","Low":"#10B981"}.get(prob_ss,"#EF4444")
                ats_s     = ats_ss.get("ats_score", 0)
                co_ss     = st.session_state.get("company", "")
                st.markdown(f"""
                <div style="background:rgba(255,255,255,.025);border:1px solid var(--border2);
                            border-radius:10px;padding:12px 14px;margin:10px 0 6px;">
                  <div style="font-family:'JetBrains Mono',monospace;font-size:8px;
                              color:var(--muted);text-transform:uppercase;letter-spacing:1.5px;
                              margin-bottom:8px;">Last Analysis{f" · {co_ss}" if co_ss else ""}</div>
                  <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div>
                      <div style="font-size:9px;color:var(--muted);margin-bottom:2px;">Overall</div>
                      <div style="font-family:'JetBrains Mono',monospace;font-size:26px;
                                  font-weight:800;color:{_sc(overall)};line-height:1;">{overall}</div>
                    </div>
                    <div style="text-align:right;">
                      <div style="font-size:9px;color:var(--muted);margin-bottom:2px;">ATS</div>
                      <div style="font-family:'JetBrains Mono',monospace;font-size:18px;
                                  font-weight:700;color:{_sc(ats_s)};">{ats_s}</div>
                    </div>
                    <div style="text-align:right;">
                      <div style="font-size:9px;color:var(--muted);margin-bottom:2px;">Risk</div>
                      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;
                                  font-weight:700;color:{prob_c_ss};">{prob_ss}</div>
                    </div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

            if st.button("🔄  New Analysis", use_container_width=True):
                for k in list(st.session_state.keys()):
                    st.session_state.pop(k, None)
                st.rerun()

        # ── API key status ──────────────────────────────
        api_key = (os.environ.get("ANTHROPIC_API_KEY") or
                   os.environ.get("OPENAI_API_KEY") or
                   os.environ.get("GOOGLE_API_KEY"))
        if not api_key:
            st.markdown("""
            <div style="background:rgba(245,166,35,.05);border:1px solid rgba(245,166,35,.2);
                        border-radius:8px;padding:10px 12px;margin-top:10px;">
              <div style="font-family:'JetBrains Mono',monospace;font-size:9px;
                          color:var(--amber);text-transform:uppercase;letter-spacing:1px;
                          margin-bottom:3px;">⚡ Demo Mode</div>
              <div style="font-size:11px;color:var(--muted);line-height:1.5;">
                No API key detected.<br>Add ANTHROPIC_API_KEY to .env for live analysis.
              </div>
            </div>
            """, unsafe_allow_html=True)

    return uploaded, company, jd, brutal, analyze

# ══════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════
def render_header(company="", analyzed_at=""):
    co_html = (
        '<span style="font-size:1rem;font-weight:300;color:rgba(255,255,255,.4);margin:0 6px;">/</span>'
        f'<span style="font-size:1rem;font-weight:600;color:var(--emerald);">{company}</span>'
    ) if company else ""
    ts_html = (
        f'<span class="stat-pill fade-in-4" style="font-size:10px;color:var(--dim);">'
        f'<span style="color:var(--emerald);font-size:10px;">&#9679;</span> {analyzed_at}'
        f'</span>'
    ) if analyzed_at else ""

    st.markdown(f"""
    <div class="fade-in" style="padding:16px 0 26px;margin-bottom:22px;
         border-bottom:1px solid var(--b1);position:relative;">
      <div style="display:flex;align-items:center;justify-content:space-between;
                  flex-wrap:wrap;gap:12px;margin-bottom:8px;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div style="width:40px;height:40px;border-radius:12px;
                      background:linear-gradient(145deg,rgba(0,255,178,.12),rgba(61,155,255,.08));
                      border:1px solid rgba(0,255,178,.3);flex-shrink:0;
                      display:flex;align-items:center;justify-content:center;
                      box-shadow:0 0 20px rgba(0,255,178,.12);
                      animation:borderGlow 4s ease-in-out infinite;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <circle cx="10" cy="10" r="5" stroke="#00FFB2" stroke-width="1.5"/>
              <path d="M14.5 14.5L19 19" stroke="#00FFB2" stroke-width="1.8" stroke-linecap="round"/>
              <circle cx="10" cy="10" r="2" fill="#00FFB2" opacity=".6"/>
            </svg>
          </div>
          <div>
            <div style="font-family:'Sora',sans-serif;font-size:1.45rem;font-weight:800;
                        letter-spacing:-.5px;line-height:1.1;
                        background:linear-gradient(135deg,#ffffff 0%,#00FFB2 45%,#3D9BFF 100%);
                        -webkit-background-clip:text;background-clip:text;color:transparent;">
              HireLens AI{co_html}
            </div>
            <div style="font-family:'JetBrains Mono',monospace;font-size:8.5px;
                        color:var(--muted);letter-spacing:2.5px;text-transform:uppercase;margin-top:3px;">
              Multi-Agent Resume Analyzer
            </div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
          {ts_html}
          <span class="stat-pill fade-in-2" style="color:var(--emerald);font-size:10px;">
            <span class="glow-dot" style="width:5px;height:5px;flex-shrink:0;"></span>
            5 Agents Active
          </span>
          <span class="stat-pill fade-in-3" style="color:var(--sapphire);font-size:10px;">
            40+ Signals
          </span>
        </div>
      </div>
      <div style="position:absolute;bottom:0;left:0;right:0;height:1px;overflow:hidden;">
        <div style="height:1px;
                    background:linear-gradient(90deg,transparent,var(--emerald),var(--sapphire),var(--violet),transparent);
                    animation:scanSlide 4s ease-in-out infinite alternate;"></div>
      </div>
    </div>
    <style>
    @keyframes scanSlide{{0%{{transform:translateX(-100%);opacity:.5;}}100%{{transform:translateX(100%);opacity:.5;}}}}
    </style>
    """, unsafe_allow_html=True)


def render_score_explainer(results):
    """Compact score meaning cards shown right below the 5 dials."""
    coord = results.get("coordinator", {})
    overall = coord.get("overall_score", 0)
    prob    = coord.get("rejection_probability", "High")
    verdict = coord.get("application_verdict", "Apply After Fixes")
    root    = coord.get("root_cause_category", "Multiple")

    prob_emoji = {"Very High": "💀", "High": "⚠️", "Medium": "🎯", "Low": "✅"}.get(prob, "⚠️")
    verdict_emoji = {"Apply Now": "🚀", "Apply After Fixes": "🔧", "Not Ready Yet": "⏳"}.get(verdict, "🔧")
    verdict_color = {"Apply Now": "#10B981", "Apply After Fixes": "#F59E0B", "Not Ready Yet": "#EF4444"}.get(verdict, "#F59E0B")
    prob_color = {"Very High": "#EF4444", "High": "#EF4444", "Medium": "#F59E0B", "Low": "#10B981"}.get(prob, "#EF4444")

    c1, c2, c3 = st.columns(3, gap="small")
    with c1:
        st.markdown(f"""
        <div class="card" style="padding:14px 16px;border-left:3px solid {prob_color};">
          <div class="lbl">Rejection Risk</div>
          <div style="font-size:22px;margin:4px 0;">{prob_emoji}</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:14px;
                      font-weight:700;color:{prob_color};">{prob}</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="card" style="padding:14px 16px;border-left:3px solid {verdict_color};">
          <div class="lbl">Verdict</div>
          <div style="font-size:22px;margin:4px 0;">{verdict_emoji}</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:13px;
                      font-weight:700;color:{verdict_color};">{verdict}</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        root_color = {"Skills Gap":"#EF4444","ATS Filtering":"#3D9BFF",
                      "Experience Level":"#F59E0B","Narrative Clarity":"#9D7FFF",
                      "Multiple":"#FF3D6B"}.get(root, "#94A3B8")
        st.markdown(f"""
        <div class="card" style="padding:14px 16px;border-left:3px solid {root_color};">
          <div class="lbl">Root Cause</div>
          <div style="font-size:22px;margin:4px 0;">🔍</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:12px;
                      font-weight:700;color:{root_color};">{root}</div>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# AGENT TABS
# ══════════════════════════════════════════════════════
def render_agent_tabs(results):
    ats  = results.get("ats",{})
    sk   = results.get("skills",{})
    exp  = results.get("experience",{})
    hm   = results.get("hiring_manager",{})
    coord= results.get("coordinator",{})

    t1,t2,t3,t4,t5 = st.tabs(["🤖 ATS Agent","🔬 Skills Gap","📊 Experience","🧠 Hiring Manager","🎯 Coordinator"])

    # ── ATS ──
    with t1:
        score = ats.get("ats_score",0)
        pf    = ats.get("pass_fail","FAIL")
        pf_c  = {"PASS":"#10B981","BORDERLINE":"#F59E0B","FAIL":"#EF4444"}.get(pf,"#EF4444")
        density = ats.get("keyword_density_pct",0)

        c1,c2,c3 = st.columns([1,1.2,1],gap="medium")
        with c1:
            if CHARTS:
                fig=_gauge(score,"ATS SCORE");
                if fig: _pc(fig)
            else:
                st.markdown(f'<div class="card" style="text-align:center;padding:28px 16px;"><div class="lbl">ATS Score</div><div style="font-family:JetBrains Mono,monospace;font-size:52px;font-weight:700;color:{_sc(score)};">{score}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align:center;margin-top:-4px;"><span style="background:{pf_c}18;border:1px solid {pf_c};border-radius:20px;padding:5px 14px;font-family:JetBrains Mono,monospace;font-size:12px;color:{pf_c};">{pf}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align:center;margin-top:6px;font-family:JetBrains Mono,monospace;font-size:10px;color:#64748B;">Keyword Density: <span style="color:{_sc(density)};">{density}%</span></div>', unsafe_allow_html=True)

        with c2:
            st.markdown('<div class="sec" style="margin-top:0;">Section Audit</div>', unsafe_allow_html=True)
            audit=ats.get("section_audit",{})
            for name,key in [("Summary","has_summary"),("Skills","has_skills"),("Experience","has_experience"),("Education","has_education"),("Contact","has_contact")]:
                p=audit.get(key,False); ic,bg=("#10B981","#064E3B") if p else ("#EF4444","#450A0A")
                st.markdown(f'<div style="background:{bg};border-radius:7px;padding:7px 12px;margin-bottom:5px;display:flex;justify-content:space-between;align-items:center;"><span style="font-size:13px;color:#CBD5E1;">{name}</span><span style="font-family:JetBrains Mono,monospace;font-size:14px;color:{ic};font-weight:700;">{"✓" if p else "✗"}</span></div>', unsafe_allow_html=True)

        with c3:
            bd=ats.get("score_breakdown",{})
            if bd:
                st.markdown('<div class="sec" style="margin-top:0;">Score Breakdown</div>', unsafe_allow_html=True)
                lmap={"keyword_match":"Keywords","section_structure":"Sections","format_parsability":"Format","contact_completeness":"Contact"}
                for k,v in bd.items():
                    lbl=lmap.get(k,k.replace("_"," ").title()); c=_sc(v)
                    st.markdown(f'<div style="margin-bottom:9px;"><div style="display:flex;justify-content:space-between;margin-bottom:3px;"><span style="font-size:12px;color:#94A3B8;">{lbl}</span><span style="font-family:JetBrains Mono,monospace;font-size:11px;color:{c};">{v}</span></div><div style="background:#1E293B;border-radius:3px;height:5px;"><div style="width:{v}%;height:100%;background:{c};border-radius:3px;"></div></div></div>', unsafe_allow_html=True)

        ac="al-g" if score>=70 else "al-a" if score>=45 else "al-r"
        st.markdown(f'<div class="al {ac}">{ats.get("ats_verdict","")}</div>', unsafe_allow_html=True)

        risks=ats.get("top_ats_risks",[]); fixes=ats.get("quick_ats_fixes",[])
        if risks or fixes:
            rc1,rc2=st.columns(2)
            with rc1:
                if risks:
                    st.markdown('<div class="sec">Top ATS Risks</div>', unsafe_allow_html=True)
                    for i,r in enumerate(risks[:5],1):
                        rc=("#EF4444" if i<=2 else "#F59E0B")
                        st.markdown(f'<div style="display:flex;gap:8px;padding:6px 0;border-bottom:1px solid #1E293B;"><span style="font-family:JetBrains Mono,monospace;font-size:10px;color:{rc};flex-shrink:0;">#{i}</span><span style="font-size:12px;color:#94A3B8;line-height:1.4;">{r}</span></div>', unsafe_allow_html=True)
            with rc2:
                if fixes:
                    st.markdown('<div class="sec">Quick Fixes</div>', unsafe_allow_html=True)
                    for f in fixes[:5]: st.markdown(f'<div class="al al-g" style="margin-bottom:5px;">→ {f}</div>', unsafe_allow_html=True)

        st.markdown('<div class="sec">Keywords</div>', unsafe_allow_html=True)
        kc1,kc2=st.columns(2)
        with kc1:
            st.markdown(f'<div class="lbl" style="color:#10B981;">✓ Matched ({len(ats.get("keyword_matches",[]))})</div>', unsafe_allow_html=True)
            st.markdown(_chips(ats.get("keyword_matches",[])[:14],"g"), unsafe_allow_html=True)
        with kc2:
            st.markdown(f'<div class="lbl" style="color:#EF4444;">✗ Missing ({len(ats.get("missing_keywords",[]))})</div>', unsafe_allow_html=True)
            st.markdown(_chips(ats.get("missing_keywords",[])[:14],"r"), unsafe_allow_html=True)

        for issue in ats.get("formatting_issues",[]):
            st.markdown(f'<div class="al al-a">⚠ {issue}</div>', unsafe_allow_html=True)

        # ATS What-If Simulator
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🔮 ATS What-If Simulator — Preview score after adding keywords"):
            render_ats_whatif(results)

    # ── SKILLS ──
    with t2:
        score=sk.get("match_score",0)
        c1,c2=st.columns([1,1.2],gap="large")
        with c1:
            if CHARTS:
                fig=_gauge(score,"SKILLS MATCH");
                if fig: _pc(fig)
            traj=sk.get("skill_trajectory","")
            if traj: st.markdown(f'<div class="card" style="padding:12px 15px;"><div class="lbl">Skill Trajectory</div><div style="font-size:12px;color:#94A3B8;margin-top:4px;line-height:1.6;">{traj}</div></div>', unsafe_allow_html=True)
        with c2:
            fig2=_radar(sk.get("matched_skills",[]));
            if fig2: _pc(fig2)
            top5=sk.get("top_5_missing",[])
            if top5:
                st.markdown('<div class="sec">Top 5 Missing</div>', unsafe_allow_html=True)
                for s in top5: st.markdown(f'<div style="display:flex;gap:8px;align-items:center;padding:6px 0;border-bottom:1px solid #1E293B;"><span style="color:#EF4444;font-family:JetBrains Mono,monospace;font-size:13px;">✗</span><span style="font-size:13px;color:#CBD5E1;">{s}</span></div>', unsafe_allow_html=True)

        ac="al-g" if score>=70 else "al-a" if score>=45 else "al-r"
        st.markdown(f'<div class="al {ac}" style="margin:10px 0;">{sk.get("skills_verdict","")}</div>', unsafe_allow_html=True)

        missing=sk.get("missing_critical",[])
        if missing:
            st.markdown('<div class="sec">Critical Gaps — Days to Learn</div>', unsafe_allow_html=True)
            fig3=_bar(missing);
            if fig3: _pc(fig3)
            for item in missing:
                imp=item.get("importance","Medium")
                ic={"Critical":"r","High":"a","Medium":"b"}.get(imp,"b")
                why=item.get("why_it_matters",""); res=item.get("recommended_resource","")
                bc={"Critical":"#EF4444","High":"#F59E0B","Medium":"#3B82F6"}.get(imp,"#3B82F6")
                why_html = f'<div style="font-size:12px;color:#64748B;margin-bottom:3px;">{why}</div>' if why else ""
                res_html  = f'<div style="font-size:12px;color:#10B981;">→ {res}</div>' if res else ""
                st.markdown(f'<div class="card" style="padding:12px 16px;margin-bottom:7px;border-left:3px solid {bc};"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;"><span style="font-size:13px;font-weight:600;color:#E2E8F0;">{item.get("skill","")}</span><span class="chip chip-{ic}">{imp} · ~{item.get("learn_time_days","?")}d</span></div>{why_html}{res_html}</div>', unsafe_allow_html=True)

        matched=sk.get("matched_skills",[])
        if matched:
            st.markdown('<div class="sec">Matched Skills</div>', unsafe_allow_html=True)
            imap={"Required":"r","Preferred":"a","Nice-to-have":"b"}
            for s in matched:
                prof=s.get("proficiency",""); imp=s.get("jd_importance","Required")
                pc2={"Expert":"#10B981","Advanced":"#3B82F6","Intermediate":"#F59E0B","Beginner":"#64748B"}.get(prof,"#64748B")
                chip_cls=imap.get(imp,"b")
                st.markdown(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid #1E293B;"><div><span style="font-size:13px;color:#E2E8F0;">{s.get("skill","")}</span><div style="font-size:11px;color:#475569;margin-top:1px;">{s.get("evidence","")[:60]}</div></div><div style="display:flex;gap:6px;align-items:center;flex-shrink:0;"><span class="chip chip-{chip_cls}" style="font-size:9px;">{imp}</span><span style="font-family:JetBrains Mono,monospace;font-size:11px;color:{pc2};">{prof}</span></div></div>', unsafe_allow_html=True)

        for t in sk.get("transferable_skills",[]):
            st.markdown(f'<div class="al al-b">↔ {t}</div>', unsafe_allow_html=True)

    # ── EXPERIENCE ──
    with t3:
        escore=exp.get("experience_score",0); quant=exp.get("quantification_score",0)
        sm=exp.get("seniority_match","?"); prog=exp.get("career_progression","?"); verb=exp.get("action_verb_quality","?")
        cols5=st.columns(5,gap="small")
        for col,(lbl,val,clr) in zip(cols5,[
            ("Score",f"{escore}/100",_sc(escore)),
            ("Seniority",sm,{"Under":"#EF4444","Match":"#10B981","Over":"#F59E0B"}.get(sm,"#3B82F6")),
            ("Quantified",f"{quant}%",_sc(quant)),
            ("Verbs",verb,{"Strong":"#10B981","Mixed":"#F59E0B","Weak":"#EF4444"}.get(verb,"#64748B")),
            ("Progression",prog,{"Strong":"#10B981","Lateral":"#F59E0B","Unclear":"#EF4444"}.get(prog,"#64748B")),
        ]):
            with col: st.markdown(f'<div class="card" style="text-align:center;padding:14px 8px;"><div class="lbl">{lbl}</div><div style="font-family:JetBrains Mono,monospace;font-size:16px;font-weight:600;color:{clr};margin-top:5px;">{val}</div></div>', unsafe_allow_html=True)

        yr=exp.get("years_apparent"); req=exp.get("years_required")
        if yr or req: st.markdown(f'<div class="card" style="display:flex;gap:24px;align-items:center;padding:12px 18px;"><div><div class="lbl">Years Apparent</div><div style="font-family:JetBrains Mono,monospace;font-size:22px;color:#3B82F6;">{yr or "?"}</div></div><div style="color:#1E293B;font-size:22px;">→</div><div><div class="lbl">Years Required</div><div style="font-family:JetBrains Mono,monospace;font-size:22px;color:#64748B;">{req or "?"}</div></div></div>', unsafe_allow_html=True)

        ac="al-g" if escore>=70 else "al-a" if escore>=45 else "al-r"
        st.markdown(f'<div class="al {ac}" style="margin:10px 0;">{exp.get("experience_verdict","")}</div>', unsafe_allow_html=True)

        bullets=exp.get("bullet_quality",[])
        if bullets:
            st.markdown('<div class="sec">Bullet Critique + AI Rewrites</div>', unsafe_allow_html=True)
            for b in bullets:
                rw=b.get("rewritten","")
                rw_html = f'<div><div class="lbl" style="color:#8B5CF6;">Rewritten</div><div style="font-size:13px;color:#C4B5FD;font-style:italic;">{rw}</div></div>' if rw else ""
                st.markdown(f'<div class="card" style="border-left:3px solid #EF4444;padding:14px 18px;margin-bottom:8px;"><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:10px;"><div><div class="lbl" style="color:#EF4444;">Original</div><div style="font-size:13px;color:#94A3B8;font-style:italic;">"{b.get("bullet_excerpt","")}"</div></div><div><div class="lbl" style="color:#F59E0B;">Issue</div><div style="font-size:13px;color:#CBD5E1;">{b.get("issue","")}</div></div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;"><div><div class="lbl" style="color:#3B82F6;">Fix</div><div style="font-size:13px;color:#CBD5E1;">{b.get("fix","")}</div></div>{rw_html}</div></div>', unsafe_allow_html=True)

        bc1,bc2=st.columns(2,gap="medium")
        with bc1:
            if exp.get("best_bullets"):
                st.markdown('<div class="sec">Best Bullets</div>', unsafe_allow_html=True)
                for b in exp.get("best_bullets",[]): st.markdown(f'<div class="al al-g">✨ "{b}"</div>', unsafe_allow_html=True)
        with bc2:
            if exp.get("weakest_bullets"):
                st.markdown('<div class="sec">Weakest Bullets — Rewrite</div>', unsafe_allow_html=True)
                for b in exp.get("weakest_bullets",[]): st.markdown(f'<div class="al al-r">✗ "{b}"</div>', unsafe_allow_html=True)

        projs=exp.get("project_evaluations",[])
        if projs:
            st.markdown('<div class="sec">Project Evaluations</div>', unsafe_allow_html=True)
            pc_cols=st.columns(min(len(projs),3),gap="medium")
            rmap={"High":"g","Medium":"a","Low":"r"}
            for col,proj in zip(pc_cols,projs):
                with col:
                    rc=rmap.get(proj.get("relevance","Low"),"r")
                    ic2={"Strong":"#10B981","Moderate":"#F59E0B","Weak":"#EF4444"}.get(proj.get("impact_clarity","Weak"),"#EF4444")
                    miss=proj.get("missing_info","")
                    miss_html=f'<div style="font-size:11px;color:#F59E0B;margin-top:3px;">{miss[:60]}</div>' if miss else ""
                    st.markdown(f'<div class="card" style="padding:13px;"><div style="font-size:13px;font-weight:600;color:#E2E8F0;margin-bottom:7px;">{proj.get("title","")[:40]}</div><span class="chip chip-{rc}">Rel: {proj.get("relevance","")}</span><div style="font-size:11px;color:#64748B;margin-top:6px;">Impact: <span style="color:{ic2};">{proj.get("impact_clarity","")}</span></div>{miss_html}</div>', unsafe_allow_html=True)

    # ── HIRING MANAGER ──
    with t4:
        gut=hm.get("gut_score",0); wi=hm.get("would_interview","No")
        conf=hm.get("decision_confidence","Medium"); hs=hm.get("headline_strength","Adequate")
        wi_c={"Yes":"#10B981","Maybe":"#F59E0B","No":"#EF4444"}.get(wi,"#EF4444")
        wi_lbl={"Yes":"✅ WOULD INTERVIEW","Maybe":"🤔 MAYBE","No":"❌ WOULD NOT INTERVIEW"}.get(wi,"❌ NO")

        c1,c2=st.columns([1,1.5],gap="large")
        with c1:
            if CHARTS:
                fig=_gauge(gut,"HM GUT SCORE");
                if fig: _pc(fig)
            st.markdown(f'<div style="text-align:center;margin-top:-6px;"><span style="background:{wi_c}18;border:1px solid {wi_c};border-radius:20px;padding:7px 18px;font-family:JetBrains Mono,monospace;font-size:12px;color:{wi_c};">{wi_lbl}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align:center;margin-top:7px;font-family:JetBrains Mono,monospace;font-size:10px;color:#64748B;">Confidence: {conf}  ·  Headline: {hs}</div>', unsafe_allow_html=True)
            fi=hm.get("first_impression","")
            if fi: st.markdown(f'<div class="card" style="margin-top:12px;padding:13px 15px;"><div class="lbl">6-Second Impression</div><div style="font-size:13px;color:#94A3B8;font-style:italic;margin-top:5px;line-height:1.6;">"{fi}"</div></div>', unsafe_allow_html=True)

        with c2:
            ko=hm.get("knockout_factors",[])
            if ko:
                st.markdown('<div class="sec" style="margin-top:0;">💀 Knockout Factors</div>', unsafe_allow_html=True)
                for f in ko: st.markdown(f'<div style="background:#1A0505;border:1px solid #7F1D1D;border-left:3px solid #EF4444;border-radius:8px;padding:10px 14px;margin-bottom:6px;font-size:13px;color:#FCA5A5;">{f}</div>', unsafe_allow_html=True)

            reasons=hm.get("rejection_reasons",[])
            if reasons:
                st.markdown('<div class="sec">Rejection Reasons</div>', unsafe_allow_html=True)
                for r in reasons:
                    sev=r.get("severity","Major")
                    sc3={"Knockout":"#EF4444","Major":"#F59E0B","Minor":"#64748B"}.get(sev,"#F59E0B")
                    chip_cls="r" if sev=="Knockout" else "a"
                    fix2=r.get("how_to_fix","")
                    fix_html=f'<div style="font-size:12px;color:#10B981;">→ {fix2}</div>' if fix2 else ""
                    st.markdown(f'<div class="card" style="border-left:3px solid {sc3};padding:12px 16px;margin-bottom:7px;"><div style="display:flex;justify-content:space-between;margin-bottom:4px;"><span style="font-size:13px;color:#CBD5E1;">{r.get("reason","")}</span><span class="chip chip-{chip_cls}" style="font-size:9px;">{sev}</span></div>{fix_html}</div>', unsafe_allow_html=True)

            tp=hm.get("interview_talking_points",[])
            if tp:
                st.markdown('<div class="sec">Interview Talking Points</div>', unsafe_allow_html=True)
                for i,p in enumerate(tp,1): st.markdown(f'<div style="display:flex;gap:10px;align-items:flex-start;background:#0E1420;border:1px solid #1E293B;border-radius:8px;padding:9px 13px;margin-bottom:6px;"><span style="background:#3B82F6;color:#fff;border-radius:50%;min-width:18px;height:18px;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;">{i}</span><span style="font-size:13px;color:#94A3B8;line-height:1.5;">{p}</span></div>', unsafe_allow_html=True)

        rf1,rf2=st.columns(2,gap="medium")
        with rf1:
            if hm.get("red_flags"):
                st.markdown('<div class="sec">Red Flags</div>', unsafe_allow_html=True)
                for f in hm.get("red_flags",[]): st.markdown(f'<div class="al al-r">🚩 {f}</div>', unsafe_allow_html=True)
        with rf2:
            if hm.get("green_flags"):
                st.markdown('<div class="sec">Green Flags</div>', unsafe_allow_html=True)
                for f in hm.get("green_flags",[]): st.markdown(f'<div class="al al-g">✓ {f}</div>', unsafe_allow_html=True)

        nc1,nc2=st.columns(2,gap="medium")
        with nc1:
            if hm.get("narrative_arc"): st.markdown(f'<div class="al al-b"><b>Narrative:</b> {hm.get("narrative_arc","")}</div>', unsafe_allow_html=True)
        with nc2:
            if hm.get("culture_fit_signals"): st.markdown(f'<div class="al al-b"><b>Culture:</b> {hm.get("culture_fit_signals","")}</div>', unsafe_allow_html=True)

        em=hm.get("rejection_email_draft","")
        if em: st.markdown(f'<div class="card" style="border-left:3px solid #EF4444;margin-top:8px;padding:14px 18px;"><div class="lbl" style="color:#EF4444;">The Rejection Email They\'d Send</div><div style="font-family:JetBrains Mono,monospace;font-size:12px;color:#94A3B8;margin-top:7px;font-style:italic;">{em}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="al al-{"g" if gut>=70 else "a" if gut>=45 else "r"}" style="margin-top:10px;">{hm.get("hiring_manager_verdict","")}</div>', unsafe_allow_html=True)

    # ── COORDINATOR ──
    with t5:
        prob=coord.get("rejection_probability","High"); root=coord.get("root_cause_category","Multiple")
        app_v=coord.get("application_verdict","Apply After Fixes"); est=coord.get("estimated_success_after_fixes",0)
        comp2=coord.get("competitor_comparison",""); overall=coord.get("overall_score",0)
        enc=coord.get("encouragement",""); final=coord.get("final_verdict","")

        prob_c={"Very High":"#EF4444","High":"#EF4444","Medium":"#F59E0B","Low":"#10B981"}.get(prob,"#EF4444")
        root_c={"Skills Gap":"#EF4444","Experience Level":"#F59E0B","ATS Filtering":"#3B82F6","Narrative Clarity":"#8B5CF6","Multiple":"#EF4444"}.get(root,"#EF4444")
        av_c={"Apply Now":"#10B981","Apply After Fixes":"#F59E0B","Not Ready Yet":"#EF4444"}.get(app_v,"#F59E0B")
        av_icon={"Apply Now":"🎯","Apply After Fixes":"🔧","Not Ready Yet":"⏳"}.get(app_v,"🔧")
        emoji="💀" if prob in ("Very High","High") else "⚠" if prob=="Medium" else "✓"

        st.markdown(f'<div style="background:linear-gradient(135deg,#0A1628,#0D1219);border:1px solid {prob_c}25;border-left:4px solid {prob_c};border-radius:12px;padding:22px 26px;margin-bottom:18px;display:flex;align-items:center;gap:22px;flex-wrap:wrap;"><div style="font-size:42px;">{emoji}</div><div style="flex:1;min-width:200px;"><div style="font-family:JetBrains Mono,monospace;font-size:11px;color:{prob_c};text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;">{prob} REJECTION RISK</div><div style="font-size:13px;color:#94A3B8;line-height:1.6;">{coord.get("primary_rejection_reason","")}</div></div><div style="text-align:center;"><div style="font-family:JetBrains Mono,monospace;font-size:42px;font-weight:700;color:{_sc(overall)};line-height:1;">{overall}</div><div style="font-family:JetBrains Mono,monospace;font-size:9px;color:#64748B;">OVERALL /100</div><div style="margin-top:8px;font-size:22px;">{av_icon}</div><div style="font-family:JetBrains Mono,monospace;font-size:9px;color:{av_c};text-transform:uppercase;max-width:70px;">{app_v}</div></div></div>', unsafe_allow_html=True)

        rc1,rc2=st.columns([1.2,1],gap="medium")
        with rc1: st.markdown(f'<div class="card" style="border-left:3px solid {root_c};padding:14px 18px;"><div class="lbl">Root Cause Category</div><div style="font-family:JetBrains Mono,monospace;font-size:18px;font-weight:600;color:{root_c};margin:5px 0;">{root}</div></div>', unsafe_allow_html=True)
        with rc2: st.markdown(f'<div class="card" style="text-align:center;padding:14px;"><div class="lbl">After All Fixes</div><div style="font-family:JetBrains Mono,monospace;font-size:36px;font-weight:700;color:{_sc(est)};margin:6px 0;">{est}%</div><div style="font-size:9px;color:#64748B;">Estimated Pass Rate</div></div>', unsafe_allow_html=True)

        if comp2: st.markdown(f'<div class="al al-b">{comp2}</div>', unsafe_allow_html=True)

        gaps=coord.get("top_3_fixable_gaps",[])
        if gaps:
            st.markdown('<div class="sec">Top 3 Fixable Gaps</div>', unsafe_allow_html=True)
            for i,g in enumerate(gaps[:3],1):
                ec={"Days":"g","Weeks":"a","Months":"r"}.get(g.get("effort","Weeks"),"a")
                st.markdown(f'<div class="card" style="padding:13px 17px;margin-bottom:8px;"><div style="display:flex;align-items:flex-start;gap:11px;"><div style="background:linear-gradient(135deg,#10B981,#3B82F6);color:#080C14;width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:JetBrains Mono,monospace;font-size:11px;font-weight:600;flex-shrink:0;">#{i}</div><div style="flex:1;"><div style="display:flex;justify-content:space-between;margin-bottom:4px;"><span style="font-size:14px;font-weight:600;color:#E2E8F0;">{g.get("gap","")}</span><span class="chip chip-{ec}">{g.get("effort","")}</span></div><div style="font-size:12px;color:#64748B;margin-bottom:4px;">{g.get("impact","")}</div><div style="font-size:13px;color:#10B981;">→ {g.get("fix","")}</div></div></div></div>', unsafe_allow_html=True)

        qw=coord.get("quick_wins",[]); sec2=coord.get("secondary_rejection_reasons",[])
        if qw or sec2:
            wc1,wc2=st.columns(2,gap="medium")
            with wc1:
                if qw:
                    st.markdown('<div class="sec">⚡ Quick Wins</div>', unsafe_allow_html=True)
                    for w in qw: st.markdown(f'<div class="al al-g">⚡ {w}</div>', unsafe_allow_html=True)
            with wc2:
                if sec2:
                    st.markdown('<div class="sec">Secondary Reasons</div>', unsafe_allow_html=True)
                    for r in sec2: st.markdown(f'<div class="al al-a">⚠ {r}</div>', unsafe_allow_html=True)

        if final: st.markdown(f'<div class="al al-{"g" if overall>=70 else "a" if overall>=45 else "r"}" style="margin-top:8px;">{final}</div>', unsafe_allow_html=True)
        if enc: st.markdown(f'<div class="card" style="border-left:3px solid #10B981;padding:14px 18px;margin-top:8px;"><div class="lbl" style="color:#10B981;">💙 One Genuine Strength</div><div style="font-size:14px;color:#CBD5E1;font-style:italic;margin-top:6px;line-height:1.6;">"{enc}"</div></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# ROADMAP
# ══════════════════════════════════════════════════════
def render_roadmap(results):
    coord=results.get("coordinator",{})
    roadmap=coord.get("30_day_roadmap",coord.get("roadmap",[]))
    if not roadmap: return
    st.markdown('<div class="sec">30-Day Career Improvement Plan</div>', unsafe_allow_html=True)
    wc=["#10B981","#3B82F6","#F59E0B","#10B981"]
    for row in [roadmap[:2],roadmap[2:4]]:
        cols=st.columns(len(row),gap="medium")
        for col,week in zip(cols,row):
            wn=week.get("week",1); c=wc[(int(wn)-1)%4]
            acts="".join([f'<div style="font-size:12px;color:#64748B;padding:5px 0;border-bottom:1px solid #1E293B;line-height:1.4;">› {a}</div>' for a in week.get("actions",[])])
            sm_lbl=week.get("success_metric","")
            sm_html=f'<div style="font-size:11px;color:#10B981;margin-top:8px;padding-top:7px;border-top:1px solid #1E293B;">✓ Done when: {sm_lbl}</div>' if sm_lbl else ""
            with col: st.markdown(f'<div class="card" style="border-top:2px solid {c};padding:15px;"><div style="display:flex;align-items:center;gap:9px;margin-bottom:11px;"><div style="background:{c};color:#080C14;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-family:JetBrains Mono,monospace;font-size:11px;font-weight:600;">{wn}</div><div style="font-size:13px;font-weight:600;color:{c};">{week.get("theme","")}</div></div>{acts}{sm_html}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# DOWNLOAD
# ══════════════════════════════════════════════════════
def render_quick_tips(results):
    """Top 3 quick wins from coordinator — always visible at bottom."""
    coord = results.get("coordinator", {})
    wins  = coord.get("quick_wins", [])
    enc   = coord.get("encouragement", "")
    if not wins and not enc:
        return
    st.markdown('<div class="sec">⚡ Your Top Quick Wins</div>', unsafe_allow_html=True)
    if wins:
        for i, w in enumerate(wins[:3], 1):
            st.markdown(
                f'''<div style="display:flex;gap:10px;align-items:flex-start;
                            background:rgba(0,255,178,.04);border:1px solid rgba(0,255,178,.15);
                            border-radius:8px;padding:10px 14px;margin-bottom:6px;">
                  <div style="background:var(--green);color:#020810;border-radius:50%;
                              min-width:20px;height:20px;display:flex;align-items:center;
                              justify-content:center;font-family:JetBrains Mono,monospace;
                              font-size:10px;font-weight:700;flex-shrink:0;">{i}</div>
                  <div style="font-size:13px;color:#7FFFD4;line-height:1.5;">{w}</div>
                </div>''', unsafe_allow_html=True)
    if enc:
        st.markdown(
            f'<div class="card" style="border-left:3px solid var(--green);padding:14px 18px;">'
            f'<div class="lbl" style="color:var(--green);">💙 One Genuine Strength</div>'
            f'<div style="font-size:14px;color:#CBD5E1;font-style:italic;margin-top:6px;">&ldquo;{enc}&rdquo;</div>'
            f'</div>', unsafe_allow_html=True)


def render_download(results, company):
    st.markdown('<div class="sec">📥 Download Report</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="small")
    with c1:
        try:
            pdf = generate_pdf_report(results, company or "N/A")
            if pdf:
                st.download_button(
                    "⬇  Download PDF Report",
                    data=pdf,
                    file_name=f"HireLens_{(company or 'report').replace(' ','_')}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
        except Exception as e:
            st.warning(f"PDF: {e}")
    with c2:
        st.download_button(
            "⬇  Download JSON Data",
            data=json.dumps(results, indent=2, default=str).encode(),
            file_name="HireLens_data.json",
            mime="application/json",
            use_container_width=True,
        )
    with c3:
        # Generate a shareable text summary for clipboard
        coord   = results.get("coordinator", {})
        ats     = results.get("ats", {})
        summary = (
            f"HireLens AI Analysis\n"
            f"Company: {company or 'N/A'}\n"
            f"Overall Score: {coord.get('overall_score', 0)}/100\n"
            f"ATS Score: {ats.get('ats_score', 0)}/100\n"
            f"Rejection Risk: {coord.get('rejection_probability', 'N/A')}\n"
            f"Verdict: {coord.get('application_verdict', 'N/A')}\n"
            f"Root Cause: {coord.get('root_cause_category', 'N/A')}\n"
            f"Primary Issue: {coord.get('primary_rejection_reason', '')[:100]}\n"
        )
        st.download_button(
            "📋  Copy Summary",
            data=summary.encode(),
            file_name="HireLens_summary.txt",
            mime="text/plain",
            use_container_width=True,
        )




# ══════════════════════════════════════════════════════
# ANALYTICS — SECTION SCORER
# ══════════════════════════════════════════════════════
def render_section_scores(results, resume_text=""):
    if not HAS_SECTION_SCORER:
        st.info("Section scorer unavailable.")
        return
    try:
        scores = compute_all_section_scores(results, resume_text)
    except Exception as e:
        st.error(f"Section scorer error: {e}")
        return
    st.markdown('<div class="sec">Resume Section Scores</div>', unsafe_allow_html=True)
    cols = st.columns(len(scores), gap="small")
    for col, s in zip(cols, scores):
        with col:
            st.markdown(
                f'''<div class="card" style="text-align:center;padding:16px 10px;">
                  <div class="lbl">{s.name}</div>
                  <div style="font-family:JetBrains Mono,monospace;font-size:28px;font-weight:700;
                              color:{s.color};margin:8px 0;">{s.score}</div>
                  <div style="font-size:20px;font-weight:700;color:{s.color};opacity:.6;">{s.grade}</div>
                  <div style="background:#1E293B;border-radius:3px;height:4px;margin:8px 4px 0;">
                    <div style="width:{s.score}%;height:100%;background:{s.color};border-radius:3px;"></div>
                  </div>
                </div>''', unsafe_allow_html=True)
    for s in scores:
        with st.expander(f"📋 {s.name} — Detail"):
            ec1, ec2 = st.columns(2, gap="medium")
            with ec1:
                if s.strengths:
                    st.markdown('<div class="sec" style="margin-top:0;">Strengths</div>', unsafe_allow_html=True)
                    for item in s.strengths:
                        st.markdown(f'<div class="al al-g">✓ {item}</div>', unsafe_allow_html=True)
            with ec2:
                if s.weaknesses:
                    st.markdown('<div class="sec" style="margin-top:0;">Weaknesses</div>', unsafe_allow_html=True)
                    for item in s.weaknesses:
                        st.markdown(f'<div class="al al-r">✗ {item}</div>', unsafe_allow_html=True)
            if s.sub_scores:
                st.markdown('<div class="sec">Sub-Scores</div>', unsafe_allow_html=True)
                for k, v in s.sub_scores.items():
                    c = _sc(v)
                    st.markdown(
                        f'''<div style="margin-bottom:8px;">
                          <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                            <span style="font-size:12px;color:#94A3B8;">{k}</span>
                            <span style="font-family:JetBrains Mono,monospace;font-size:11px;color:{c};">{v}</span>
                          </div>
                          <div style="background:#1E293B;border-radius:3px;height:4px;">
                            <div style="width:{v}%;height:100%;background:{c};border-radius:3px;"></div>
                          </div>
                        </div>''', unsafe_allow_html=True)
            if s.tip:
                st.markdown(f'<div class="al al-b">💡 {s.tip}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# ANALYTICS — RECRUITER SIMULATOR
# ══════════════════════════════════════════════════════
def render_recruiter_simulator(results):
    if not HAS_RECRUITER:
        st.info("Recruiter simulator unavailable.")
        return
    try:
        decision = simulate_recruiter_decision(results)
    except Exception as e:
        st.error(f"Recruiter simulator error: {e}")
        return

    dc = decision.decision_color
    st.markdown(
        f'''<div style="background:linear-gradient(135deg,#0A1628,#0D1219);
                    border:2px solid {dc}30;border-left:4px solid {dc};
                    border-radius:12px;padding:24px 28px;margin-bottom:18px;
                    display:flex;align-items:center;gap:24px;flex-wrap:wrap;">
          <div style="font-family:JetBrains Mono,monospace;font-size:56px;font-weight:800;
                      color:{dc};line-height:1;">{decision.shortlist_pct}%</div>
          <div style="flex:1;min-width:200px;">
            <div style="font-family:JetBrains Mono,monospace;font-size:11px;color:{dc};
                        text-transform:uppercase;letter-spacing:2px;margin-bottom:6px;">
              {decision.decision} · {decision.confidence} CONFIDENCE</div>
            <div style="font-size:13px;color:#94A3B8;">Shortlist probability based on weighted signal analysis</div>
          </div>
        </div>''', unsafe_allow_html=True)

    st.markdown('<div class="sec">Signal Breakdown</div>', unsafe_allow_html=True)
    for sig in decision.signals:
        vc = _sc(sig.raw_score)
        pct = sig.raw_score
        st.markdown(
            f'''<div style="margin-bottom:10px;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:3px;">
                <div>
                  <span style="font-size:12px;color:#E2E8F0;">{sig.name}</span>
                  <span style="font-size:10px;color:#475569;margin-left:8px;">weight: {int(sig.weight*100)}%</span>
                </div>
                <span style="font-family:JetBrains Mono,monospace;font-size:11px;color:{vc};">{sig.raw_score}</span>
              </div>
              <div style="background:#1E293B;border-radius:3px;height:5px;">
                <div style="width:{pct}%;height:100%;background:{vc};border-radius:3px;"></div>
              </div>
              <div style="font-size:10px;color:#475569;margin-top:2px;">{sig.reason}</div>
            </div>''', unsafe_allow_html=True)

    rc1, rc2 = st.columns(2, gap="medium")
    with rc1:
        if decision.top_positive:
            st.markdown('<div class="sec">Positive Signals</div>', unsafe_allow_html=True)
            for p in decision.top_positive:
                st.markdown(f'<div class="al al-g">✓ {p}</div>', unsafe_allow_html=True)
    with rc2:
        if decision.top_negative:
            st.markdown('<div class="sec">Risk Signals</div>', unsafe_allow_html=True)
            for n in decision.top_negative:
                st.markdown(f'<div class="al al-r">✗ {n}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sec">Stage-by-Stage Probability</div>', unsafe_allow_html=True)
    scols = st.columns(len(decision.stage_breakdown), gap="small")
    for col, (stage, pct) in zip(scols, decision.stage_breakdown.items()):
        with col:
            c = _sc(pct)
            st.markdown(
                f'''<div class="card" style="text-align:center;padding:12px 8px;">
                  <div class="lbl" style="font-size:9px;">{stage}</div>
                  <div style="font-family:JetBrains Mono,monospace;font-size:20px;font-weight:700;
                              color:{c};margin-top:6px;">{pct}%</div>
                </div>''', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# ANALYTICS — MULTI-AGENT vs SINGLE AI COMPARISON
# ══════════════════════════════════════════════════════
def render_comparison(results):
    if not HAS_COMPARISON:
        st.info("Comparison unavailable.")
        return
    try:
        report = run_comparison(results)
    except Exception as e:
        st.error(f"Comparison error: {e}")
        return

    cc1, cc2, cc3 = st.columns(3, gap="medium")
    with cc1:
        st.markdown(
            f'''<div class="card card-g" style="text-align:center;padding:18px;">
              <div class="lbl">Multi-Agent Score</div>
              <div style="font-family:JetBrains Mono,monospace;font-size:40px;font-weight:800;
                          color:#10B981;">{report.overall_multi}</div>
            </div>''', unsafe_allow_html=True)
    with cc2:
        st.markdown(
            f'''<div class="card card-r" style="text-align:center;padding:18px;">
              <div class="lbl">Single AI Score</div>
              <div style="font-family:JetBrains Mono,monospace;font-size:40px;font-weight:800;
                          color:#EF4444;">{report.overall_single}</div>
            </div>''', unsafe_allow_html=True)
    with cc3:
        st.markdown(
            f'''<div class="card card-b" style="text-align:center;padding:18px;">
              <div class="lbl">Advantage</div>
              <div style="font-family:JetBrains Mono,monospace;font-size:40px;font-weight:800;
                          color:#3D9BFF;">+{report.total_delta}</div>
            </div>''', unsafe_allow_html=True)

    st.markdown(f'<div class="al al-b" style="margin:14px 0;">{report.verdict}</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec">Dimension Comparison</div>', unsafe_allow_html=True)
    for dim in report.dimensions:
        delta_c = "#10B981" if dim.delta > 0 else "#94A3B8"
        st.markdown(
            f'''<div class="card" style="padding:14px 18px;margin-bottom:8px;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span style="font-size:13px;font-weight:600;color:#E2E8F0;">{dim.name}</span>
                <span style="font-family:JetBrains Mono,monospace;font-size:11px;
                             color:{delta_c};">+{dim.delta} pts</span>
              </div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                <div>
                  <div style="font-size:10px;color:#10B981;text-transform:uppercase;letter-spacing:1px;
                               margin-bottom:3px;">Multi-Agent</div>
                  <div style="background:#1E293B;border-radius:3px;height:4px;margin-bottom:4px;">
                    <div style="width:{dim.multi_agent_score}%;height:100%;background:#10B981;border-radius:3px;"></div>
                  </div>
                  <div style="font-size:11px;color:#64748B;line-height:1.4;">{dim.multi_agent_detail[:80]}...</div>
                </div>
                <div>
                  <div style="font-size:10px;color:#EF4444;text-transform:uppercase;letter-spacing:1px;
                               margin-bottom:3px;">Single AI</div>
                  <div style="background:#1E293B;border-radius:3px;height:4px;margin-bottom:4px;">
                    <div style="width:{dim.single_ai_score}%;height:100%;background:#EF4444;border-radius:3px;"></div>
                  </div>
                  <div style="font-size:11px;color:#64748B;line-height:1.4;">{dim.single_ai_detail[:80]}...</div>
                </div>
              </div>
            </div>''', unsafe_allow_html=True)

    if report.unique_insights:
        st.markdown('<div class="sec">Unique Insights (Multi-Agent Only)</div>', unsafe_allow_html=True)
        for insight in report.unique_insights:
            st.markdown(f'<div class="al al-g">🔬 {insight}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# ANALYTICS — INTERVIEW PREDICTOR
# ══════════════════════════════════════════════════════
def render_interview_predictor(results):
    if not HAS_INTERVIEW:
        st.info("Interview predictor unavailable.")
        return
    try:
        pred = predict_interview_questions(results)
    except Exception as e:
        render_friendly_error(e, "interview prediction")
        return

    if pred.focus_areas:
        st.markdown('<div class="sec">Predicted Focus Areas</div>', unsafe_allow_html=True)
        st.markdown(" ".join(
            f'<span class="chip chip-b">{fa}</span>' for fa in pred.focus_areas
        ), unsafe_allow_html=True)

    # ── Filters ─────────────────────────────────────────────
    all_cats  = sorted(set(q.category  for q in pred.questions))
    all_diffs = sorted(set(q.difficulty for q in pred.questions),
                       key=lambda d: {"Easy":0,"Medium":1,"Hard":2}.get(d,1))

    fc1, fc2, fc3 = st.columns([2, 2, 1], gap="small")
    with fc1:
        cat_filter = st.multiselect(
            "Filter by category", options=all_cats, default=all_cats,
            key="ip_cat_filter", label_visibility="collapsed",
            placeholder="All categories",
        )
    with fc2:
        diff_filter = st.multiselect(
            "Filter by difficulty", options=all_diffs, default=all_diffs,
            key="ip_diff_filter", label_visibility="collapsed",
            placeholder="All difficulties",
        )
    with fc3:
        show_traps = st.toggle("Show traps", value=True, key="ip_traps")

    filtered = [q for q in pred.questions
                if q.category  in (cat_filter  or all_cats)
                and q.difficulty in (diff_filter or all_diffs)]

    st.markdown(
        f'<div style="font-size:11px;color:var(--muted);margin:8px 0 12px;">' +
        f'Showing {len(filtered)} of {len(pred.questions)} questions' +
        '</div>', unsafe_allow_html=True)

    cat_colors  = {"Technical":"r","Behavioural":"a","Situational":"b","Culture":"v","Gap Defence":"r"}
    diff_colors = {"Hard":"#EF4444","Medium":"#F59E0B","Easy":"#10B981"}

    for i, q in enumerate(filtered, 1):
        cat_c  = cat_colors.get(q.category, "b")
        diff_c = diff_colors.get(q.difficulty, "#94A3B8")
        trap_html = (
            f'<div style="margin-top:8px;padding:8px 12px;background:#1A0505;' +
            f'border-left:2px solid #EF4444;border-radius:4px;font-size:11px;color:#FCA5A5;">' +
            f'⚠ Trap: {q.trap}</div>'
        ) if q.trap and show_traps else ""
        st.markdown(f'''
        <div class="card" style="padding:16px 18px;margin-bottom:10px;">
          <div style="display:flex;gap:8px;align-items:center;margin-bottom:10px;">
            <div style="background:linear-gradient(135deg,#10B981,#3D9BFF);color:#080C14;
                        width:22px;height:22px;border-radius:50%;display:flex;align-items:center;
                        justify-content:center;font-family:JetBrains Mono,monospace;
                        font-size:10px;font-weight:600;flex-shrink:0;">Q{i}</div>
            <span class="chip chip-{cat_c}" style="font-size:9px;">{q.category}</span>
            <span style="font-family:JetBrains Mono,monospace;font-size:9px;color:{diff_c};">{q.difficulty}</span>
          </div>
          <div style="font-size:14px;font-weight:600;color:#E2E8F0;line-height:1.5;margin-bottom:10px;">
            &ldquo;{q.question}&rdquo;
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
            <div>
              <div style="font-size:10px;color:#94A3B8;text-transform:uppercase;
                          letter-spacing:1px;margin-bottom:4px;">Why asked</div>
              <div style="font-size:12px;color:#64748B;line-height:1.5;">{q.why_asked}</div>
            </div>
            <div>
              <div style="font-size:10px;color:#10B981;text-transform:uppercase;
                          letter-spacing:1px;margin-bottom:4px;">How to nail it</div>
              <div style="font-size:12px;color:#7FFFD4;line-height:1.5;">{q.strong_answer_tip}</div>
            </div>
          </div>
          {trap_html}
        </div>''', unsafe_allow_html=True)

    if pred.prep_priorities:
        st.markdown('<div class="sec">Prep Priorities</div>', unsafe_allow_html=True)
        for p in pred.prep_priorities:
            st.markdown(f'<div class="al al-a">→ {p}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# ANALYTICS — COVER LETTER GENERATOR
# ══════════════════════════════════════════════════════
def render_cover_letter(results, resume_text="", jd="", company=""):
    if not HAS_COVER_LETTER:
        st.info("Cover letter generator unavailable.")
        return

    tone = st.selectbox(
        "Tone",
        ["Confident", "Professional", "Direct"],
        key="cover_tone",
        label_visibility="collapsed",
    )

    # ── Cache key: regenerate only when tone or run_id changes ──
    cache_key = f"cl_{st.session_state.get('run_id','')}{tone}"
    cached_cl = st.session_state.get("cl_cache_key") == cache_key

    col_gen, col_clear = st.columns([2, 1], gap="small")
    with col_gen:
        gen_clicked = st.button("✍  Generate Cover Letter", use_container_width=True)
    with col_clear:
        if st.session_state.get("cl_result") and st.button("🗑  Clear", use_container_width=True):
            st.session_state.pop("cl_result", None)
            st.session_state.pop("cl_cache_key", None)
            st.rerun()

    if gen_clicked and not (cached_cl and st.session_state.get("cl_result")):
        with st.spinner("Generating cover letter…"):
            try:
                cl = generate_cover_letter(resume_text, jd, company, results, tone=tone)
                st.session_state["cl_result"]    = cl
                st.session_state["cl_cache_key"] = cache_key
            except Exception as e:
                st.error(f"Cover letter error: {e}")
                return

    cl = st.session_state.get("cl_result")
    if cl:
        st.markdown('<div class="sec">Generated Cover Letter</div>', unsafe_allow_html=True)
        word_c = "#10B981" if 150 <= cl.word_count <= 400 else "#F59E0B"
        st.markdown(
            f'''<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <div style="font-family:JetBrains Mono,monospace;font-size:10px;color:#64748B;">
                Tone: {cl.tone}
              </div>
              <div style="font-family:JetBrains Mono,monospace;font-size:10px;color:{word_c};">
                {cl.word_count} words
              </div>
            </div>''', unsafe_allow_html=True)
        st.markdown(
            f'''<div class="card" style="padding:22px 26px;white-space:pre-wrap;
                        font-family:Space Grotesk,sans-serif;font-size:13px;
                        color:#CBD5E1;line-height:1.85;">{cl.content}</div>''',
            unsafe_allow_html=True)
        if cl.key_signals_used:
            st.markdown(
                '<div style="margin-top:6px;font-size:11px;color:#475569;">Signals used: ' +
                ", ".join(cl.key_signals_used[:3]) + '</div>', unsafe_allow_html=True)
        dc1, dc2 = st.columns(2, gap="small")
        with dc1:
            st.download_button(
                "⬇  Download .txt",
                data=cl.content.encode(),
                file_name=f"CoverLetter_{(company or 'Application').replace(' ','_')}.txt",
                mime="text/plain",
                use_container_width=True,
            )
        with dc2:
            st.download_button(
                "📋  Copy as Text",
                data=cl.content.encode(),
                file_name="cover_letter_copy.txt",
                mime="text/plain",
                use_container_width=True,
            )
    elif not gen_clicked:
        st.markdown(
            '''<div class="al al-b" style="margin-top:6px;">
              Select a tone above and click <b>Generate Cover Letter</b>.<br>
              <span style="font-size:11px;color:#64748B;">
                Generated letters are cached — switching tabs won't lose your result.
              </span>
            </div>''', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# ANALYTICS — BULLET IMPROVER
# ══════════════════════════════════════════════════════
def render_bullet_improver(results):
    if not HAS_BULLET_IMPROVER:
        st.info("Bullet improver unavailable.")
        return

    bullets = extract_bullets_from_result(results) if results else []
    if not bullets:
        st.markdown('<div class="al al-a">No bullet excerpts found. Run a full analysis first.</div>', unsafe_allow_html=True)
        return

    # ── Cache key tied to run_id ─────────────────────────────────
    run_cache_key = f"bi_{st.session_state.get('run_id', '')}"
    improvements  = st.session_state.get("bi_result") if st.session_state.get("bi_cache_key") == run_cache_key else None

    if not improvements:
        st.markdown(
            f'''<div class="al al-b">
              Found <b>{len(bullets)}</b> resume bullet excerpts.
              <span style="font-size:11px;color:#64748B;display:block;margin-top:3px;">
                Results are cached for this analysis — clicking again won't re-run.
              </span>
            </div>''', unsafe_allow_html=True)

    bc1, bc2 = st.columns([2, 1], gap="small")
    with bc1:
        run_clicked = st.button("⚡  Improve All Bullets", use_container_width=True, disabled=bool(improvements))
    with bc2:
        if improvements and st.button("🔄  Re-run", use_container_width=True):
            st.session_state.pop("bi_result", None)
            st.session_state.pop("bi_cache_key", None)
            st.rerun()

    if run_clicked:
        with st.spinner("Analysing and rewriting bullets…"):
            try:
                improvements = improve_bullets(
                    bullets,
                    use_ai=bool(os.environ.get("ANTHROPIC_API_KEY"))
                )
                st.session_state["bi_result"]    = improvements
                st.session_state["bi_cache_key"] = run_cache_key
            except Exception as e:
                st.error(f"Bullet improver error: {e}")
                return

    if improvements:
        total_delta = sum(i.impact_delta for i in improvements)
        st.markdown('<div class="sec">Improved Bullets</div>', unsafe_allow_html=True)
        st.markdown(
            f'''<div style="display:flex;gap:12px;align-items:center;margin-bottom:12px;flex-wrap:wrap;">
              <div class="al al-g" style="flex:1;margin:0;">
                ✨ Estimated improvement: <b>+{total_delta} pts</b> across {len(improvements)} bullets
              </div>
            </div>''', unsafe_allow_html=True)

        # Export all rewrites as text
        export_text = "\n\n".join(
            f"BEFORE: {imp.original}\nAFTER:  {imp.improved}\nCHANGES: {'; '.join(imp.changes)}"
            for imp in improvements
        )
        st.download_button(
            "⬇  Export All Rewrites (.txt)",
            data=export_text.encode(),
            file_name="HireLens_BulletRewrites.txt",
            mime="text/plain",
        )

        for imp in improvements:
            st.markdown(
                f'''<div class="card" style="border-left:3px solid #10B981;padding:14px 18px;margin-bottom:8px;">
                  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:10px;">
                    <div>
                      <div class="lbl" style="color:#EF4444;margin-bottom:5px;">✗ Before</div>
                      <div style="font-size:13px;color:#94A3B8;font-style:italic;line-height:1.5;">"{imp.original[:100]}"</div>
                    </div>
                    <div>
                      <div class="lbl" style="color:#10B981;margin-bottom:5px;">✓ After</div>
                      <div style="font-size:13px;color:#7FFFD4;font-style:italic;line-height:1.5;">"{imp.improved[:100]}"</div>
                    </div>
                  </div>
                  <div style="display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding-top:8px;
                               border-top:1px solid var(--border);">
                    {" ".join(f'<span class="chip chip-b" style="font-size:9px;">{c}</span>' for c in imp.changes[:3])}
                    <span style="font-family:JetBrains Mono,monospace;font-size:11px;
                                 color:#10B981;margin-left:auto;font-weight:600;">+{imp.impact_delta} pts</span>
                  </div>
                </div>''', unsafe_allow_html=True)
    elif not run_clicked:
        st.markdown('<div class="lbl">Click above to analyse and rewrite your resume bullets with AI.</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# NEW: SCORE HISTORY PANEL
# ══════════════════════════════════════════════════════
def render_score_history():
    history = st.session_state.get("score_history", [])
    if len(history) < 2:
        return  # Need at least 2 runs to be useful
    st.markdown('<div class="sec">📈 Score History — This Session</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="font-size:11px;color:var(--muted);margin-bottom:10px;">' +
        f'Tracking {len(history)} analys{"es" if len(history)>1 else "is"} — upload a revised resume to see improvement.' +
        '</div>', unsafe_allow_html=True)
    cols = st.columns(len(history), gap="small")
    metrics = [("Overall", "overall"), ("ATS", "ats"), ("Skills", "skills"), ("Exp", "experience"), ("HM", "hm")]
    for col, run in zip(cols, history):
        with col:
            ov = run["overall"]
            c  = _sc(ov)
            co = run.get("company", "?")[:12]
            ts = run.get("timestamp", "")
            rows = "".join(
                f'<div style="display:flex;justify-content:space-between;padding:3px 0;'
                f'border-bottom:1px solid var(--border);">' +
                f'<span style="font-size:10px;color:var(--muted);">{lbl}</span>' +
                f'<span style="font-family:JetBrains Mono,monospace;font-size:10px;color:{_sc(run[key])};">{run[key]}</span>' +
                f'</div>'
                for lbl, key in metrics
            )
            st.markdown(f'''
            <div class="card" style="padding:12px;text-align:center;">
              <div style="font-family:JetBrains Mono,monospace;font-size:9px;
                          color:var(--muted);margin-bottom:4px;">{ts} · {co}</div>
              <div style="font-family:Outfit,sans-serif;font-size:28px;
                          font-weight:800;color:{c};line-height:1;">{ov}</div>
              <div style="font-size:8px;color:var(--muted);margin-bottom:8px;">Overall</div>
              {rows}
            </div>''', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# NEW: JD QUICK SCAN (no API call)
# ══════════════════════════════════════════════════════
def render_jd_quick_scan(jd_text: str):
    """Instant JD keyword extraction — runs before agents, costs nothing."""
    if not jd_text or len(jd_text.strip()) < 30:
        return
    import re as _re

    # Extract tech keywords and requirements
    tech_pattern = _re.compile(
        r'\b(Python|Java|JavaScript|TypeScript|Go|Rust|C\+\+|SQL|NoSQL|'
        r'React|Vue|Angular|Node\.?js|Django|FastAPI|Flask|Spring|'
        r'AWS|GCP|Azure|Docker|Kubernetes|Terraform|Helm|'
        r'PostgreSQL|MySQL|MongoDB|Redis|Elasticsearch|Kafka|'
        r'Machine Learning|Deep Learning|TensorFlow|PyTorch|'
        r'CI/CD|Git|GitHub|GitLab|Jenkins|REST|GraphQL|gRPC|'
        r'Microservices|Agile|Scrum|DevOps|MLOps|Linux|'
        r'Prometheus|Grafana|Datadog|Splunk)\b',
        _re.IGNORECASE
    )
    years_pattern = _re.compile(r'(\d+)\+?\s*(?:years?|yrs?)\s+(?:of\s+)?experience', _re.IGNORECASE)
    level_pattern = _re.compile(r'\b(Junior|Mid|Senior|Staff|Principal|Lead|Director|VP|Head of)\b', _re.IGNORECASE)

    techs  = list(dict.fromkeys(m.group() for m in tech_pattern.finditer(jd_text)))[:18]
    years  = years_pattern.findall(jd_text)
    levels = list(dict.fromkeys(m.group() for m in level_pattern.finditer(jd_text)))[:4]

    if not techs and not years:
        return

    with st.expander("🔍 JD Quick Scan — Keywords & Requirements", expanded=False):
        sc1, sc2, sc3 = st.columns(3, gap="medium")
        with sc1:
            st.markdown('<div class="lbl" style="color:var(--green);">Tech Keywords</div>', unsafe_allow_html=True)
            if techs:
                st.markdown(" ".join(
                    f'<span class="chip chip-g" style="font-size:9px;">{t}</span>' for t in techs
                ), unsafe_allow_html=True)
            else:
                st.markdown('<span style="font-size:11px;color:var(--muted);">None detected</span>', unsafe_allow_html=True)
        with sc2:
            st.markdown('<div class="lbl" style="color:var(--amber);">Experience Required</div>', unsafe_allow_html=True)
            if years:
                for y in list(dict.fromkeys(years))[:3]:
                    st.markdown(
                        f'<div style="font-family:JetBrains Mono,monospace;font-size:18px;'
                        f'font-weight:700;color:var(--amber);">{y}+ yrs</div>',
                        unsafe_allow_html=True)
            else:
                st.markdown('<span style="font-size:11px;color:var(--muted);">Not specified</span>', unsafe_allow_html=True)
        with sc3:
            st.markdown('<div class="lbl" style="color:var(--blue);">Seniority Signals</div>', unsafe_allow_html=True)
            if levels:
                st.markdown(" ".join(
                    f'<span class="chip chip-b" style="font-size:9px;">{l}</span>' for l in levels
                ), unsafe_allow_html=True)
            else:
                st.markdown('<span style="font-size:11px;color:var(--muted);">Not specified</span>', unsafe_allow_html=True)
        st.markdown(
            f'<div style="margin-top:8px;font-size:11px;color:var(--muted);">' +
            f'⚡ {len(techs)} tech keywords extracted · Add matching ones to your Skills section before running analysis' +
            '</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# NEW: RESUME PREVIEW PANEL
# ══════════════════════════════════════════════════════
def render_resume_preview(resume_text: str):
    """Show parsed resume text so user can verify extraction quality."""
    if not resume_text or len(resume_text.strip()) < 20:
        return
    lines = [l for l in resume_text.splitlines() if l.strip()]
    word_count = len(resume_text.split())
    char_count = len(resume_text)
    with st.expander(f"📄 Parsed Resume Preview — {word_count} words, {char_count} chars", expanded=False):
        if word_count < 100:
            st.markdown(
                '<div class="al al-r">⚠ Very short — only ' + str(word_count) + ' words extracted. ' +
                'This PDF may be image-based or have copy protection. Try exporting as a text-based PDF.</div>',
                unsafe_allow_html=True)
        elif word_count < 200:
            st.markdown(
                '<div class="al al-a">⚠ Short extract (' + str(word_count) + ' words). Some content may not have been parsed.</div>',
                unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="al al-g">✓ ' + str(word_count) + ' words extracted successfully.</div>',
                unsafe_allow_html=True)
        preview = "\n".join(lines[:40])
        if len(lines) > 40:
            preview += f"\n... ({len(lines)-40} more lines)"
        st.code(preview, language=None)


# ══════════════════════════════════════════════════════
# NEW: ATS WHAT-IF SIMULATOR
# ══════════════════════════════════════════════════════
def render_ats_whatif(results):
    """Let user toggle keyword additions and see predicted ATS score."""
    ats = results.get("ats", {})
    missing = ats.get("missing_keywords", [])
    if not missing:
        st.info("No missing keywords to simulate.")
        return

    current_score   = ats.get("ats_score", 0)
    keyword_density = ats.get("keyword_density_pct", 0)
    total_missing   = len(missing)

    st.markdown(
        f'''<div class="card card-b" style="padding:16px 20px;margin-bottom:14px;">
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div>
              <div class="lbl">Current ATS Score</div>
              <div style="font-family:JetBrains Mono,monospace;font-size:36px;
                          font-weight:800;color:{_sc(current_score)};">{current_score}</div>
            </div>
            <div style="text-align:right;">
              <div class="lbl">Keyword Density</div>
              <div style="font-family:JetBrains Mono,monospace;font-size:24px;
                          font-weight:700;color:var(--blue);">{keyword_density}%</div>
            </div>
          </div>
        </div>''', unsafe_allow_html=True)

    st.markdown('<div class="lbl" style="margin-bottom:8px;">Select keywords you would add to your resume:</div>', unsafe_allow_html=True)

    # Checkbox grid for missing keywords
    selected = []
    n_cols = min(3, max(1, len(missing) // 3 + 1))
    check_cols = st.columns(n_cols, gap="small")
    for i, kw in enumerate(missing[:15]):
        with check_cols[i % n_cols]:
            if st.checkbox(kw, key=f"whatif_{kw}"):
                selected.append(kw)

    # Predict new score
    if selected:
        # Each added keyword boosts density by roughly (100/total_jd_keywords)
        # Estimate: each missing keyword is worth ~2-4 score points
        gain_per_kw = max(1, min(4, 40 // max(total_missing, 1)))
        predicted   = min(100, current_score + len(selected) * gain_per_kw)
        delta       = predicted - current_score
        delta_c     = "#10B981" if delta > 0 else "#94A3B8"
        st.markdown(
            f'''<div style="display:flex;align-items:center;gap:16px;
                         background:rgba(0,255,178,.05);border:1px solid rgba(0,255,178,.2);
                         border-radius:12px;padding:16px 20px;margin-top:12px;">
              <div style="text-align:center;">
                <div class="lbl">Predicted Score</div>
                <div style="font-family:JetBrains Mono,monospace;font-size:40px;
                            font-weight:800;color:{_sc(predicted)};">{predicted}</div>
              </div>
              <div style="font-size:28px;">→</div>
              <div>
                <div style="font-family:JetBrains Mono,monospace;font-size:18px;
                            font-weight:700;color:{delta_c};">+{delta} pts</div>
                <div style="font-size:12px;color:var(--muted);margin-top:4px;">
                  Add: {", ".join(selected[:5])}{"..." if len(selected)>5 else ""}
                </div>
                <div style="font-size:11px;color:var(--muted);margin-top:2px;">
                  to your Skills section and at least one bullet point
                </div>
              </div>
            </div>''', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div style="font-size:12px;color:var(--muted);margin-top:8px;font-style:italic;">' +
            'Check keywords above to simulate your improved ATS score.' +
            '</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# NEW: FRIENDLY ERROR HELPER
# ══════════════════════════════════════════════════════
def render_friendly_error(e: Exception, context: str = "analysis"):
    """Convert raw exceptions into user-friendly guidance."""
    err_str = str(e).lower()
    if "api_key" in err_str or "authentication" in err_str or "unauthorized" in err_str:
        msg = "🔑 **API key issue** — Your API key appears to be invalid or missing. Check your `.env` file and make sure `ANTHROPIC_API_KEY` is set correctly."
        cls = "al-r"
    elif "rate" in err_str or "quota" in err_str or "429" in err_str:
        msg = "⏱ **Rate limit hit** — Too many requests. Wait 30 seconds and try again. Consider switching to a lower-tier model in `.env`."
        cls = "al-a"
    elif "timeout" in err_str or "timed out" in err_str:
        msg = "⌛ **Timeout** — The analysis took too long. This can happen on slow connections. Try again — it usually works on the second attempt."
        cls = "al-a"
    elif "pdf" in err_str or "extract" in err_str:
        msg = "📄 **PDF parsing failed** — Make sure your PDF is text-based (not a scanned image). Export from Word/Google Docs for best results."
        cls = "al-r"
    elif "connection" in err_str or "network" in err_str or "resolve" in err_str:
        msg = "🌐 **Network error** — Could not reach the AI provider. Check your internet connection and try again."
        cls = "al-r"
    else:
        msg = f"❌ **{context.title()} failed** — An unexpected error occurred. Try again, or check the error details below."
        cls = "al-r"

    st.markdown(f'<div class="al {cls}">{msg}</div>', unsafe_allow_html=True)
    with st.expander("🔧 Technical details (for debugging)"):
        st.exception(e)


# ══════════════════════════════════════════════════════
# NEW: PER-SCORE MICRO TIPS
# ══════════════════════════════════════════════════════
def render_score_micro_tips(results):
    """Show the single highest-impact fix below each score."""
    ats   = results.get("ats", {})
    sk    = results.get("skills", {})
    exp   = results.get("experience", {})
    hm    = results.get("hiring_manager", {})
    coord = results.get("coordinator", {})

    tips = []
    # ATS tip
    ats_fixes = ats.get("quick_ats_fixes", [])
    if ats_fixes:
        tips.append(("ATS", _sc(ats.get("ats_score", 0)), ats_fixes[0]))
    # Skills tip
    missing_crit = sk.get("missing_critical", [])
    if missing_crit:
        top_gap = missing_crit[0]
        tips.append(("Skills", _sc(sk.get("match_score", 0)),
                     f"Add {top_gap.get('skill','missing skill')} — {top_gap.get('why_it_matters','')[:60]}"))
    # Experience tip
    bullets = exp.get("bullet_quality", [])
    if bullets:
        tips.append(("Experience", _sc(exp.get("experience_score", 0)),
                     bullets[0].get("fix", "Rewrite weakest bullet with a quantified metric")))
    # Quick win
    qw = coord.get("quick_wins", [])
    if qw:
        tips.append(("Quick Win", "#10B981", qw[0]))

    if not tips:
        return

    st.markdown('<div class="sec">💡 Highest-Impact Fixes</div>', unsafe_allow_html=True)
    tip_cols = st.columns(len(tips), gap="small")
    for col, (label, color, tip) in zip(tip_cols, tips):
        with col:
            st.markdown(f'''
            <div class="card" style="padding:12px 14px;border-left:3px solid {color};">
              <div style="font-family:JetBrains Mono,monospace;font-size:9px;
                          color:{color};text-transform:uppercase;letter-spacing:1.2px;
                          margin-bottom:6px;">{label}</div>
              <div style="font-size:12px;color:#CBD5E1;line-height:1.5;">{tip[:100]}</div>
            </div>''', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# EMPTY STATE
# ══════════════════════════════════════════════════════
def render_empty():
    features = [
        ("#00FFB2", "ATS Compliance",    "Keyword audit, format scan and section scoring"),
        ("#3D9BFF", "Skills Gap",         "Evidence-based mapping with learn-time estimates"),
        ("#A78BFA", "Experience Audit",   "Bullet-level STAR critique with AI rewrites"),
        ("#F5A623", "Hiring Manager Sim", "Simulates VP decision from 6-second scan to offer"),
        ("#22D3EE", "Root Cause",         "All agents synthesised into a ranked action plan"),
        ("#FF3D6B", "ATS What-If",        "Toggle missing keywords, see predicted score change"),
        ("#9D7FFF", "Interview Prep",     "Questions filtered by category and difficulty"),
        ("#00FFB2", "Cover Letter",       "AI-generated in 3 tones, cached per run"),
        ("#F5A623", "Bullet Rewriter",    "Weak verbs upgraded and metrics added"),
        ("#3D9BFF", "Score History",      "Track last 5 analyses and compare versions"),
        ("#FF3D6B", "Recruiter Sim",      "Shortlist probability with signal breakdown"),
    ]

    cards = ""
    for i, (color, title, desc) in enumerate(features):
        delay = "{:.2f}s".format(i * 0.04)
        cards += (
            "<div style='background:linear-gradient(145deg,rgba(255,255,255,.04),rgba(255,255,255,.015));"
            "border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:16px 14px;"
            "transition:all .2s ease;cursor:default;position:relative;overflow:hidden;"
            "animation:fadeInUp .4s ease " + delay + " both;'>"
            "<div style='position:absolute;top:0;left:0;right:0;height:2px;"
            "background:linear-gradient(90deg,transparent," + color + "55,transparent);'></div>"
            "<div style='font-family:Sora,sans-serif;font-size:12px;font-weight:700;"
            "color:#F0F4FF;margin-bottom:3px;margin-top:4px;'>" + title + "</div>"
            "<div style='font-size:11px;color:#3D5270;line-height:1.4;'>" + desc + "</div>"
            "</div>"
        )

    steps = ""
    for n, ti, de, c1, c2 in [
        ("01", "Upload Resume", "Drop your PDF in the sidebar",  "#00FFB2", "#3D9BFF"),
        ("02", "Paste JD",      "Or pick a role template above", "#3D9BFF", "#9D7FFF"),
        ("03", "Get Analysis",  "All 5 agents in 60 to 120 sec", "#9D7FFF", "#FF3D6B"),
    ]:
        steps += (
            "<div style='flex:1;min-width:155px;text-align:center;padding:16px 12px;"
            "background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.06);"
            "border-radius:14px;'>"
            "<div style='font-family:Sora,sans-serif;font-size:1.9rem;font-weight:800;"
            "background:linear-gradient(135deg," + c1 + "," + c2 + ");"
            "-webkit-background-clip:text;background-clip:text;color:transparent;"
            "margin-bottom:5px;'>" + n + "</div>"
            "<div style='font-size:12px;font-weight:600;color:#F0F4FF;margin-bottom:2px;'>" + ti + "</div>"
            "<div style='font-size:11px;color:#3D5270;'>" + de + "</div>"
            "</div>"
        )

    html = (
        "<div style='min-height:88vh;display:flex;flex-direction:column;"
        "align-items:center;justify-content:center;padding:40px 20px;'>"
        "<div style='width:64px;height:64px;margin:0 auto 18px;"
        "background:linear-gradient(145deg,rgba(0,255,178,.14),rgba(61,155,255,.08));"
        "border-radius:18px;border:1px solid rgba(0,255,178,.3);"
        "display:flex;align-items:center;justify-content:center;"
        "box-shadow:0 0 36px rgba(0,255,178,.15);"
        "animation:borderGlow 4s ease-in-out infinite;'>"
        "<svg width='32' height='32' viewBox='0 0 24 24' fill='none'>"
        "<circle cx='10' cy='10' r='5' stroke='#00FFB2' stroke-width='1.5'/>"
        "<path d='M14.5 14.5L19 19' stroke='#00FFB2' stroke-width='1.8' stroke-linecap='round'/>"
        "<circle cx='10' cy='10' r='2' fill='#00FFB2' opacity='.7'/>"
        "<circle cx='10' cy='10' r='8' stroke='#00FFB2' stroke-width='.5'"
        " stroke-dasharray='3 2' opacity='.35'/>"
        "</svg></div>"
        "<h1 style='font-family:Sora,sans-serif;font-size:clamp(1.8rem,4.5vw,2.8rem);"
        "font-weight:800;letter-spacing:-2px;line-height:1.08;margin:0 0 14px;"
        "text-align:center;max-width:640px;"
        "background:linear-gradient(135deg,#ffffff 0%,#00FFB2 40%,#3D9BFF 70%,#9D7FFF 100%);"
        "-webkit-background-clip:text;background-clip:text;color:transparent;"
        "animation:fadeInUp .5s ease both;'>Know exactly why<br>you got rejected.</h1>"
        "<p style='font-size:.9rem;color:#8898B4;line-height:1.8;margin:0 0 24px;"
        "text-align:center;max-width:520px;animation:fadeInUp .5s ease .1s both;'>"
        "5 specialist AI agents dissect your resume against any job description."
        "</p>"
        "<div style='display:flex;gap:8px;justify-content:center;flex-wrap:wrap;"
        "margin-bottom:38px;animation:fadeInUp .5s ease .2s both;'>"
        "<span style='padding:5px 14px;border-radius:20px;"
        "border:1px solid rgba(0,255,178,.3);background:rgba(0,255,178,.06);color:#00FFB2;"
        "font-family:JetBrains Mono,monospace;font-size:10px;font-weight:600;'>&#9889; No API key for demo</span>"
        "<span style='padding:5px 14px;border-radius:20px;"
        "border:1px solid rgba(61,155,255,.3);background:rgba(61,155,255,.06);color:#3D9BFF;"
        "font-family:JetBrains Mono,monospace;font-size:10px;font-weight:600;'>&#128274; Runs locally</span>"
        "<span style='padding:5px 14px;border-radius:20px;"
        "border:1px solid rgba(255,61,107,.3);background:rgba(255,61,107,.06);color:#FF3D6B;"
        "font-family:JetBrains Mono,monospace;font-size:10px;font-weight:600;'>&#128128; Brutal Mode</span>"
        "</div>"
        "<div style='display:flex;gap:10px;margin-bottom:38px;max-width:580px;"
        "width:100%;flex-wrap:wrap;justify-content:center;'>"
        + steps +
        "</div>"
        "<div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3D5270;"
        "text-transform:uppercase;letter-spacing:3px;text-align:center;margin-bottom:12px;'>"
        "Everything included &#8212; 11 tools in one"
        "</div>"
        "<div style='display:grid;grid-template-columns:repeat(auto-fill,minmax(185px,1fr));"
        "gap:8px;width:100%;max-width:900px;'>"
        + cards +
        "</div></div>"
    )
    st.markdown(html, unsafe_allow_html=True)

def main():
    if _errs:
        st.warning("Optional modules missing: " + ", ".join(_errs[:2]))

    uploaded, company, jd, brutal, analyze = render_sidebar()

    api_key = (os.environ.get("ANTHROPIC_API_KEY") or
               os.environ.get("OPENAI_API_KEY")     or
               os.environ.get("GOOGLE_API_KEY"))
    demo_mode = not bool(api_key)

    # ── Show results if already done ──
    if st.session_state.get("done") and st.session_state.get("results"):
        results = st.session_state["results"]
        co      = st.session_state.get("company","")
        analyzed_at = st.session_state.get("analyzed_at", "")
        render_header(co, analyzed_at=analyzed_at)
        render_scores(results)
        render_score_explainer(results)
        render_score_micro_tips(results)
        render_score_history()
        st.markdown("<hr>", unsafe_allow_html=True)

        # ── JD Quick Scan + Resume Preview (collapsible) ──────
        jd_text   = st.session_state.get("jd", "")
        res_text  = st.session_state.get("resume_text", "")
        if jd_text:
            render_jd_quick_scan(jd_text)
        if res_text:
            render_resume_preview(res_text)

        # ── Main results tabs ─────────────────────────────────
        main_t1, main_t2, main_t3, main_t4 = st.tabs([
            "🤖 Agent Analysis",
            "📊 Section Scores",
            "🎯 Recruiter Simulator",
            "🔬 Multi-Agent vs Single AI",
        ])

        with main_t1:
            st.markdown('<div class="sec">Agent Analysis</div>', unsafe_allow_html=True)
            render_agent_tabs(results)
            st.markdown("<hr>", unsafe_allow_html=True)
            render_roadmap(results)

        with main_t2:
            st.markdown('<div class="sec">Resume Section Scores</div>', unsafe_allow_html=True)
            resume_txt = st.session_state.get("resume_text", "")
            render_section_scores(results, resume_txt)

        with main_t3:
            st.markdown('<div class="sec">Recruiter Shortlist Simulator</div>', unsafe_allow_html=True)
            render_recruiter_simulator(results)

        with main_t4:
            st.markdown('<div class="sec">Multi-Agent vs Single AI</div>', unsafe_allow_html=True)
            render_comparison(results)

        # ── Tools tabs ────────────────────────────────────────
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="sec">Career Tools</div>', unsafe_allow_html=True)
        tool_t1, tool_t2, tool_t3 = st.tabs([
            "💬 Interview Predictor",
            "✍ Cover Letter",
            "⚡ Bullet Improver",
        ])

        with tool_t1:
            render_interview_predictor(results)

        with tool_t2:
            render_cover_letter(
                results,
                resume_text=st.session_state.get("resume_text", ""),
                jd=st.session_state.get("jd", ""),
                company=co,
            )

        with tool_t3:
            render_bullet_improver(results)

        st.markdown("<hr>", unsafe_allow_html=True)
        render_quick_tips(results)
        st.markdown("<hr>", unsafe_allow_html=True)
        render_download(results, co)
        with st.expander("🔧 Raw JSON"):
            st.json(results)
        return

    # Intro replaced by render_empty landing page

    # ── Analyze button ──
    if analyze:
        render_header(company)

        if demo_mode:
            st.markdown('''<div style="background:rgba(245,166,35,.07);border:1px solid rgba(245,166,35,.3);
                             border-left:3px solid var(--amber);border-radius:10px;
                             padding:12px 16px;margin-bottom:12px;">
              <div style="font-family:JetBrains Mono,monospace;font-size:10px;color:var(--amber);
                          text-transform:uppercase;letter-spacing:1.2px;margin-bottom:4px;">
                ⚡ Demo Mode Active
              </div>
              <div style="font-size:12px;color:#FFD68A;line-height:1.6;">
                No API key detected — showing a sample analysis to demonstrate all features.
                Add <code style="background:rgba(0,0,0,.3);padding:1px 5px;border-radius:3px;">ANTHROPIC_API_KEY</code>
                to your <code style="background:rgba(0,0,0,.3);padding:1px 5px;border-radius:3px;">.env</code>
                file to run live analysis.
              </div>
            </div>''', unsafe_allow_html=True)

            import copy as _copy, uuid as _uuid2
            demo_steps = [
                (15,  "🤖 ATS Agent — scanning resume format & keywords…"),
                (32,  "🔬 Skills Gap Agent — mapping JD requirements…"),
                (54,  "📊 Experience Agent — auditing bullet quality…"),
                (76,  "🧠 Hiring Manager Agent — simulating gut reaction…"),
                (92,  "🎯 Coordinator — synthesising root-cause analysis…"),
            ]
            pb_demo   = st.progress(0)
            stat_demo = st.empty()
            for prog, msg in demo_steps:
                pb_demo.progress(prog)
                stat_demo.markdown(
                    f'<div class="al al-b" style="font-family:JetBrains Mono,monospace;font-size:12px;">{msg}</div>',
                    unsafe_allow_html=True)
                time.sleep(0.4)
            pb_demo.progress(100)
            stat_demo.empty()

            if HAS_MOCK:
                # Deep-copy so every demo run is a fresh independent dict —
                # this prevents the "same report every time" bug where the
                # shared MOCK_RESULT reference gets returned unchanged on re-runs
                fresh_result = _copy.deepcopy(MOCK_RESULT)
                demo_co = company.strip() if company.strip() else "Demo Company"
                import datetime as _dt
                st.session_state["results"]     = fresh_result
                st.session_state["company"]     = demo_co
                st.session_state["resume_text"] = ""
                st.session_state["jd"]          = jd or ""
                st.session_state["run_id"]      = str(_uuid2.uuid4())
                st.session_state["analyzed_at"] = _dt.datetime.now().strftime("%b %d, %Y · %H:%M")
                st.session_state["done"]        = True
                # Push to score history (keep last 5)
                _hist = st.session_state.get("score_history", [])
                _hist.append({
                    "company":    demo_co,
                    "overall":    fresh_result.get("coordinator", {}).get("overall_score", 0),
                    "ats":        fresh_result.get("ats", {}).get("ats_score", 0),
                    "skills":     fresh_result.get("skills", {}).get("match_score", 0),
                    "experience": fresh_result.get("experience", {}).get("experience_score", 0),
                    "hm":         fresh_result.get("hiring_manager", {}).get("gut_score", 0),
                    "verdict":    fresh_result.get("coordinator", {}).get("application_verdict", ""),
                    "timestamp":  _dt.datetime.now().strftime("%H:%M"),
                })
                st.session_state["score_history"] = _hist[-5:]
                st.rerun()
            else:
                st.error("Mock data not available.")
            return

        if not uploaded:
            st.markdown('<div class="al al-r">❌ Please upload your resume PDF in the sidebar.</div>', unsafe_allow_html=True)
            return
        if not jd or len(jd.strip()) < 20:
            st.markdown('<div class="al al-a">⚡ Please paste a job description (at least 20 characters).</div>', unsafe_allow_html=True)
            return

        with st.spinner("📄 Parsing resume PDF..."):
            resume_text = extract_text_from_pdf(uploaded)
        if not resume_text or len(resume_text.strip()) < 50:
            st.error("Could not read PDF text. Use a text-based PDF (not a scanned image).")
            return

        # ── Live timer + agent progress UI ──────────────────────────
        timer_slot   = st.empty()
        status_slot  = st.empty()
        pb           = st.progress(5)

        # Inject live JS timer that counts up every second
        timer_slot.markdown("""
        <div id="hl-timer-wrap" style="display:flex;align-items:center;gap:12px;
             background:rgba(61,155,255,.06);border:1px solid rgba(61,155,255,.25);
             border-radius:10px;padding:12px 18px;margin-bottom:8px;">
          <div style="font-size:24px;">⏱</div>
          <div>
            <div style="font-family:'JetBrains Mono',monospace;font-size:10px;
                        color:#3D9BFF;text-transform:uppercase;letter-spacing:1.5px;">Analysis Running</div>
            <div style="font-family:'JetBrains Mono',monospace;font-size:22px;
                        font-weight:700;color:#E2E8F0;" id="hl-timer">0:00</div>
          </div>
          <div style="margin-left:auto;font-size:11px;color:#64748B;line-height:1.6;">
            5 specialist agents · 60–120 sec typical
          </div>
        </div>
        <script>
        (function(){
          var s = 0;
          var el = document.getElementById('hl-timer');
          if(!el) return;
          var iv = setInterval(function(){
            s++;
            var m = Math.floor(s/60);
            var sec = s%60;
            if(el) el.textContent = m+':'+(sec<10?'0':'')+sec;
          }, 1000);
          window._hlTimerIv = iv;
        })();
        </script>
        """, unsafe_allow_html=True)

        AGENT_STEPS = [
            (20,  "🤖 ATS Agent — scanning keywords & format compliance…"),
            (40,  "🔬 Skills Gap Agent — mapping JD requirements vs resume…"),
            (60,  "📊 Experience Agent — auditing bullets & impact evidence…"),
            (80,  "🧠 Hiring Manager Agent — simulating recruiter decision…"),
            (95,  "🎯 Coordinator Agent — synthesising root-cause analysis…"),
        ]

        # Show first step immediately
        pb.progress(AGENT_STEPS[0][0])
        status_slot.markdown(
            f'<div class="al al-b" style="font-family:JetBrains Mono,monospace;font-size:12px;">'
            f'{AGENT_STEPS[0][1]}</div>', unsafe_allow_html=True)

        try:
            from agents.crew_agents import run_hirelens_analysis

            raw = run_hirelens_analysis(
                resume_text=resume_text,
                job_description=jd,
                company_name=company.strip() or "the company",
                brutal_mode=brutal,
            )

            pb.progress(100)
            timer_slot.empty()
            status_slot.markdown(
                '<div class="al al-g" style="font-size:14px;">✅ Analysis complete! Scroll down to see results.</div>',
                unsafe_allow_html=True)

            import uuid as _uuid, datetime as _dt2
            result = raw.model_dump(by_alias=True) if hasattr(raw, "model_dump") else raw
            st.session_state["results"]     = result
            st.session_state["company"]     = company
            st.session_state["resume_text"] = resume_text
            st.session_state["jd"]          = jd
            st.session_state["run_id"]      = str(_uuid.uuid4())
            st.session_state["analyzed_at"] = _dt2.datetime.now().strftime("%b %d, %Y · %H:%M")
            st.session_state["done"]        = True
            # Push to score history (keep last 5)
            _hist2 = st.session_state.get("score_history", [])
            _hist2.append({
                "company":    company,
                "overall":    result.get("coordinator", {}).get("overall_score", 0),
                "ats":        result.get("ats", {}).get("ats_score", 0),
                "skills":     result.get("skills", {}).get("match_score", 0),
                "experience": result.get("experience", {}).get("experience_score", 0),
                "hm":         result.get("hiring_manager", {}).get("gut_score", 0),
                "verdict":    result.get("coordinator", {}).get("application_verdict", ""),
                "timestamp":  _dt2.datetime.now().strftime("%H:%M"),
            })
            st.session_state["score_history"] = _hist2[-5:]
            st.rerun()

        except Exception as e:
            pb.progress(0)
            timer_slot.empty()
            status_slot.empty()
            render_friendly_error(e, "analysis")
        return

    # ── Empty state ──
    render_empty()


if __name__ == "__main__":
    main()
