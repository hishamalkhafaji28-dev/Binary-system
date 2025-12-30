import tkinter as tk
from tkinter import messagebox, font


# --- دوال التحويل ---
def text_to_binary():
    text = entry.get()
    if not text:
        messagebox.showwarning("تنبيه", "يرجى إدخال نص أولاً!")
        return

    result = []

    if text.isdigit():  # كلها أرقام كرقم واحد
        result.append(bin(int(text))[2:])  # ثنائي كامل
    else:
        for char in text:
            if char.isdigit():  # رقم مفرد وسط نص
                result.append(bin(int(char))[2:])
            else:
                result.append(format(ord(char), '016b'))  # حرف عربي أو انجليزي

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ' '.join(result))


def binary_to_text():
    binary_input = entry.get()
    if not binary_input:
        messagebox.showwarning("تنبيه", "يرجى إدخال نص أولاً!")
        return
    try:
        result = []
        for b in binary_input.split():
            if all(c in '01' for c in b):
                # إذا طول البت > 4 نفترض حرف (Unicode) وإلا رقم
                if len(b) > 4:
                    result.append(chr(int(b, 2)))
                else:
                    result.append(str(int(b, 2)))
            else:
                raise ValueError
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, ''.join(result))
    except ValueError:
        messagebox.showerror("خطأ", "النص المدخل ليس نظام ثنائي صحيح!")


# --- إنشاء النافذة ---
root = tk.Tk()
root.title("محول النصوص والأرقام إلى ثنائي والعكس")
root.geometry("650x400")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# --- خطوط وألوان ---
title_font = font.Font(family="Arial", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)
btn_font = font.Font(family="Arial", size=12, weight="bold")
text_font = font.Font(family="Courier", size=11)

# --- عناصر الواجهة ---
title_label = tk.Label(root, text="محول النصوص والأرقام إلى ثنائي والعكس", font=title_font, bg="#1e1e2f", fg="#ffffff")
title_label.pack(pady=15)

entry_label = tk.Label(root, text="أدخل النص أو النظام الثنائي:", font=label_font, bg="#1e1e2f", fg="#cccccc")
entry_label.pack()

entry = tk.Entry(root, width=60, font=label_font, bg="#2e2e3e", fg="#ffffff", insertbackground="white")
entry.pack(pady=10, ipady=5)

# --- أزرار التحويل مع تأثير عند المرور بالماوس ---
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=10)


def on_enter(e, btn, color):
    btn['bg'] = color


def on_leave(e, btn, color):
    btn['bg'] = color


convert_to_binary_btn = tk.Button(button_frame, text="تحويل إلى ثنائي", font=btn_font, bg="#4CAF50", fg="white",
                                  width=15, command=text_to_binary)
convert_to_binary_btn.grid(row=0, column=0, padx=15)
convert_to_binary_btn.bind("<Enter>", lambda e: on_enter(e, convert_to_binary_btn, "#45a049"))
convert_to_binary_btn.bind("<Leave>", lambda e: on_leave(e, convert_to_binary_btn, "#4CAF50"))

convert_to_text_btn = tk.Button(button_frame, text="تحويل إلى نص", font=btn_font, bg="#2196F3", fg="white", width=15,
                                command=binary_to_text)
convert_to_text_btn.grid(row=0, column=1, padx=15)
convert_to_text_btn.bind("<Enter>", lambda e: on_enter(e, convert_to_text_btn, "#1e88e5"))
convert_to_text_btn.bind("<Leave>", lambda e: on_leave(e, convert_to_text_btn, "#2196F3"))

# --- مربع الناتج ---
output_label = tk.Label(root, text="الناتج:", font=label_font, bg="#1e1e2f", fg="#cccccc")
output_label.pack(pady=(15, 5))

output_text = tk.Text(root, height=6, width=75, font=text_font, bg="#2e2e3e", fg="#ffffff")
output_text.pack(pady=5)


# --- زر نسخ الناتج ---
def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END).strip())
    messagebox.showinfo("نسخ", "تم نسخ الناتج للحافظة!")


copy_btn = tk.Button(root, text="نسخ الناتج", font=btn_font, bg="#FF9800", fg="white", width=15, command=copy_output)
copy_btn.pack(pady=5)
copy_btn.bind("<Enter>", lambda e: on_enter(e, copy_btn, "#fb8c00"))
copy_btn.bind("<Leave>", lambda e: on_leave(e, copy_btn, "#FF9800"))


# --- زر مسح النصوص ---
def clear_all():
    entry.delete(0, tk.END)
    output_text.delete(1.0, tk.END)


clear_btn = tk.Button(root, text="مسح النصوص", font=btn_font, bg="#f44336", fg="white", width=15, command=clear_all)
clear_btn.pack(pady=5)
clear_btn.bind("<Enter>", lambda e: on_enter(e, clear_btn, "#e53935"))
clear_btn.bind("<Leave>", lambda e: on_leave(e, clear_btn, "#f44336"))

# --- تشغيل البرنامج ---
root.mainloop()
