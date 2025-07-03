# 💣 Brute-Force PIN Cracker Simulator 🔐

A Python GUI simulation of brute-force PIN cracking — built for ethical hacking education and cybersecurity awareness. This app mimics how weak 4-digit PINs can be cracked using brute-force techniques.  

🛠️ Created by **Anugraha** 

---

## 🚀 Features

- 🔒 Android-style **lock screen**
- 📥 Custom 4-digit PIN input
- 🧠 Live **brute-force attempt simulation**
- 📊 Progress bar showing cracking progress
- 🔊 **Beep sound** alert on success
- 🪪 Watermark: "Made by Anugraha"

## 🧪 How It Works

1. You set a 4-digit PIN when the app starts
2. The lock screen asks for that PIN
3. When entered correctly, the simulation starts:
   - Live cracking of the PIN from 0000 to 9999
   - GUI progress bar and attempt counter
   - Sound alert when cracked

## 💡 Educational Purpose

This tool is intended **for educational and ethical use only**.  
It demonstrates why short PINs are weak and helps learners understand brute-force logic safely.

---

## 🧰 Built With

- Python 3
- Tkinter (GUI)
- winsound (for beep alert)
- `threading` for smooth GUI performance

---

## 🔧 Run It Locally

1. Clone this repo or download the `.py` file
2. Run:
   ```bash
   python gui_cracker_final.py
