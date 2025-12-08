# Circuits

# RC Low-Pass Filter for Noise Removal (Analog + FFT Verification)

This project demonstrates the **design, mathematical analysis, and simulation of an RC low-pass filter** for removing high-frequency noise from a signal. The filter is verified using **time-domain analysis and FFT-based frequency-domain analysis** in LTspice and Python.

---

## Project Objectives

* To design an **RC low-pass filter** for a cutoff frequency of **10 Hz**
* To apply a **mixed noisy signal** as the input
* To observe **noise attenuation in time domain**
* To verify filtering using **FFT analysis**
* To validate theoretical predictions through simulation

---

## Theory Overview

An RC low-pass filter consists of:

* A **resistor (R)** in series with the input
* A **capacitor (C)** connected to ground
* Output taken across the **capacitor**

### Transfer Function

H(jω) = 1 / (1 + jωRC)


### Cutoff Frequency

f_c = 1 / (2πRC)


---

## Design Specifications

| Parameter                | Value      |
| ------------------------ | ---------- |
| Desired cutoff frequency | **10 Hz**  |
| Signal frequency         | **5 Hz**   |
| Noise frequency          | **50 Hz**  |
| Resistor                 | **10 kΩ**  |
| Capacitor                | **1.5 μF** |

---

## Input Signal Used

A mixed-frequency test signal is applied:

V(t) = sin(2π·5t) + 0.3·sin(2π·50t)


This represents a useful low-frequency signal corrupted by high-frequency noise.

---

## Software Tools Used

* **LTspice / NGSpice** – circuit simulation + FFT
* **Python (NumPy, SciPy, Matplotlib)** – FFT verification
* **LaTeX** – report writing
* **CircuitikZ** – circuit diagram

---


## Expected Results

* In **time domain**:

  * Input → noisy waveform
  * Output → smooth, low-frequency waveform
* In **frequency domain (FFT)**:

  * 5 Hz component → preserved 
  * 50 Hz component → diminished

---

## Documentation

*  Full mathematical derivation
*  CircuitikZ diagram
*  LTspice simulation
*  FFT verification
*  LaTeX project report included

---

## Author

**Bhargav Krishnamurthy**
First-Year Electrical Engineering Student
IIT Hyderabad

---

## License

This project is intended for **academic and learning purposes**.
All simulations and derivations are student-generated.
