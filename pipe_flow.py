import numpy as np
import matplotlib.pyplot as plt

def analyze_pipe_flow(D, L, roughness, flow_rates, density, viscosity):
    """
    Analyzes pressure drop in a pipe across a range of flow rates using Darcy-Weisbach.
    """
    area = np.pi * (D / 2)**2
    velocities = flow_rates / area
    reynolds_numbers = (density * velocities * D) / viscosity
    
    friction_factors = []
    pressure_drops = []

    for v, re in zip(velocities, reynolds_numbers):
        if re < 2300:
            # Laminar flow (Hagen-Poiseuille)
            f = 64 / re if re > 0 else 0
        else:
            # Turbulent flow - Haaland approximation for Colebrook equation
            term = (roughness / (3.7 * D))**1.11 + 6.9 / re
            f = (-1.8 * np.log10(term))**-2
        
        friction_factors.append(f)
        # Darcy-Weisbach equation: dP = f * (L/D) * (rho * v^2 / 2)
        dp = f * (L / D) * (density * v**2 / 2)
        pressure_drops.append(dp / 1000) # Convert to kPa

    # Plotting Pressure Drop vs Flow Velocity
    plt.figure(figsize=(9, 5))
    plt.plot(velocities, pressure_drops, color='darkorange', lw=2.5, marker='o', markersize=5)
    plt.title('Pipe Flow Analysis: Pressure Drop vs. Flow Velocity', fontsize=12, fontweight='bold')
    plt.xlabel('Flow Velocity (m/s)')
    plt.ylabel('Pressure Drop (kPa)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig("pipe_flow_plot.png", dpi=300)
    plt.show()

    print("Fluid flow analysis complete. Plot saved as 'pipe_flow_plot.png'.")

if __name__ == "__main__":
    # Pipe and Fluid Parameters
    D = 0.05          # Pipe diameter: 50 mm (0.05 m)
    L = 50.0          # Pipe length: 50 meters
    roughness = 1.5e-6 # Commercial steel absolute roughness (m)
    density = 998.2   # Water density at 20°C (kg/m^3)
    viscosity = 1.002e-3 # Dynamic viscosity of water (Pa·s)
    
    # Range of volumetric flow rates (m^3/s) from 0.001 to 0.015 m^3/s
    flow_rates = np.linspace(0.001, 0.015, 50)

    analyze_pipe_flow(D, L, roughness, flow_rates, density, viscosity)
