#!/usr/bin/env python3
"""
Circle Calculator and Visualizer

This module provides functions to calculate various circle properties,
visualize circles with sectors, and create ASCII art representations of circles.
"""

from math import pi, sqrt
from matplot_visualize import visualize_circle

#pi = round(pi)


def calculate_circle_properties(radius, angle_degrees=360):
    """
    Calculate the basic properties of a circle and a sector within it.
    
    Args:
        radius (float): The radius of the circle
        angle_degrees (float, optional): The angle of the sector in degrees. Defaults to 360.
    
    Returns:
        dict: A dictionary containing all calculated circle properties
    """
    # Basic circle properties
    diameter = 2 * radius
    circumference = 2 * pi * radius
    area = pi * radius ** 2
    
    # Sector and arc properties
    sector_area = (angle_degrees / 360) * area
    arc_length = (angle_degrees / 360) * circumference
    
    return {
        "radius": radius,
        "angle_degrees": angle_degrees,
        "diameter": diameter,
        "circumference": circumference,
        "area": area,
        "sector_area": sector_area,
        "arc_length": arc_length
    }


def display_calculation_steps(properties):
    """
    Display the step-by-step calculations of circle properties.
    
    Args:
        properties (dict): The dictionary of circle properties
    """
    radius = properties["radius"]
    angle = properties["angle_degrees"]
    
    print("\n=== Input Data ===")
    print(f"Radius: {radius}")
    
    print("\n=== Basic Circle Calculations ===")
    print(f"Diameter: {properties['diameter']} (calculation: 2 × {radius})")
    print(f"Circumference: {properties['circumference']:.4f} "
          f"(calculation: 2 × π × {radius})")
    print(f"Circle area: {properties['area']:.4f} (calculation: π × {radius}²)")
    
    print("\n=== Arc and Sector Calculations ===")
    print(f"Sector area at {angle}°: {properties['sector_area']:.4f} "
          f"(calculation: {angle}/360 × π × {radius}²)")
    print(f"Arc length at {angle}°: {properties['arc_length']:.4f} "
          f"(calculation: {angle}/360 × 2π × {radius})")


def draw_circle_ascii(radius, show_calculation=False):
    """
    Create an ASCII art representation of a circle.
    
    Args:
        radius (int): The radius of the circle
        show_calculation (bool, optional): Whether to show calculation details. Defaults to False.
    
    Returns:
        str: ASCII representation of the circle
    """
    result = []
    
    if show_calculation:
        print(f"\nDrawing parameters:")
        print(f"Drawing radius: {radius}")
        print(f"Y range: from {-radius} to {radius}")
        print(f"X range: from {-2*radius} to {2*radius}")
        print("\nCircle drawing process (showing a few points as examples):")
    
    # Scaling factor to account for character aspect ratio
    scale_x = 2  
    
    for y in range(-radius, radius + 1):
        line = ""
        for x in range(-2 * radius, 2 * radius + 1):
            # Calculate distance from center, accounting for character width/height ratio
            distance = sqrt((x/scale_x)**2 + y**2)
            is_on_circle = abs(distance - radius) < 0.5
            
            if show_calculation and len(result) < 3:  # Show only first few calculations
                print(f"  Point: X={x}, Y={y}")
                print(f"    Distance from center: {distance:.4f}")
                print(f"    Difference from radius: {abs(distance - radius):.4f}")
            
            line += "*" if is_on_circle else " "
                
        result.append(line)
    
    if show_calculation:
        print("\nExplanation: The '*' characters indicate points where the distance "
              "from the center (0,0) is approximately equal to the radius.")
    
    return "\n".join(result)


def main():
    """
    Main function to run the circle calculator and visualizer.
    """
    try:
        # Get user input
        radius = float(input("\nEnter circle radius: "))
        if radius <= 0:
            raise ValueError("Radius must be positive")
            
        angle = float(input("Enter sector angle in degrees (default = 40): ") or "40")
        if angle <= 0 or angle > 360:
            raise ValueError("Angle must be between 0 and 360 degrees")
        
        # Calculate all properties
        properties = calculate_circle_properties(radius, angle)
        
        # Display calculations
        display_calculation_steps(properties)
        
        # Draw ASCII circle
        print("\n=== ASCII Circle Representation ===")
        ascii_circle = draw_circle_ascii(int(radius), show_calculation=True)
        
        # Visualize circle with matplotlib
        print("\n=== Interactive Circle Visualization ===")
        print("Launching visualization window...")
        visualize_circle(
            radius=properties["radius"],
            angle=properties["angle_degrees"],
            diameter=properties["diameter"],
            circumference=properties["circumference"],
            arc_length=properties["arc_length"],
            area=properties["area"],
            sector_area=properties["sector_area"]
        )
        
        # Show ASCII circle
        print(ascii_circle)
        
        return True
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return True


def run_interactive_session():
    """
    Run the circle calculator in interactive mode, allowing multiple calculations.
    """
    print("=" * 50)
    print("CIRCLE CALCULATOR AND VISUALIZER")
    print("=" * 50)
    
    while True:
        try:
            # Run the main calculation
            result = main()
            
            # Ask if the user wants to continue
            print("\n" + "=" * 50)
            while True:
                choice = input("\nWould you like to perform another calculation? (y/n): ").lower()
                if choice in ['y', 'yes']:
                    print("\n" + "=" * 50 + "\n")
                    break  # Break the inner loop to continue with calculations
                elif choice in ['n', 'no']:
                    print("\n" + "=" * 50)  
                    print("\nThank you for using the Circle Calculator. Goodbye!")
                    return  # Exit the function completely
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            
        except KeyboardInterrupt:
            print("\n" + "=" * 50)  
            print("\n\nProgram terminated by user. Goodbye!")
            break


if __name__ == "__main__":
    run_interactive_session()
            
            
 
