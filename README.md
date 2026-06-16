# 📱 Engineering Assistant Mobile Simulator Application (Python GUI)

A lightweight, robust desktop application that simulates a mobile assistant interface designed for mechanical engineers, field technicians, and R&D specialists. This project bypasses heavy visual low-code ecosystems by utilizing Python's native high-stability framework, implementing a zero-dependency architecture.

---

## 🚀 Key Modules & Embedded Engineering Logic

### ⚡ 1. Unit Conversion Hub
* **Pressure Translation:** Performs high-precision, localized mathematical conversions between MegaPascals and Pounds per Square Inch ($1 \text{ MPa} \rightarrow 145.0377 \text{ Psi}$).
* **Dynamic Validation:** Features an integrated real-time text listener with input filtering to catch structural formatting anomalies or empty queries without system crashes.

### 📊 2. Materials Properties Database
* Provides instant lookups for structural engineering alloys and metals, dynamically tracking core thermodynamic and physical constraints:
  * **Structural Steel:** Density ($7850 \text{ kg/m³}$), Elastic Modulus ($200 \text{ GPa}$), Yield Strength ($250 \text{ MPa}$).
  * **Aluminum Alloy:** Density ($2700 \text{ kg/m³}$), Elastic Modulus ($70 \text{ GPa}$), Yield Strength ($250 \text{ MPa}$).
  * **Titanium (Grade 5):** Density ($4430 \text{ kg/m³}$), Elastic Modulus ($114 \text{ GPa}$), Yield Strength ($880 \text{ MPa}$).

---

## 🛠️ Software Stack & UI/UX Design
* **Language:** Python 3.x (Fully compatible with Python 3.14+)
* **Core Engine:** Native `Tkinter` & `ttk` (Component-Driven Event Lifecycle)
* **Visual Theme:** Custom **Dracula / Tokyo-Night inspired Dark Mode** layout featuring explicit frame boundaries, custom hexadecimal padding (`#1E1E2E` and `#252538`), and localized typography rendering.
