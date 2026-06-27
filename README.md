# Voice-to-PDF-Item-Report-Generator
A python application that converts voice input into a professionally formatted PDF item report using SpeechRecognition and ReportLab

# 🎤 Voice to PDF Item Report Generator

A Python-based application that converts spoken item details into a professionally formatted PDF report.

The application listens to your voice through the microphone, extracts the item name and price, stores multiple entries, and finally generates a PDF report automatically.

---

## ✨ Features

- Voice Recognition
- Automatic Item & Price Detection
- PDF Report Generation
- Multiple Item Support
- Stop Recording by Saying "exit"
- Clean PDF Layout

---

## Tech Stack

- Python 3
- SpeechRecognition
- PyAudio
- ReportLab

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Voice-to-PDF-Generator.git
```

Move into the project folder

```bash
cd Voice-to-PDF-Generator
```

Install dependencies

```bash
pip install SpeechRecognition
pip install PyAudio
pip install reportlab
```

---

## Run the Project

```bash
python voice.py
```

---

## Example Voice Inputs

```
Laptop 55000
```

```
Mouse 800
```

```
Keyboard 1500
```

Say

```
exit
```

to finish recording.

---

## Output

The program generates

```
Items_Report.pdf
```

Example

| S.No | Item | Price |
|------|------|-------|
|1|Laptop|Rs 55000|
|2|Mouse|Rs 800|
|3|Keyboard|Rs 1500|

---

## Project Structure

```
Voice-to-PDF-Generator/
│
├── voice.py
├── README.md
├── requirements.txt
└── Items_Report.pdf
```

---

## Future Improvements

- Streamlit GUI
- Export to Excel
- CSV Support
- Database Storage
- Offline Speech Recognition
- Invoice Generation
- Date & Time in Report
- Company Logo in PDF

---

## Author

Nek Sandha

