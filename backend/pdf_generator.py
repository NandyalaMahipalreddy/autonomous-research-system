import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import re

def clean_text(text):

    text = re.sub(r'#+\s*', '', text)
    text = text.replace("**", "")
    text = text.replace("|", " ")
    text = re.sub(r'<.*?>', '', text)

    text = text.replace("📌", "")
    text = text.replace("🤖", "")
    text = text.replace("🔎", "")
    text = text.replace("⚠", "")
    text = text.replace("🧠", "")
    text = text.replace("📊", "")
    text = text.replace("🔗", "")
    text = text.replace("✅", "")

    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    text = text.replace("---", "")

    return text


def generate_pdf(report_text, filename="research_report.pdf"):

    cleaned_report = clean_text(report_text)

    os.makedirs("reports", exist_ok=True)

    filepath = os.path.join("reports", filename)

    pdf = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []
    story.append(
        Paragraph(
        "<b>Autonomous Multi-Agent Research Report</b>",
        styles["Title"]
    )
)

    story.append(Spacer(1, 20))

    for line in cleaned_report.split("\n"):

        line = line.replace("<br>", "")
        line = line.replace("<br/>", "")
        line = line.replace("<br />", "")
        line = line.strip()

        if line:
            story.append(
                Paragraph(line, styles["Normal"])
            )

            story.append(
                Spacer(1, 8)
            )

    pdf.build(story)

    return f"reports/{filename}"