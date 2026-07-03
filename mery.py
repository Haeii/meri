import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup

def islem():
    terim = entry.get()
    
    if len(terim) < 4:
        messagebox.showerror("Hata", "Lütfen en az 4 karakter girin.")
        return
        
    ekran.delete(1.0, tk.END)
    ekran.insert(tk.END, "5 kamyon yola çıktık geliyoruz.\n")
    
    try:
        r = requests.get(f"https://html.duckduckgo.com/html/?q={terim}", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        sonuclar = soup.find_all("a", class_="result__a")
        
        ekran.delete(1.0, tk.END)
        
        if not sonuclar:
            ekran.insert(tk.END, "yazdığın şeyi beyenmemiş.")
            return

        ekran.insert(tk.END, "Şunları söyledi:\n" + "-"*30 + "\n")
        for x in sonuclar[:4]:
            ekran.insert(tk.END, f"> {x.text.strip()}\n\n")
        
        ekran.insert(tk.END, "bulduğu haberler bu kadarmış.\n")
            
    except:
        ekran.delete(1.0, tk.END)
        ekran.insert(tk.END, "galiba uyuyor(zaten geç uyanır).(internet bağlantını kontrol et.)")

root = tk.Tk()
root.title("mery")
root.geometry("550x600")

tk.Label(root, text="what are you thinking?", font=("Courier", 11)).pack(pady=15)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Sorgula", command=islem, bg="#ffcc00").pack(pady=10)

ekran = scrolledtext.ScrolledText(root, width=60, height=20)
ekran.pack(pady=10)

root.mainloop()