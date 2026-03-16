import tkinter as tk
from tkinter import ttk, messagebox
import time

def calculate_stats(start_time, end_time, text_length, errors):
    time_taken = end_time - start_time
    if time_taken <= 0: time_taken = 0.1
    cpm = (text_length / time_taken) * 60
    
    # Calculate ms per char
    avg_ms = (time_taken / text_length) * 1000
    min_ms = max(50, int(avg_ms * 0.7))
    max_ms = int(avg_ms * 1.3)
    
    # Calculate error rate per 500 chars
    err_rate = int((errors / text_length) * 500) if text_length > 0 else 0
    return min_ms, max_ms, err_rate

class TypingTestWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tipp-Leistungstest")
        self.geometry("600x400")
        self.parent = parent
        self.configure(bg="#f4f4f4")
        
        self.sample_text = "Die künstliche Intelligenz hilft uns dabei, viele alltägliche Aufgaben zu automatisieren und unsere Produktivität zu steigern."
        self.start_time = 0
        self.errors = 0
        self.started = False
        
        tk.Label(self, text="Schreibe diesen Text ab:", font=("Segoe UI", 12, "bold"), bg="#f4f4f4").pack(pady=10)
        
        self.text_display = tk.Text(self, height=4, width=60, font=("Segoe UI", 11), bg="#e8e8e8", state=tk.DISABLED, wrap=tk.WORD)
        self.text_display.pack(pady=5)
        self.text_display.config(state=tk.NORMAL)
        self.text_display.insert(tk.END, self.sample_text)
        self.text_display.config(state=tk.DISABLED)
        
        tk.Label(self, text="Hier tippen:", font=("Segoe UI", 10), bg="#f4f4f4").pack(pady=5)
        
        self.input_entry = tk.Entry(self, width=60, font=("Segoe UI", 11))
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<Key>", self.on_key)
        self.input_entry.bind("<KeyRelease>", self.check_completion)
        self.input_entry.focus()
        
        self.status_label = tk.Label(self, text="", font=("Segoe UI", 10), bg="#f4f4f4")
        self.status_label.pack(pady=10)

    def on_key(self, event):
        if not self.started and event.keysym not in ['Shift_L', 'Shift_R', 'Caps_Lock', 'Tab', 'Return']:
            self.started = True
            self.start_time = time.time()
            
        if event.keysym == 'BackSpace':
            self.errors += 1

    def check_completion(self, event):
        typed = self.input_entry.get()
        if not self.sample_text.startswith(typed):
            self.input_entry.config(bg="#ffcccc")
        else:
            self.input_entry.config(bg="white")
            
        if typed == self.sample_text:
            end_time = time.time()
            self.finish_test(end_time)
            
    def finish_test(self, end_time):
        min_ms, max_ms, err_rate = calculate_stats(self.start_time, end_time, len(self.sample_text), self.errors)
        
        self.status_label.config(text=f"Fertig! Min: {min_ms}ms, Max: {max_ms}ms, Fehler: {err_rate}/500Z", fg="green")
        
        # Set values in parent window
        self.parent.min_speed_var.set(str(min_ms))
        self.parent.max_speed_var.set(str(max_ms))
        self.parent.errors_var.set(str(err_rate))
        
        messagebox.showinfo("Test Abgeschlossen", "Deine Leistung wurde gemessen! Die Einstellungen wurden in das Hauptfenster übernommen.", parent=self)
        self.destroy()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typewriter Bot Generator Pro")
        self.geometry("680x750")
        self.configure(bg="#ffffff")
        
        style = ttk.Style(self)
        style.theme_use('clam')
        
        self.min_speed_var = tk.StringVar(value="180")
        self.max_speed_var = tk.StringVar(value="300")
        self.errors_var = tk.StringVar(value="4")
        
        self.build_ui()
        
    def build_ui(self):
        header = tk.Label(self, text="🤖 Typewriter Bot Setup", font=("Segoe UI", 20, "bold"), bg="#ffffff", fg="#333333")
        header.pack(pady=(20, 10))
        
        # Calibration section
        cal_frame = tk.Frame(self, bg="#f9f9f9", bd=1, relief=tk.SOLID)
        cal_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(cal_frame, text="Lass deinen Speed automatisch ermitteln:", font=("Segoe UI", 11), bg="#f9f9f9").pack(pady=(10, 5))
        
        btn_cal_frame = tk.Frame(cal_frame, bg="#f9f9f9")
        btn_cal_frame.pack(pady=(0, 15))
        
        test_btn = tk.Button(btn_cal_frame, text="🎯 Tipp-Leistungstest", 
                             command=self.open_test, bg="#9C27B0", fg="white", font=("Segoe UI", 11, "bold"),
                             relief=tk.FLAT, padx=15, pady=8, cursor="hand2")
        test_btn.grid(row=0, column=0, padx=5)

        help_btn = tk.Button(btn_cal_frame, text="❓ Anleitung", 
                             command=self.open_help, bg="#FF9800", fg="white", font=("Segoe UI", 11, "bold"),
                             relief=tk.FLAT, padx=15, pady=8, cursor="hand2")
        help_btn.grid(row=0, column=1, padx=5)
        
        # Settings frame
        frame = tk.Frame(self, bg="#ffffff")
        frame.pack(pady=15)
        
        tk.Label(frame, text="Minimale Schreibpause (ms):", font=("Segoe UI", 11), bg="#ffffff").grid(row=0, column=0, sticky="e", padx=10, pady=10)
        ttk.Entry(frame, textvariable=self.min_speed_var, width=15, font=("Segoe UI", 11)).grid(row=0, column=1, sticky="w")
        
        tk.Label(frame, text="Maximale Schreibpause (ms):", font=("Segoe UI", 11), bg="#ffffff").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        ttk.Entry(frame, textvariable=self.max_speed_var, width=15, font=("Segoe UI", 11)).grid(row=1, column=1, sticky="w")
        
        tk.Label(frame, text="Fehler auf 500 Zeichen:", font=("Segoe UI", 11), bg="#ffffff").grid(row=2, column=0, sticky="e", padx=10, pady=10)
        ttk.Entry(frame, textvariable=self.errors_var, width=15, font=("Segoe UI", 11)).grid(row=2, column=1, sticky="w")
        
        btn_frame = tk.Frame(self, bg="#ffffff")
        btn_frame.pack(pady=15)
        
        gen_btn = tk.Button(btn_frame, text="⚡ Code Generieren", command=self.generate_script, bg="#4CAF50", fg="white", font=("Segoe UI", 11, "bold"), relief=tk.FLAT, padx=15, pady=8, cursor="hand2")
        gen_btn.grid(row=0, column=0, padx=10)
        
        copy_btn = tk.Button(btn_frame, text="📋 Code Kopieren", command=self.copy_to_clipboard, bg="#2196F3", fg="white", font=("Segoe UI", 11, "bold"), relief=tk.FLAT, padx=15, pady=8, cursor="hand2")
        copy_btn.grid(row=0, column=1, padx=10)
        
        tk.Label(self, text="Fertiger JavaScript Code (Für F12 Konsole):", font=("Segoe UI", 10, "bold"), bg="#ffffff").pack(pady=5)
        
        self.output_text = tk.Text(self, height=18, width=78, font=("Consolas", 10), bg="#f4f6f8", bd=1, relief=tk.SOLID)
        self.output_text.pack(pady=5, padx=20)

    def open_test(self):
        TypingTestWindow(self)

    def open_help(self):
        help_win = tk.Toplevel(self)
        help_win.title("Wie funktioniert das?")
        help_win.geometry("550x500")
        help_win.configure(bg="#ffffff")
        
        tk.Label(help_win, text="📖 Schritt-für-Schritt Anleitung", font=("Segoe UI", 14, "bold"), bg="#ffffff").pack(pady=15)
        
        steps = [
            "1. Kalibrierung (Empfohlen)\nKlicke auf den violetten Button 'Tipp-Leistungstest'. Tippe den\nvorgegebenen Text ab. Das Tool berechnet deine echte\nTippgeschwindigkeit und Fehlerquote und trägt diese Werte\nautomatisch ein. Das macht den Bot realistischer!\n",
            "2. Code Generieren\nKlicke auf den grünen Button 'Code Generieren'. Das Programm\nerstellt nun einen maßgeschneiderten JavaScript-Code,\nbasierend auf deinen Zeiten und Fehlern.\n",
            "3. Code Kopieren\nKlicke auf den blauen Button 'Code Kopieren', um den Text\nin deine Zwischenablage zu speichern.\n",
            "4. Bot starten (Auf der Webseite)\n- Öffne im Browser die Typewriter.at Webseite und starte eine Übung.\n- Drücke F12, um die Entwicklerkonsole zu öffnen.\n- Wähle den Reiter 'Konsole' (Console).\n- Klicke in das leere Eingabefeld unten (oder das >>> Zeichen).\n- Drücke Strg+V, um den kopierten Code einzufügen.\n- Drücke Enter, um das Skript zu starten.\n- Zurücklehnen und zuschauen! 😎"
        ]
        
        text_widget = tk.Text(help_win, font=("Segoe UI", 11), bg="#f4f6f8", relief=tk.FLAT, padx=15, pady=15, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        for step in steps:
            text_widget.insert(tk.END, step + "\n")
        
        text_widget.config(state=tk.DISABLED)

    def generate_script(self):
        try:
            min_speed = int(self.min_speed_var.get())
            max_speed = int(self.max_speed_var.get())
            errors = int(self.errors_var.get())
        except ValueError:
            messagebox.showerror("Fehler", "Bitte nur ganze Zahlen eingeben!")
            return

        error_probability = errors / 500.0
        speed_diff = max(1, max_speed - min_speed)

        js_template = f"""(function autoType() {{
    console.log("🚀 Auto-Typer gestartet...");

    function sim(char) {{
        const c = char.charCodeAt(0);
        const e = {{ key: char, keyCode: c, which: c, bubbles: true }};

        document.dispatchEvent(new KeyboardEvent('keydown', e));
        document.dispatchEvent(new KeyboardEvent('keypress', e));
        
        const inp = document.getElementById('input_area') || document.activeElement;
        if (inp && inp.value !== undefined) {{
            inp.value += char;
            inp.dispatchEvent(new Event('input', {{ bubbles: true }}));
        }}
        document.dispatchEvent(new KeyboardEvent('keyup', e));
    }}

    function typeNext() {{
        const box = document.getElementById('text_todo_1');
        if (!box || !box.textContent) return console.log("✅ Fertig!");

        const char = box.textContent.charAt(0).replace(/\\u00a0/g, " ");
        let speed = Math.floor(Math.random() * {speed_diff} + {min_speed});
        
        if (Math.random() < {error_probability:.4f}) {{
            sim(String.fromCharCode(97 + Math.floor(Math.random() * 26)));
            setTimeout(() => {{ sim(char); step(char, speed); }}, Math.random() * 150 + 250);
        }} else {{
            sim(char);
            step(char, speed);
        }}
    }}

    function step(char, speed) {{
        if (/^[.,!?]$/.test(char)) speed += Math.random() * 200 + 150;
        setTimeout(typeNext, speed);
    }}
    
    typeNext();
}})();"""

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, js_template)
        
    def copy_to_clipboard(self):
        script_content = self.output_text.get(1.0, tk.END).strip()
        if script_content:
            self.clipboard_clear()
            self.clipboard_append(script_content)
            self.update() 
            messagebox.showinfo("Kopiert!", "Der Code wurde in die Zwischenablage kopiert.")
        else:
            messagebox.showwarning("Leer", "Generiere zuerst den Code, bevor du ihn kopierst!")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
