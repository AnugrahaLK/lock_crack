import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import time
import threading
import winsound  # Windows beep sound

# Step 1: Ask user to set a 4-digit PIN
setup = tk.Tk()
setup.withdraw()
stored_password = simpledialog.askstring("Set PIN", "Enter a 4-digit phone PIN to simulate lock:", show="*")

# Validate input
if not stored_password or not stored_password.isdigit() or len(stored_password) != 4:
    messagebox.showerror("Invalid PIN", "PIN must be exactly 4 digits.")
    exit()

# Step 2: Brute-force cracker GUI
def start_crack_gui():
    crack = tk.Tk()
    crack.title("💣 Brute Force Cracker")
    crack.geometry("420x260")
    crack.configure(bg="black")

    tk.Label(crack, text="Brute-force in progress...", font=("Courier New", 13), fg="orange", bg="black").pack(pady=10)

    attempt_label = tk.Label(crack, text="Attempt: ", font=("Courier New", 12), fg="lime", bg="black")
    attempt_label.pack()

    progress = ttk.Progressbar(crack, orient="horizontal", length=300, mode="determinate", maximum=9999)
    progress.pack(pady=10)

    result_label = tk.Label(crack, text="", font=("Courier New", 12, "bold"), fg="red", bg="black")
    result_label.pack()

    # Watermark
    tk.Label(crack, text="🔐 Made by Anugraha", font=("Courier New", 8), fg="gray", bg="black")\
        .place(relx=1.0, rely=1.0, anchor='se', x=-5, y=-5)

    def run_crack():
        start_time = time.time()
        for i in range(10000):
            attempt = str(i).zfill(4)
            attempt_label.config(text=f"Attempt: {attempt}")
            progress['value'] = i
            crack.update()
            time.sleep(0.001)

            if attempt == stored_password:
                winsound.Beep(1000, 500)  # 🔊 Success sound
                elapsed = round(time.time() - start_time, 2)
                result_label.config(
                    text=f"💥 Cracked PIN: {attempt}\n🕒 Time: {elapsed} sec\n🧠 Attempts: {i + 1}"
                )
                progress['value'] = i
                break

    threading.Thread(target=run_crack).start()
    crack.mainloop()

# Step 3: Lock screen GUI
def show_lock_screen():
    def check_pin():
        entered = entry.get()
        if entered == stored_password:
            messagebox.showinfo("Access Granted", "🔓 Correct PIN!\nLaunching Brute-Force Simulation...")
            root.destroy()
            start_crack_gui()
        else:
            messagebox.showerror("Access Denied", "❌ Wrong PIN")

    root = tk.Tk()
    root.title("🔐 Android Lock Screen (Simulation)")
    root.geometry("300x200")
    root.configure(bg="black")

    tk.Label(root, text="Enter your PIN to unlock:", font=("Courier New", 12), fg="lime", bg="black").pack(pady=15)
    entry = tk.Entry(root, font=("Courier New", 14), show="*", justify='center')
    entry.pack()

    tk.Button(root, text="Unlock", font=("Courier New", 12), bg="red", fg="white", command=check_pin).pack(pady=10)

    # Watermark
    tk.Label(root, text="🔐 Made by Anugraha", font=("Courier New", 8), fg="gray", bg="black")\
        .place(relx=1.0, rely=1.0, anchor='se', x=-5, y=-5)

    root.mainloop()

# Run the full simulation
show_lock_screen()
