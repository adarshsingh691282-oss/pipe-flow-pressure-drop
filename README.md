# Pipe Flow & Pressure Drop Analyzer

A Python tool designed for fluid mechanics applications to evaluate flow regimes (Laminar vs. Turbulent), determine friction factors via the Haaland approximation, and calculate total pressure losses using the Darcy-Weisbach equation.

## 📌 Engineering Principles
- **Reynolds Number ($Re$):** $\\frac{\\rho v D}{\\mu}$
- **Friction Factor ($f$):** Evaluated via Hagen-Poiseuille for laminar flow ($Re < 2300$) and the Haaland explicit approximation of the Colebrook-White equation for turbulent flow.
- **Darcy-Weisbach Equation:** $\\Delta P = f \\cdot \\frac{L}{D} \\cdot \\frac{\\rho v^2}{2}$

## 🛠️ Usage
1. Install dependencies:
   ```bash
   pip install numpy matplotlib
