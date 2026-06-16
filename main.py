import tkinter as tk
from tkinter import ttk

# --- HESAPLAMA MANTIKLARI ---
def convert_pressure():
    try:
        mpa = float(entry_mpa.get())
        psi = mpa * 145.0377
        label_psi_result.config(text=f"Sonuç: {psi:.2f} Psi", fg="#4EE880") # Hata veren renk kodu düzeltildi (#4EE880)
    except ValueError:
        label_psi_result.config(text="Lütfen geçerli bir sayı girin!", fg="#FF6B6B")

def show_material(event):
    selected = combo_material.get()
    if selected == "Alüminyum Alaşımı":
        label_mat_props.config(text="Yoğunluk: 2700 kg/m³\nElastisite Modülü: 70 GPa\nAkma Dayanımı: 250 MPa")
    elif selected == "Yapısal Çelik":
        label_mat_props.config(text="Yoğunluk: 7850 kg/m³\nElastisite Modülü: 200 GPa\nAkma Dayanımı: 250 MPa")
    elif selected == "Titanyum (Grade 5)":
        label_mat_props.config(text="Yoğunluk: 4430 kg/m³\nElastisite Modülü: 114 GPa\nAkma Dayanımı: 880 MPa")

# --- ARAYÜZ TASARIMI (MOBİL PENCERE) ---
root = tk.Tk()
root.title("Engineering Assistant")
root.geometry("360x600") # Tam telefon boyutu
root.resizable(False, False)
root.configure(bg="#1E1E2E") # Modern koyu tema arka planı

# Stil Ayarları
style = ttk.Style()
style.theme_use('clam')

# Başlık
label_title = tk.Label(root, text="MÜHENDİSLİK ASİSTANI", font=("Arial", 16, "bold"), bg="#1E1E2E", fg="#89B4FA")
label_title.pack(pady=20)

# --- ⚡ BİRİM DÖNÜŞTÜRÜCÜ ÇERÇEVESİ ---
frame_unit = tk.LabelFrame(root, text=" ⚡ Birim Dönüştürücü Hub ", font=("Arial", 11, "bold"), bg="#252538", fg="#CDD6F4", bd=2, relief="groove")
frame_unit.pack(pady=15, padx=20, fill="both")

label_mpa = tk.Label(frame_unit, text="Basınç Değeri (MPa):", font=("Arial", 10), bg="#252538", fg="#A6ADC8")
label_mpa.pack(pady=5)

entry_mpa = tk.Entry(frame_unit, font=("Arial", 11), justify="center", width=15)
entry_mpa.insert(0, "1")
entry_mpa.pack(pady=5)

btn_convert = tk.Button(frame_unit, text="MPa -> Psi Dönüştür", font=("Arial", 10, "bold"), bg="#89B4FA", fg="#1E1E2E", activebackground="#B4BEFE", command=convert_pressure, relief="flat", height=1, width=20)
btn_convert.pack(pady=10)

label_psi_result = tk.Label(frame_unit, text="Sonuç: 145.04 Psi", font=("Arial", 11, "bold"), bg="#252538", fg="#4EE880") # Hata veren renk kodu düzeltildi (#4EE880)
label_psi_result.pack(pady=5)


# --- 📊 MALZEME VERİ TABANI ÇERÇEVESİ ---
frame_mat = tk.LabelFrame(root, text=" 📊 Malzeme Veri Tabanı ", font=("Arial", 11, "bold"), bg="#252538", fg="#CDD6F4", bd=2, relief="groove")
frame_mat.pack(pady=15, padx=20, fill="both")

label_select = tk.Label(frame_mat, text="Malzeme Seçin:", font=("Arial", 10), bg="#252538", fg="#A6ADC8")
label_select.pack(pady=5)

combo_material = ttk.Combobox(frame_mat, values=["Alüminyum Alaşımı", "Yapısal Çelik", "Titanyum (Grade 5)"], state="readonly", width=22)
combo_material.set("Alüminyum Alaşımı")
combo_material.bind("<<ComboboxSelected>>", show_material)
combo_material.pack(pady=5)

label_mat_props = tk.Label(frame_mat, text="Yoğunluk: 2700 kg/m³\nElastisite Modülü: 70 GPa\nAkma Dayanımı: 250 MPa", font=("Consolas", 10), bg="#252538", fg="#BAC2DE", justify="left")
label_mat_props.pack(pady=10)

root.mainloop()