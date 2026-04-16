# 🔥 AI DDR Report Generator

## 📌 Overview

This project converts Inspection and Thermal Reports into a structured **Detailed Diagnostic Report (DDR)** using intelligent data processing and reasoning.

---

## 🚀 Features

* Upload Inspection & Thermal PDFs
* Extract issues (dampness, cracks, leakage)
* Combine inspection + thermal data
* Generate structured DDR report
* Export as PDF
* Display extracted images

---

## 📸 Screenshots

### 🖥️ 1. User Interface

<img width="1231" height="877" alt="Screenshot 2026-04-16 231446" src="https://github.com/user-attachments/assets/c6c7fee2-bbd5-4e8c-ae76-8017776c4cb6" />


---

### 📄 2. DDR Report Output

<img width="990" height="849" alt="Screenshot 2026-04-16 231508" src="https://github.com/user-attachments/assets/0f86f375-1833-4e34-b3fa-7f73172c6dac" />


---

### 🖼️ 3. Extracted Images

<img width="1024" height="846" alt="Screenshot 2026-04-16 231520" src="https://github.com/user-attachments/assets/e13d7d98-25f9-41fa-a59d-bbfffc4a54a6" />

<img width="808" height="857" alt="Screenshot 2026-04-16 231531" src="https://github.com/user-attachments/assets/da51beed-9fe8-4d3c-81e1-742df544704f" />

---

## 🧠 Working Logic

* Detect dampness from inspection report
* Identify temperature variation from thermal report
* Combine both to confirm moisture
* Map issues to root causes

---

## 🛠️ Tech Stack

* Python
* Streamlit
* PyMuPDF
* ReportLab

---

## ▶️ Run Project

```bash
pip install streamlit pymupdf reportlab pillow
streamlit run app.py
```

---

## ⚠️ Limitations

* Rule-based logic (keyword-based)
* Basic image mapping

---

## 🔮 Future Improvements

* NLP-based extraction
* Smart image mapping
* Advanced reasoning

---

## 👨‍💻 Author

Swapnil Ware
