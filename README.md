# Circuits

# RC Low-Pass Filter for Noise Removal (Analog + FFT Verification)

This project demonstrates the **design, mathematical analysis, and simulation of an RC low-pass filter** for removing high-frequency noise from a signal. The filter is verified using **time-domain analysis and FFT-based frequency-domain analysis** in LTspice and Python.

---

## 📌 Project Objectives

* To design an **RC low-pass filter** for a cutoff frequency of **10 Hz**
* To apply a **mixed noisy signal** as the input
* To observe **noise attenuation in time domain**
* To verify filtering using **FFT analysis**
* To validate theoretical predictions through simulation

---

## 🧠 Theory Overview

An RC low-pass filter consists of:

* A **resistor (R)** in series with the input
* A **capacitor (C)** connected to ground
* Output taken across the **capacitor**

### ✅ Transfer Function

[
H(j\omega) = \frac{1}{1 + j\omega RC}
]

### ✅ Cutoff Frequency

[
f_c = \frac{1}{2\pi RC}
]

---

## ⚙️ Design Specifications

| Parameter                | Value      |
| ------------------------ | ---------- |
| Desired cutoff frequency | **10 Hz**  |
| Signal frequency         | **5 Hz**   |
| Noise frequency          | **50 Hz**  |
| Resistor                 | **10 kΩ**  |
| Capacitor                | **1.5 μF** |

---

## 🔌 Input Signal Used

A mixed-frequency test signal is applied:

[
V(t) = \sin(2\pi \cdot 5t) + 0.3\sin(2\pi \cdot 50t)
]

This represents a useful low-frequency signal corrupted by high-frequency noise.

---

## 🧪 Software Tools Used

* **LTspice / NGSpice** – circuit simulation + FFT
* **Python (NumPy, SciPy, Matplotlib)** – FFT verification
* **LaTeX** – report writing
* **CircuitikZ** – circuit diagram

---

## ▶️ How to Run the LTspice Simulation

1. Open **LTspice**
2. Build the RC circuit:

   * Series **R = 10 kΩ**
   * Shunt **C = 1.5 μF**
3. Use a **Behavioral Voltage Source (BV)** and enter:

   ```
   V = sin(2*pi*5*time) + 0.3*sin(2*pi*50*time)
   ```
4. Add simulation command:

   ```
   .tran 2
   .save V(in) V(out)
   ```
5. Run the simulation
6. Plot:

   * `V(in)` → Input
   * `V(out)` → Filtered Output
7. Use **View → FFT** to verify frequency suppression

---

## 📊 Expected Results

* In **time domain**:

  * Input → noisy waveform
  * Output → smooth, low-frequency waveform
* In **frequency domain (FFT)**:

  * 5 Hz component → preserved ✅
  * 50 Hz component → strongly attenuated ✅

---

## 📄 Documentation

* ✅ Full mathematical derivation
* ✅ CircuitikZ diagram
* ✅ LTspice simulation
* ✅ FFT verification
* ✅ LaTeX project report included

---

## 🚀 Future Scope

* RC **high-pass and band-pass filters**
* Digital **Butterworth and FIR filters**
* Hardware implementation on a **breadboard**
* Sensor signal conditioning
* Control systems applications

---

## 👤 Author

**Bhargav Krishnamurthy**
First-Year Electrical Engineering Student
IIT Hyderabad

---

## ✅ License

This project is intended for **academic and learning purposes**.
All simulations and derivations are student-generated.

---

If you want, I can also:

✅ Add a **Python usage section**
✅ Convert this into a **GitHub-style professional README with badges**
✅ Add a **project folder structure**

Just tell me what you want to add next 😄
