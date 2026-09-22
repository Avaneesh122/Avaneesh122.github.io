"""Render Avaneesh Bhoite's resume (from Resume-mk20.docx content) to a clean PDF for the portfolio site."""
from fpdf import FPDF

_REPLACEMENTS = {
    "–": "-",
    "—": "--",
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
    "²": "2",
}


def _ascii(text):
    for src, dst in _REPLACEMENTS.items():
        text = text.replace(src, dst)
    return text

NAVY = (20, 20, 20)
GRAY = (90, 90, 90)
RULE = (200, 200, 200)

MARGIN = 18
PAGE_W = 215.9  # US Letter

pdf = FPDF(format="Letter", unit="mm")
pdf.set_margins(MARGIN, MARGIN, MARGIN)
pdf.set_auto_page_break(True, margin=18)
pdf.add_page()
pdf.set_text_color(*NAVY)

CONTENT_W = PAGE_W - 2 * MARGIN


def h1(text):
    pdf.set_font("Times", "B", 20)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 8, _ascii(text), ln=1)


def contact_line(text):
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 6, _ascii(text), ln=1)
    pdf.ln(1)


def section(text):
    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 6, _ascii(text.upper()), ln=1)
    y = pdf.get_y()
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.3)
    pdf.line(MARGIN, y, PAGE_W - MARGIN, y)
    pdf.ln(2.5)


def row(left, right, bold=True, size=10.5):
    pdf.set_font("Times", "B" if bold else "", size)
    pdf.set_text_color(*NAVY)
    w_right = 55
    w_left = CONTENT_W - w_right
    x0 = pdf.get_x()
    y0 = pdf.get_y()
    pdf.multi_cell(w_left, 5.2, _ascii(left))
    y1 = pdf.get_y()
    pdf.set_xy(x0 + w_left, y0)
    pdf.set_font("Times", "I", 9.5)
    pdf.set_text_color(*GRAY)
    pdf.multi_cell(w_right, 5.2, _ascii(right), align="R")
    pdf.set_y(max(y1, pdf.get_y()))


def subrow(left, right):
    pdf.set_font("Times", "I", 9.5)
    pdf.set_text_color(*GRAY)
    w_right = 55
    w_left = CONTENT_W - w_right
    x0 = pdf.get_x()
    y0 = pdf.get_y()
    pdf.multi_cell(w_left, 5, _ascii(left))
    y1 = pdf.get_y()
    pdf.set_xy(x0 + w_left, y0)
    pdf.multi_cell(w_right, 5, _ascii(right), align="R")
    pdf.set_y(max(y1, pdf.get_y()))
    pdf.ln(0.5)


def para(text, size=9.7):
    pdf.set_font("Times", "", size)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(CONTENT_W, 4.8, _ascii(text))
    pdf.ln(0.5)


def bullet(text, size=9.7):
    pdf.set_font("Times", "", size)
    pdf.set_text_color(*NAVY)
    indent = 5
    bullet_w = 4
    x0 = pdf.get_x()
    pdf.set_x(x0 + indent)
    pdf.cell(bullet_w, 4.6, "-")
    pdf.set_x(x0 + indent + bullet_w)
    pdf.multi_cell(CONTENT_W - indent - bullet_w, 4.6, _ascii(text))
    pdf.set_x(x0)


# Header
h1("Avaneesh Sanjay Bhoite")
contact_line(
    "US Citizen  |  avaneesh.bhoite@gmail.com  |  (603) 404-7871  |  "
    "linkedin.com/in/avaneesh-bhoite  |  github.com/Avaneesh122"
)

# Professional Summary
section("Professional Summary")
para(
    "Computer Science graduate student at Emory University with hands-on experience building AI systems, "
    "cloud-native architectures, and machine learning pipelines. Developed a serverless multi-agent platform "
    "on AWS at TCS, built ML models for financial forecasting and medical image classification, and published "
    "research on reinforcement learning. Comfortable working across the full stack from model development to "
    "cloud deployment."
)

# Education
section("Education")
row("Emory University", "Atlanta, GA")
subrow("Master's in Computer Science. GPA: 3.8/4.00.", "Aug 2025 – Present")
para(
    "Relevant Coursework: Machine Learning and Computational Analytics, Information Retrieval and AI Systems, "
    "PhD-level Algorithms, Data Mining, Database Systems, NLP, Human-AI Interaction, "
    "Human-Computer Interaction (HCI), Software Design",
    size=9.2,
)
row("Dr. Vishwanath Karad MIT World Peace University", "Pune, India")
subrow("B.Tech in Computer Science and Engineering. GPA: 3.8/4.00.", "Jul 2024")
pdf.ln(1)

# Skills
section("Skills")
skills = [
    ("Machine Learning & AI", "Generative AI, LLMs, Vector Databases, Prompt Engineering"),
    ("Libraries and Frameworks", "TensorFlow, scikit-learn, Pandas, NumPy, PyTerrier, Seaborn, Django, Flask"),
    ("Cloud and Tools", "AWS (Lambda, DynamoDB, S3, SQS), Amazon Bedrock, VS Code, Bootstrap, Android Studio, Linux, MacOS, Windows"),
    ("Programming and Databases", "Python, JavaScript, Java, HTML/CSS, Node.js, React.js, MySQL, MongoDB"),
]
for label, value in skills:
    pdf.set_font("Times", "B", 9.7)
    pdf.set_text_color(*NAVY)
    label_w = 52
    x0 = pdf.get_x()
    y0 = pdf.get_y()
    pdf.multi_cell(label_w, 4.8, _ascii(label + ":"))
    y1 = pdf.get_y()
    pdf.set_xy(x0 + label_w, y0)
    pdf.set_font("Times", "", 9.7)
    pdf.multi_cell(CONTENT_W - label_w, 4.8, _ascii(value))
    pdf.set_y(max(y1, pdf.get_y()))

# Experience
section("Experience")
row("Agentic AI Intern", "May 2026 – Aug 2026")
subrow("Tata Consultancy Services (TCS)", "Edison, NJ")
bullet(
    "Manual peer review of SQL report-logic changes took 24-48 hours per ticket across a team of 50-100, the "
    "top bottleneck in Prudential’s deployment pipeline; designed and built SuPRvisor, a serverless AI platform "
    "(AWS Lambda, DynamoDB, S3, SQS, Amazon Bedrock) to automate it."
)
bullet(
    "Built a multi-agent Lambda architecture and custom intake workflow to fully automate semantic SQL review, "
    "blank-data risk assessment, and executive review generation, replacing what had been a manual process."
)
bullet(
    "Implemented automated data-quality checks, report profiling, and metadata validation, generating structured "
    "Excel audit packages with remediation guidance in place of manual audits."
)
bullet(
    "Engineered DynamoDB-based persistence for workflow tracking, Bedrock response caching, and developer "
    "performance analytics, cutting per-ticket review time from 24-48 hours to 5-10 minutes — over a 99% "
    "reduction — while automating 100% of the review process."
)
pdf.ln(1.5)

row("Software Development Engineer", "Jan 2024 – Jul 2024")
subrow("FairShare IT Services", "Pune, India")
bullet(
    "Engineered Python predictive models (Pandas, TensorFlow, scikit-learn) to forecast prices for 100+ stocks "
    "from historical data, achieving 96% R² and 90% directional accuracy in backtesting."
)
bullet(
    "Automated data collection and candidate-stock screening pipelines via targeted web scraping (ElementTree) "
    "and report generation (Docx), removing manual research work in building the model’s input universe."
)
pdf.ln(1.5)

row("Research Co-Developer", "Jul 2022 – Mar 2023")
subrow("Skoda Auto Volkswagen Pvt. Ltd.", "Pune, India")
bullet(
    "Dealership service teams lacked consistent onboarding and performance tracking; collaborated on an 8-person "
    "team to build interactive training software and KPI-driven instructional modules adopted by 6 Service "
    "Managers, extending training to teams of 40-50 employees each (240+ employees reached)."
)

# Projects
section("Projects")
row("Oral Cavity Cancer Classification Model", "Sep 2025 – Present")
subrow("Research Intern", "")
bullet(
    "Developed an end-to-end Python pipeline using h5py to extract features from large-scale Whole Slide Images "
    "(WSI) and train a Logistic Regression classifier to distinguish tumor patches; processed up to 20 "
    "full-sized .svs files (6-8 GB per slide) yielding patch counts in the 10,000 range."
)
bullet(
    "Engineered data processing scripts mapping patch coordinates to pathological binary masks, automatically "
    "generating training labels via pixel-level tumor density thresholds."
)
bullet(
    "Built interpretability modules using PIL and NumPy to overlay color-coded prediction grids onto slide "
    "thumbnails, enabling visual verification of tumor classifications."
)
pdf.ln(1.5)

row("Unity ML-Agents: Gaming through Reinforcement Learning", "Jan 2024 – Jun 2024")
subrow("Team Leader", "")
bullet(
    "Developed a computer racing game integrating reinforcement learning via the Unity ML library to dynamically "
    "adapt non-playable characters (NPCs) to player behaviors."
)
bullet(
    "Simulated personalized challenges with an 87.5% success rate; presented and published the associated "
    "research paper at the IEEE 2nd WCONF 2024."
)

pdf.output("/Users/avaneesh12/Developer/portfolio/public/resume.pdf")
print("done")
