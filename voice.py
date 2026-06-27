
# Voice to PDF Item Report Generator


# Install required libraries:
# pip install SpeechRecognition
# pip install pyaudio
# pip install reportlab

# Import required libraries
import speech_recognition as sr
from reportlab.pdfgen import canvas

# Create a Speech Recognizer object

r = sr.Recognizer()

# List to store (item_name, price)
items = []


# Function to listen to microphone

def listen():

    # Open microphone
    with sr.Microphone() as source:

        print("\n🎤 Speak an item with price")
        print("Example: Laptop 55000")
        print("Say 'exit' when finished.\n")

        # Reduce background noise
        r.adjust_for_ambient_noise(source, duration=1)

        # Listen to user's voice
        audio = r.listen(source)

    try:
        # Convert speech to text
        text = r.recognize_google(audio)

        print("You said:", text)

        return text.strip()

    except sr.UnknownValueError:
        print("Could not understand your voice.")
        return ""

    except sr.RequestError:
        print("Internet connection error.")
        return ""


# Keep listening until user says "exit"


while True:

    text = listen()

    if not text:
        continue

    # Stop recording
    if text.lower() == "exit":
        break

    
    # Split sentence into words
    
    words = text.split()

    price = ""

    # Find numeric value (price)
    for word in words:

        if word.replace(".", "").isdigit():
            price = word
            break

    # Remove price and "Rs" from item name
    item_name = " ".join(
        word for word in words
        if not word.replace(".", "").isdigit()
        and word.lower() != "rs"
    )

    # Store data
    if price:

        items.append((item_name, price))

        print(f" Added: {item_name} - Rs {price}")

    else:

        print(" Price not found. Please try again.")


# Generate PDF Report


pdf = canvas.Canvas("Items_Report.pdf")

# Title
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(180, 800, "Items Report")

# Heading
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, 770, "S.No")
pdf.drawString(100, 770, "Item")
pdf.drawString(350, 770, "Price")

# Start writing items
y = 740

pdf.setFont("Helvetica", 12)

for i, (name, price) in enumerate(items, start=1):

    pdf.drawString(50, y, str(i))
    pdf.drawString(100, y, name)
    pdf.drawString(350, y, f"Rs {price}")

    y -= 20

# Save PDF
pdf.save()

print("\n-----------------------------------")
print("✅ PDF Saved Successfully!")
print("📄 File Name: Items_Report.pdf")
print("-------------------------------------")
