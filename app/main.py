import sys
import os

# Automatically configure sys.path so 'app' can be resolved from anywhere
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

for _p in (PROJECT_ROOT, BASE_DIR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

os.environ["PYTHONPATH"] = f"{PROJECT_ROOT}{os.pathsep}{BASE_DIR}{os.pathsep}{os.environ.get('PYTHONPATH', '')}"

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response, RedirectResponse
from pydantic import BaseModel, EmailStr
import json

app = FastAPI(
    title="Y.N.A. Dewmini | Portfolio",
    description="Mobile-First Portfolio for Y.N.A. Dewmini - A/L Physical Science Student at R/Ferguson High School aspiring for Computer Engineering, Game Development & AI",
    version="1.0.0"
)

# Setup pathing
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Data Models
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

# Portfolio Data — Y.N.A. Dewmini
PORTFOLIO_DATA = {
    "profile": {
        "name": "Y.N.A. Dewmini",
        "full_name": "Yattowitage Nethsarani Ahinsa Dewmini",
        "title": "A/L Physical Science Student | Aspiring Computer Engineer & Game Developer",
        "dob": "15/12/2009",
        "age": 16,
        "location": "Rathnapura, Sri Lanka",
        "address": "Akkara 20, Pagoda, Gileemale, Rathnapura, Sri Lanka",
        "status": "Advanced Level (A/L) Student — R/Ferguson High School",
        "bio": "Passionate A/L Physical Science student at R/Ferguson High School, Rathnapura, with a strong drive for Computer Engineering, Game Development, and Artificial Intelligence. Achieved 9A passes in O/L 2025 and now building expertise in Python, HTML & CSS while pursuing my dream of engineering a future in tech.",
        "target_career": "Computer Engineering / Game Development / AI",
        "socials": {
            "github": "https://github.com/ynadewmini",
            "linkedin": "https://www.linkedin.com/in/ynadewmini",
            "email": "ynadewmini@gmail.com",
            "whatsapp": "https://wa.me/94713377021",
            "telegram": "https://t.me/+94713377021"
        }
    },
    "academics": {
        "stream": "Physical Science",
        "school": "R/Ferguson High School",
        "expected_exam": "2028 A/L Examination",
        "ol_results": {
            "cert_id": "ol-examination",
            "year": "2025",
            "school": "R/Sumana Balika Vidyalaya",
            "grade": "9A Passes",
            "subjects": ["English", "Sinhala", "Buddhism", "History", "Science", "Mathematics", "Sinhala Literature", "ICT", "Geography"]
        },
        "scholarship": {
            "cert_id": "scholarship",
            "year": "Grade 5",
            "school": "R/Samanala Maha Vidyalaya",
            "marks": 163,
            "result": "Passed — Entered R/Sumana Balika Vidyalaya"
        },
        "dahampasal": {
            "cert_id": "dahampasal-academic",
            "title": "Dahampasal (Sunday School) Academic Achievements",
            "icon": "fa-dharmachakra",
            "description": "Completed multiple Dhamma examinations with distinction, demonstrating dedication to Buddhist academic studies and moral education."
        },
        "subjects": [
            {
                "name": "Combined Mathematics",
                "code": "Pure & Applied Maths",
                "progress": 80,
                "description": "Calculus, Trigonometry, Vectors, Dynamics, and Statics — the core foundation for Computer Engineering."
            },
            {
                "name": "Physics",
                "code": "Theoretical & Practical Physics",
                "progress": 82,
                "description": "Mechanics, Electricity & Magnetism, Electronics, Waves, and Modern Physics."
            },
            {
                "name": "Chemistry",
                "code": "Physical, Inorganic & Organic",
                "progress": 78,
                "description": "Atomic structure, chemical equilibrium, organic synthesis, and thermodynamics."
            },
            {
                "name": "GIT (General Information Technology)",
                "code": "General Information Technology",
                "progress": 95,
                "description": "Python programming, data structures, database management, and web technologies"
            },
            
            {
                "name": "English",
                "code": "English Grammar, Communication",
                "progress": 95,
                "description": "Genaral English, Creative Writing, Grammar"
            }
        ],
        "roadmap": [
            {"phase": "Current", "title": "A/L Physical Science @ R/Ferguson High School", "year": "2025–2028", "detail": "Building strong math, physics, and programming foundations. Learning Python, HTML & CSS."},
            {"phase": "Next Step", "title": "B.Sc. Hons in Computer Engineering", "year": "2029", "detail": "Targeting a top Sri Lankan university Faculty of Engineering."},
            {"phase": "Future Goal", "title": "Game Development & AI Specialization", "year": "2033+", "detail": "Build immersive games and intelligent AI systems that change the way people interact with technology."}
        ]
    },
    "skills": [
        {"category": "Programming Languages", "items": ["Python", "HTML5", "CSS3"]},
        {"category": "Interests & Learning", "items": ["Game Development", "Artificial Intelligence", "Web Development", "Computer Engineering"]},
        {"category": "Academic Strengths", "items": ["ICT & Computing", "Mathematics", "Physics", "Problem Solving", "Englis"]},
        {"category": "Soft Skills", "items": ["Self-Motivated Learner", "Creative Thinking", "Analytical Reasoning", "Goal-Oriented"]}
    ],
    "projects": [
        {
            "id": 1,
            "title": "Personal Portfolio Website",
            "category": "Web Development",
            "description": "A mobile-first progressive web app portfolio built with FastAPI and glassmorphism UI to showcase my academic journey, skills, and career goals as an aspiring Computer Engineer.",
            "tech": ["Python", "FastAPI", "HTML5", "CSS3", "JavaScript"],
            "github": "https://github.com",
            "demo": "#",
            "featured": True,
            "icon": "fa-laptop-code"
        },
        {
            "id": 2,
            "title": "Python Learning Projects",
            "category": "Python & Logic",
            "description": "A collection of Python scripts and mini-projects built while self-learning programming — including calculators, logic games, and automation scripts as I level up my coding skills.",
            "tech": ["Python"],
            "github": "https://github.com",
            "demo": "#",
            "featured": True,
            "icon": "fa-python"
        },
        {
            "id": 3,
            "title": "Static Web Pages (HTML & CSS)",
            "category": "Web Design",
            "description": "Practice web pages built using HTML5 and CSS3, experimenting with layouts, colors, animations, and responsive design — the foundation of my web development journey.",
            "tech": ["HTML5", "CSS3"],
            "github": "https://github.com",
            "demo": "#",
            "featured": False,
            "icon": "fa-code"
        },
        {
            "id": 4,
            "title": "Future: 2D Game Project",
            "category": "Game Development",
            "description": "An upcoming project: my first 2D game using Python and Pygame. This will be my step into game development — one of my biggest passions alongside AI and Computer Engineering.",
            "tech": ["Python", "Pygame"],
            "github": "https://github.com",
            "demo": "#",
            "featured": True,
            "icon": "fa-gamepad"
        }
    ],
    "extracurriculars": [
        {
            "category": "Uniformed Units & Leadership",
            "icon": "fa-shield-halved",
            "color": "var(--accent-secondary)",
            "items": [
                {
                    "cert_id": "girl-guides",
                    "title": "Sri Lanka Girl Guides Association",
                    "role": "Active Girl Guide",
                    "badge": "Leadership & Service",
                    "icon": "fa-compass",
                    "description": "Active member cultivating leadership, outdoor discipline, team collaboration, and community service initiatives."
                },
                {
                    "cert_id": "st-john-ambulance",
                    "title": "St. John Ambulance Cadets",
                    "role": "First Aid & Health Volunteer",
                    "badge": "First Aid & Care",
                    "icon": "fa-kit-medical",
                    "description": "Trained in life-saving first aid fundamentals, emergency preparedness, disciplined service, and humanitarian care, Army cadet full training."
                }
            ]
        },
        {
            "category": "Aesthetic & Cultural Competitions",
            "icon": "fa-music",
            "color": "var(--accent-tertiary)",
            "items": [
                {
                    "cert_id": "singing-competitions",
                    "title": "Singing Competitions",
                    "role": "Vocalist & Performer",
                    "badge": "Awards & Merit",
                    "icon": "fa-microphone-lines",
                    "description": "Participated in and received awards across Daham school (Sunday School), zonal, and district-level singing competitions, fostering creative expression and stage confidence."
                },
                {
                    "cert_id": "daham-pasala",
                    "title": "Daham Pasala (Sunday School)",
                    "role": "Religious & Cultural Studies",
                    "badge": "Excellence & Values",
                    "icon": "fa-dharmachakra",
                    "description": "Earned certificates in Buddhist studies, Dhamma examinations, and cultural festivals, building moral integrity and cultural awareness."
                }
            ]
        },
        {
            "category": "Mind Sports & Youth Development",
            "icon": "fa-chess",
            "color": "var(--accent-primary)",
            "items": [
                {
                    "cert_id": "chess-tournaments",
                    "title": "Chess Tournaments",
                    "role": "Tournament Competitor",
                    "badge": "Mind Sport",
                    "icon": "fa-chess-knight",
                    "description": "Awarded certificates of participation in competitive chess tournaments, honing strategic decision-making, foresight, and patience."
                },
                {
                    "cert_id": "youth-leadership",
                    "title": "Youth Leadership & Skill Programs",
                    "role": "Certified Participant",
                    "badge": "Participation & Skills",
                    "icon": "fa-certificate",
                    "description": "Active participant in various school and community development workshops, youth empowerment programs, and skill-building seminars."
                }
            ]
        }
    ],
    "certificates": {
        "ol-examination": {
            "id": "ol-examination",
            "title": "G.C.E. Ordinary Level (O/L) Examination 2025",
            "subtitle": "Department of Examinations Sri Lanka",
            "year": "2025",
            "school": "R/Sumana Balika Vidyalaya",
            "badge": "9A Passes — All Distinctions",
            "badge_color": "var(--accent-secondary)",
            "category": "Academic Milestone",
            "icon": "fa-trophy",
            "images": [
                {
                    "url": "/static/images/certificates/ol_exam.jpg",
                    "caption": "Official G.C.E. Ordinary Level (O/L) Certificate of Educational Excellence with 9A Distinctions awarded to Y.N.A. Dewmini.",
                    "tag": "Main Certificate"
                }
            ],
            "highlights": [
                "Achieved 9 Distinction (A) passes in all nine examination subjects",
                "Subjects: English, Sinhala, Buddhism, History, Science, Mathematics, Sinhala Literature, ICT, Geography",
                "Qualified for A/L Physical Science stream at premier R/Ferguson High School"
            ],
            "description": "Achieved the highest possible academic distinction with 9A passes in the General Certificate of Education (O/L) Examination 2025. This accomplishment forms the solid academic foundation for pursuing A/L Combined Mathematics, Physics, Chemistry, and an aspiring career in Computer Engineering.",
            "issue_date": "O/L 2025",
            "credential_id": "INDEX: 23145678",
            "verification_status": "Verified Official Examination Result"
        },
        "scholarship": {
            "id": "scholarship",
            "title": "Grade 5 National Scholarship Examination",
            "subtitle": "Ministry of Education, Sri Lanka",
            "year": "Grade 5",
            "school": "R/Samanala Maha Vidyalaya",
            "badge": "163 Marks — Merit Pass",
            "badge_color": "var(--accent-tertiary)",
            "category": "Academic Milestone",
            "icon": "fa-medal",
            "images": [
                {
                    "url": "/static/images/certificates/scholarship.jpg",
                    "caption": "Ministry of Education Grade 5 Scholarship Examination Certificate of Academic Merit (163 Marks).",
                    "tag": "Merit Certificate"
                }
            ],
            "highlights": [
                "Scored 163 marks in the highly competitive national Grade 5 Scholarship",
                "Gained admission to premier secondary school R/Sumana Balika Vidyalaya",
                "Recognized for top-ranking primary aptitude and academic promise"
            ],
            "description": "Awarded Certificate of Academic Merit by the Ministry of Education for securing a distinguished 163-mark score in the nationwide Grade 5 Scholarship examination, earning direct entry into R/Sumana Balika Vidyalaya.",
            "issue_date": "Grade 5 Examination",
            "credential_id": "EXAM-DIV-SCHOLAR-163",
            "verification_status": "Verified Ministry Examination Result"
        },
        "girl-guides": {
            "id": "girl-guides",
            "title": "Sri Lanka Girl Guides Association",
            "subtitle": "Sri Lanka Girl Guides Association (SLGGA)",
            "year": "Active Guide",
            "school": "R/Ferguson High School & R/Sumana Balika",
            "badge": "Leadership & Service",
            "badge_color": "var(--accent-secondary)",
            "category": "Uniformed Units & Leadership",
            "icon": "fa-compass",
            "images": [
                {
                    "url": "/static/images/certificates/girl_guides.jpg",
                    "caption": "Sri Lanka Girl Guides Association Official Certificate of Leadership and Service awarded to Y.N.A. Dewmini.",
                    "tag": "Leadership Certificate"
                }
            ],
            "highlights": [
                "Active member cultivating disciplined leadership, team collaboration, and outdoor skills",
                "Participated in environmental campaigns, community service, and youth rallies",
                "Earned SLGGA leadership and teamwork merit recognition"
            ],
            "description": "Certificate of Leadership and Service conferred by the Sri Lanka Girl Guides Association in recognition of sustained dedication, exemplary teamwork, outdoor problem-solving, and impactful civic contributions.",
            "issue_date": "15th November 2023",
            "credential_id": "SLGGA-HQ-LEAD-2023",
            "verification_status": "Verified Association Credential"
        },
        "st-john-ambulance": {
            "id": "st-john-ambulance",
            "title": "St. John Ambulance Cadets",
            "subtitle": "St. John Ambulance Association Sri Lanka",
            "year": "Certified Cadet",
            "school": "First Aid & Cadet Training Division",
            "badge": "First Aid & Care — Cadet Training",
            "badge_color": "#ef4444",
            "category": "Uniformed Units & Leadership",
            "icon": "fa-kit-medical",
            "images": [
                {
                    "url": "/static/images/certificates/st_john.jpg",
                    "caption": "St. John Ambulance First Aid and Cadet Training Certificate of Proficiency awarded to Y.N.A. Dewmini.",
                    "tag": "Proficiency Certificate"
                }
            ],
            "highlights": [
                "Trained and examined in life-saving first aid fundamentals, CPR, and triage",
                "Completed disciplined Army cadet drill training, endurance, and physical preparedness",
                "Active volunteer for health assistance and school emergency response squads"
            ],
            "description": "First Aid and Cadet Training Certificate of Proficiency awarded by St. John Ambulance Association under official certification, recognizing successful completion of first aid medical instruction and full Army cadet training.",
            "issue_date": "18th March 2024",
            "credential_id": "STJ-REG-49382",
            "verification_status": "Certified Life-Saving First Aider"
        },
        "singing-competitions": {
            "id": "singing-competitions",
            "title": "Singing & Vocal Music Competitions",
            "subtitle": "All-Island & Zonal Youth Singing Competitions",
            "year": "Award Winner",
            "school": "Zonal & Daham School Cultural Forum",
            "badge": "First Place & Zonal Merit",
            "badge_color": "var(--accent-tertiary)",
            "category": "Aesthetic & Cultural Competitions",
            "icon": "fa-microphone-lines",
            "images": [
                {
                    "url": "/static/images/certificates/singing.jpg",
                    "caption": "Certificate of Award & Musical Merit — First Place Winner in Vocal Performance awarded to Y.N.A. Dewmini.",
                    "tag": "Award Certificate"
                }
            ],
            "highlights": [
                "Awarded First Place Winner in vocal performance and singing competitions",
                "Honored across Sunday school, zonal, and district-level aesthetic stages",
                "Demonstrated musical expression, vocal discipline, and confident stage delivery"
            ],
            "description": "Certificate of Award & Musical Merit presented for winning First Place in vocal singing competitions, celebrating vocal range, rhythm, melodic interpretation, and creative performing arts talent.",
            "issue_date": "Annual Cultural Festival",
            "credential_id": "AIZYSC-VOC-018",
            "verification_status": "Verified Cultural Award"
        },
        "daham-pasala": {
            "id": "daham-pasala",
            "title": "Daham Pasala (Sunday School) Buddhist Studies",
            "subtitle": "Ministry of Buddha Sasana & Religious Affairs",
            "year": "Distinction Pass",
            "school": "Sri Daham Pasala",
            "badge": "Excellence & Values",
            "badge_color": "#f59e0b",
            "category": "Aesthetic & Cultural Competitions",
            "icon": "fa-dharmachakra",
            "images": [
                {
                    "url": "/static/images/certificates/daham_pasala.jpg",
                    "caption": "Dhamma Sunday School Examination Certificate of Distinction awarded to Y.N.A. Dewmini.",
                    "tag": "Distinction Certificate"
                }
            ],
            "highlights": [
                "Achieved Distinction Pass in annual Dhamma examinations",
                "Certified in Buddhist culture, Pali philosophy, and moral education",
                "Active leadership in Sunday school cultural events and community service"
            ],
            "description": "Certificate of Distinction awarded by the Ministry of Buddha Sasana and National Dhamma Education Board for exemplary performance in Dhamma examinations, building moral discipline, mindfulness, and cultural values.",
            "issue_date": "BE 2567 / 2023",
            "credential_id": "DHAMMA-DIST-2567",
            "verification_status": "Official Dhamma Examination Distinction"
        },
        "chess-tournaments": {
            "id": "chess-tournaments",
            "title": "Competitive Chess Tournaments",
            "subtitle": "Sri Lanka Schools Chess Association (SLSCA)",
            "year": "Tournament Competitor",
            "school": "District & Inter-School Championships",
            "badge": "Mind Sport — Merit & Participation",
            "badge_color": "var(--accent-primary)",
            "category": "Mind Sports & Youth Development",
            "icon": "fa-chess-knight",
            "images": [
                {
                    "url": "/static/images/certificates/chess.svg",
                    "caption": "Sri Lanka Schools Chess Association Tournament Certificate of Merit and Participation awarded to Y.N.A. Dewmini.",
                    "tag": "Tournament Certificate"
                }
            ],
            "highlights": [
                "Competed in inter-school and district-level competitive chess tournaments",
                "Honed tactical problem-solving, foresight, opening theory, and strategic planning",
                "Demonstrated sportsmanlike conduct and composure in competitive play"
            ],
            "description": "Certificate of Merit and Participation conferred by the Sri Lanka Schools Chess Association (SLSCA) for competitive tournament performance, recognizing tactical sharpness and intellectual patience.",
            "issue_date": "2023–2024",
            "credential_id": "SLSCA-TOURN-882",
            "verification_status": "Verified Tournament Competitor"
        },
        "youth-leadership": {
            "id": "youth-leadership",
            "title": "Youth Leadership & Skill Programs",
            "subtitle": "National Youth Empowerment & Skill Development Forum",
            "year": "Certified Participant",
            "school": "School & Community Youth Forum",
            "badge": "Participation & Skills",
            "badge_color": "var(--accent-secondary)",
            "category": "Mind Sports & Youth Development",
            "icon": "fa-certificate",
            "images": [
                {
                    "url": "/static/images/certificates/youth_leadership.svg",
                    "caption": "Certificate of Achievement in Youth Leadership, Team Building and Soft Skills Curriculum awarded to Y.N.A. Dewmini.",
                    "tag": "Leadership Certificate"
                }
            ],
            "highlights": [
                "Completed intensive workshops on youth leadership, digital literacy, and public communication",
                "Spearheaded collaborative student group initiatives and community projects",
                "Awarded Certificate of Achievement for proactive problem solving"
            ],
            "description": "Certificate of Achievement awarded for successful completion of the Future Leaders & Community Innovation youth program, cultivating high-impact soft skills, public communication, and collaborative teamwork.",
            "issue_date": "2024",
            "credential_id": "YOUTH-LEAD-731",
            "verification_status": "Verified Program Participant"
        },
        "dahampasal-academic": {
            "id": "dahampasal-academic",
            "title": "Dahampasal (Sunday School) Academic Achievements",
            "subtitle": "Ministry of Buddha Sasana & Religious Affairs",
            "year": "Multiple Years",
            "school": "Sri Daham Pasala",
            "badge": "Academic Excellence",
            "badge_color": "#f59e0b",
            "category": "Academic Milestone",
            "icon": "fa-dharmachakra",
            "images": [
                {
                    "url": "/static/images/certificates/daham_pasala.jpg",
                    "caption": "Dahampasal (Sunday School) academic certificates and examination results awarded to Y.N.A. Dewmini.",
                    "tag": "Academic Certificate"
                }
            ],
            "highlights": [
                "Achieved distinction passes in multiple Dhamma School examinations",
                "Demonstrated commitment to Buddhist academic studies and cultural values",
                "Active participant in Daham Pasala educational programs and cultural events"
            ],
            "description": "Collection of academic achievements from Dahampasal (Sunday School) examinations, including Dhamma studies, Buddhist philosophy, and moral education certifications.",
            "issue_date": "Multiple Years",
            "credential_id": "DHAMMA-ACAD-MULTI",
            "verification_status": "Verified Dhamma Examination Results",
            "accomplishments": [
                {
                    "id": "prathama-exam",
                    "title": "Prathama Dhamma Examination (ප්‍රාථමික ධර්ම විභාගය)",
                    "year": "2019",
                    "badge": "Distinction Pass",
                    "badge_color": "#f59e0b",
                    "image": {
                        "url": "/static/images/certificates/daham_pasala.jpg",
                        "caption": "Prathama (Primary) Dhamma School Examination Certificate of Distinction.",
                        "tag": "Examination Certificate"
                    },
                    "description": "Successfully completed the Prathama (Primary) level Dhamma School Examination with distinction, demonstrating foundational knowledge in Buddhist teachings, Pali language basics, and moral education.",
                    "highlights": [
                        "Achieved Distinction Pass in Primary-level Dhamma examination",
                        "Demonstrated strong foundation in Buddhist teachings and Pali studies",
                        "Recognized for exemplary conduct and dedication to religious studies"
                    ]
                },
                {
                    "id": "dvitheeya-exam",
                    "title": "Dvitheeya Dhamma Examination (ද්විතීය ධර්ම විභාගය)",
                    "year": "2021",
                    "badge": "Merit Pass",
                    "badge_color": "#06b6d4",
                    "image": {
                        "url": "/static/images/certificates/daham_pasala.jpg",
                        "caption": "Dvitheeya (Secondary) Dhamma School Examination Certificate of Merit.",
                        "tag": "Examination Certificate"
                    },
                    "description": "Completed the Dvitheeya (Secondary) level Dhamma School Examination with merit, advancing understanding of Abhidhamma, Sutta Pitaka, and Vinaya studies.",
                    "highlights": [
                        "Achieved Merit Pass in Secondary-level Dhamma examination",
                        "Advanced knowledge in Abhidhamma and Sutta Pitaka teachings",
                        "Participation in Dhamma school cultural and educational programs"
                    ]
                },
                {
                    "id": "thritheeya-exam",
                    "title": "Thritheeya Dhamma Examination (තෘතීය ධර්ම විභාගය)",
                    "year": "2023",
                    "badge": "Distinction Pass",
                    "badge_color": "#a855f7",
                    "image": {
                        "url": "/static/images/certificates/daham_pasala.jpg",
                        "caption": "Thritheeya (Tertiary) Dhamma School Examination Certificate of Distinction.",
                        "tag": "Examination Certificate"
                    },
                    "description": "Achieved distinction in the Thritheeya (Tertiary) level Dhamma School Examination, showcasing advanced understanding of Buddhist philosophy, ethics, and cultural heritage.",
                    "highlights": [
                        "Achieved Distinction Pass in Tertiary-level Dhamma examination",
                        "Advanced proficiency in Buddhist philosophy and ethical studies",
                        "Leadership in Daham Pasala cultural events and community service"
                    ]
                }
            ]
        }
    }
}

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"data": PORTFOLIO_DATA})


@app.get("/api/profile")
async def get_profile():
    return PORTFOLIO_DATA["profile"]

@app.get("/api/academics")
async def get_academics():
    return PORTFOLIO_DATA["academics"]

@app.get("/api/skills")
async def get_skills():
    return PORTFOLIO_DATA["skills"]

@app.get("/api/projects")
async def get_projects():
    return PORTFOLIO_DATA["projects"]

@app.get("/api/extracurriculars")
async def get_extracurriculars():
    return PORTFOLIO_DATA["extracurriculars"]

@app.get("/certificates", response_class=HTMLResponse)
async def view_certificates_index(request: Request):
    return RedirectResponse(url="/certificates/ol-examination", status_code=302)

@app.get("/certificates/{cert_id}", response_class=HTMLResponse)
async def view_certificate(request: Request, cert_id: str):
    certs = PORTFOLIO_DATA.get("certificates", {})
    if cert_id not in certs:
        raise HTTPException(status_code=404, detail="Certificate not found")
    
    cert = certs[cert_id]
    return templates.TemplateResponse(
        request=request,
        name="certificate_view.html",
        context={
            "data": PORTFOLIO_DATA,
            "cert": cert,
            "all_certs": certs
        }
    )

@app.get("/api/certificates")
async def get_certificates():
    return PORTFOLIO_DATA.get("certificates", {})

@app.get("/api/certificates/{cert_id}")
async def get_certificate(cert_id: str):
    certs = PORTFOLIO_DATA.get("certificates", {})
    if cert_id not in certs:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return certs[cert_id]

@app.post("/api/contact")
async def submit_contact(form_data: ContactForm):
    # In a real app, this could send an email or store in DB
    return {
        "status": "success",
        "message": f"Thank you {form_data.name}! Your message regarding '{form_data.subject}' has been received successfully."
    }

@app.get("/api/download-cv")
async def download_cv():
    p = PORTFOLIO_DATA["profile"]
    a = PORTFOLIO_DATA["academics"]
    
    cv_content = f"""====================================================
{p['name'].upper()} - ACADEMIC CV & PORTFOLIO
====================================================
Status: {p['status']}
Target Career: {p['target_career']}
Location: {p['location']}
Email: {p['socials']['email']}
GitHub: {p['socials']['github']}
LinkedIn: {p['socials']['linkedin']}

----------------------------------------------------
1. ABOUT & OBJECTIVE
----------------------------------------------------
{p['bio']}

----------------------------------------------------
2. ACADEMIC BACKGROUND
----------------------------------------------------
Stream: {a['stream']}
Expected Exam: {a['expected_exam']}

Subjects:
"""
    for sub in a['subjects']:
        cv_content += f" - {sub['name']} ({sub['code']}): {sub['description']}\n"

    cv_content += """
----------------------------------------------------
3. FEATURED PROJECTS
----------------------------------------------------
"""
    for proj in PORTFOLIO_DATA['projects']:
        cv_content += f"- {proj['title']} [{proj['category']}]\n  {proj['description']}\n  Technologies: {', '.join(proj['tech'])}\n\n"

    cv_content += """----------------------------------------------------
4. CO-CURRICULAR & LEADERSHIP ACHIEVEMENTS
----------------------------------------------------
"""
    for ec_group in PORTFOLIO_DATA['extracurriculars']:
        cv_content += f"\n[{ec_group['category'].upper()}]\n"
        for item in ec_group['items']:
            cv_content += f" - {item['title']} | {item['role']} ({item['badge']})\n   {item['description']}\n"

    cv_content += """
====================================================
Generated via Python FastAPI Portfolio Engine
====================================================
"""
    return Response(
        content=cv_content,
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={p['name'].replace(' ', '_')}_Academic_CV.txt"}
    )

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("  🚀 Y.N.A. Dewmini Portfolio App is starting...")
    print("  🌐 Localhost URL: http://localhost:8000")
    print("  🌐 Network URL:   http://127.0.0.1:8000")
    print("="*60 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)

