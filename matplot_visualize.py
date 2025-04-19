import matplotlib.pyplot as plt
import numpy as np
from math import pi
import json

def visualize_circle(radius, angle, diameter, circumference, arc_length, area, sector_area):
    """
    Visualize a circle with a sector at the specified angle.
    
    Args:
        radius (float): The radius of the circle רדיוס 
        angle (float): The angle of the sector in degrees זָוִית
        diameter (float): The diameter of the circle קוֹטֶר
        circumference (float): The circumference of the circle קַו מֵקִיף
        arc_length (float): The length of the arc at the specified angle אורך קשת
        area (float): The area of the circle  שטח
        sector_area (float): The area of the sector at the specified angle שטח מגזר
    """
    # Convert angle from degrees to radians | המרת זווית ממעלות לרדיאנים
    angle_rad = np.deg2rad(angle)
    
    # Create figure and axisis with equal aspect ratio | צור איור וציר עם יחס רוחב-גובה שווה
    figure, axis = plt.subplots(figsize=(8, 8))
    axis.set_aspect('equal')

    # Draw the full circle
    circle = plt.Circle((0, 0), radius, fill=False, color='black', linewidth=2, label='Circle')
    axis.add_artist(circle)

    # Generate points for the arc/sector
    theta = np.linspace(0, angle_rad, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Create a sector by including the center point
    x_sector = np.concatenate([[0], x, [0]])
    y_sector = np.concatenate([[0], y, [0]])
    axis.fill(x_sector, y_sector, color='#ADD8E6', alpha=0.6, label=f'Sector Area ({angle}°)')

    # Draw the arc
    axis.plot(x, y, color='blue', linestyle='--', linewidth=2, 
            label=f'Arc Length ({angle}°) ≈ {arc_length:.2f}')

    # Draw the radii
    axis.plot([0, radius], [0, 0], color='green', linewidth=2, label=f'Radius = {radius}')
    axis.plot([0, radius*np.cos(angle_rad)], [0, radius*np.sin(angle_rad)], 
            color='green', linewidth=2)

    # Draw the diameter
    axis.plot([-radius, radius], [0, 0], color='red', linestyle=':', linewidth=2, 
            label=f'Diameter = {diameter}')
    
    # Calculate percentages for display
    sector_percentage = (sector_area / area) * 100
    arc_percentage = (arc_length / circumference) * 100
    
    # Create text information
    textstr = '\n'.join((
        f"Circle Area ≈ {area:.4f} (π * r²)",
        f"Circumference ≈ {circumference:.4f} (2π * r)",
        f"Sector Area ({angle}°) ≈ {sector_area:.4f} ({sector_percentage:.2f}% from circle area)",
        f"Arc Length ({angle}°) ≈ {arc_length:.4f} ({arc_percentage:.2f}% of circumference)"
    ))
    
    # Add text box with information
    props = dict(boxstyle='round', facecolor='white', edgecolor='gray')
    axis.text(-100, -100, textstr, fontsize=10, bbox=props)

    # Set up the plot
    axis.set_xlim(-100,100)
    axis.set_ylim(-100,100)
    axis.set_title(f"Circle Visualization – Radius {radius}", fontsize=14)
    axis.grid(True)
    axis.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

