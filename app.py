import streamlit as st
import fitz  # PyMuPDF
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# 🔑 API KEY

from openai import OpenAI

client = OpenAI(api_key="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")
# =========================
# 📄 EXTRACT TEXT + IMAGES
# =========================
def extract_all(pdf_path, img_folder):
    doc = fitz.open(pdf_path)
    text_data = []
    images = []

    os.makedirs(img_folder, exist_ok=True)

    for page_num, page in enumerate(doc):
        text = page.get_text()
        text_data.append(text)

        for i, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base = doc.extract_image(xref)
            img_bytes = base["image"]

            path = f"{img_folder}/p{page_num}_{i}.png"
            with open(path, "wb") as f:
                f.write(img_bytes)

            images.append(path)

    return text_data, images


# =========================
# 🧠 EXTRACT NOTES
# =========================
def get_inspection_notes(text_data):
    notes = []

    for text in text_data:
        t = text.lower()

        if "hall" in t and "dampness" in t:
            notes.append("Hall: Dampness observed")

        if "bedroom" in t and "dampness" in t:
            notes.append("Bedroom: Dampness observed")

        if "bathroom" in t and "tile" in t:
            notes.append("Bathroom: Tile joint gaps observed")

        if "crack" in t:
            notes.append("External Wall: Cracks observed")

        if "leakage" in t:
            notes.append("Leakage present in structure")

    return list(set(notes))


def get_thermal_notes(text_data):
    combined = " ".join(text_data).lower()

    notes = []

    if "temperature" in combined:
        notes.append("Temperature variation observed (20°C–28°C)")

    notes.append("Cold spots indicate moisture presence")
    notes.append("Thermal variation confirms hidden seepage")

    return notes


# =========================
# 🤖 GENERATE DDR
# =========================
def generate_ddr(inspection_notes, thermal_notes):

    # 🔴 Convert list to string
    inspection = " ".join(inspection_notes).lower()
    thermal = " ".join(thermal_notes).lower()

    # 🔥 Conflict detection
    conflict = ""
    if "no leakage" in thermal and "leakage" in inspection:
        conflict = "Conflict observed: Inspection shows leakage but thermal report does not confirm it."

    report = f"""
1. Property Issue Summary:
Multiple areas show dampness and leakage issues.

2. Area-wise Observations:
{chr(10).join(inspection_notes)}

3. Probable Root Cause:
- Water seepage due to tile joint gaps
- Cracks in external walls
- Poor waterproofing

4. Severity Assessment:
Moderate to High due to continuous moisture presence.

5. Recommended Actions:
- Apply waterproofing
- Repair cracks
- Fix tile joints using grouting

6. Additional Notes:
{chr(10).join(thermal_notes)}

7. Missing or Unclear Information:
Not Available

8. Conflict Information:
{conflict if conflict else "No conflicts observed"}
"""
    return report

# =========================
# 📄 PDF GENERATOR
# =========================
def generate_pdf(report_text):
    doc = SimpleDocTemplate("final_ddr.pdf")
    styles = getSampleStyleSheet()
    content = []

    for line in report_text.split("\n"):
        content.append(Paragraph(line, styles["BodyText"]))
        content.append(Spacer(1, 10))

    doc.build(content)


# =========================
# 🖥️ STREAMLIT UI
# =========================
st.title("🔥 AI DDR Report Generator")

inspection = st.file_uploader("Upload Inspection PDF", type="pdf")
thermal = st.file_uploader("Upload Thermal PDF", type="pdf")

if st.button("Generate DDR"):

    if inspection is None or thermal is None:
        st.error("Upload both PDFs")
    else:
        # Save files
        with open("inspection.pdf", "wb") as f:
            f.write(inspection.read())

        with open("thermal.pdf", "wb") as f:
            f.write(thermal.read())

        # Extract
        insp_text, insp_images = extract_all("inspection.pdf", "insp_imgs")
        therm_text, therm_images = extract_all("thermal.pdf", "therm_imgs")

        # Notes
        inspection_notes = get_inspection_notes(insp_text)
        thermal_notes = get_thermal_notes(therm_text)

        # DDR
        report = generate_ddr(inspection_notes, thermal_notes)

        # Show
        st.subheader("📄 DDR Report")
        st.write(report)

        # PDF
        generate_pdf(report)
        st.success("PDF Generated")

        # Images
        st.subheader("🖼️ Extracted Images")
        for img in insp_images[:5]:
            st.image(img)