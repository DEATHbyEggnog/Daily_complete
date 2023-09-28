#Ashley Ferguson, 100615979 2131-01
#Circalc.py Day 4
#PROGRAM CALCULATES RESISTANCE SERIES AND PARALLEL
#PROGRAM CALCULATES THE TIME CONSTANT OF RC CIRCUIT
#PROGRAM CALCULATES RESONANT FREQUENCY, BANDWIDTH, AND Q FACTOR
#ASHLEY FERGUSON, 100615979
#TPRG2131 DAY 4, SEPTEMBER 19, 2023
## THIS PROGRAM IS STRINCTLY MY OWN WORK. ANY MATERIAL 
# BEYOND COURSE LEARNING MATERIALS THAT IS TAKEN FROM 
# THE WEB OR OTHER SOURCE IS PROPERLY CITED, GIVING
# CREDIT TO THE ORGINAL AUTHOR(S).

import math

def calculate_resonance(l, c):
    return 1 / (2 * math.pi * math.sqrt((l * 1e-3) * (c * 1e-6)))

def calculate_bandwidth(r, l):
    return r / (l * 2 * math.pi)

def calculate_qfactor(resonance, bandwidth):
    return resonance / bandwidth

def main_menu():
    print("Startup Menu:")
    print("1. Series Resistors")
    print("2. Parallel Resistors")
    print("3. RC Circuit time Constant")
    print("4. Resonant Frequency for RLC Circuit")
    print("5. Bandwidth Calculation")
    print("6. Q Factor Calculation")
    print("Q. Exit")

# Initialize variables
resistance1 = 0.0
resistance2 = 0.0
inductance = 0.0
capacitance = 0.0
resistance = 0.0

# Function to get user input for a numeric value and validate it
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0.0:
                print("The value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

while True:
    main_menu()
    choice = input("Please choose an option from 1-5 or Q to quit calculator: ")

    if choice == 'q' or choice == 'Q':
        print("Exiting program...")
        break
    elif choice == '1':
        # Series Resistors
        resistance1 = get_numeric_input("What is the resistance of resistor 1, in ohms? ")
        resistance2 = get_numeric_input("What is the resistance of resistor 2, in ohms? ")
        
        series_resistance = resistance1 + resistance2
        print(f"Total resistance: {series_resistance:.2f} ohms")
        pass
    elif choice == '2':
        # Parallel Resistors
        resistance1 = get_numeric_input("What is the resistance of resistor 1, in ohms? ")
        resistance2 = get_numeric_input("What is the resistance of resistor 2, in ohms? ")
        
        parallel_resistance = 1/(1/resistance1 + 1/resistance2)
        print(f"Total resistance: {parallel_resistance:.2f} ohms")
        pass
    elif choice == '3':
        # RC Time Constant
        resistance = get_numeric_input("What is the resistance, in ohms? ")
        capacitance = get_numeric_input("What is the capacitance in uF? ")
        
        time_constant = resistance * (capacitance * 1e-6)
        print(f"Time: {time_constant:.2f} seconds")
        pass
    elif choice == '4':
        # Resonance Calculation
        inductance = get_numeric_input("What is the inductance in mH? ")
        capacitance = get_numeric_input("What is the capacitance in uF? ")
        
        resonance = calculate_resonance(inductance, capacitance)
        print(f"Resonant Frequency: {resonance:.2f} Hz")
    elif choice == '5':
        # Bandwidth Calculation
        inductance = get_numeric_input("What is the inductance in mH? ")
        resistance = get_numeric_input("What is the resistance in ohms? ")
        
        bandwidth = calculate_bandwidth(resistance, inductance)
        print(f"Bandwidth: {bandwidth:.2f} Hz")
    elif choice == '6':
        # Q Factor Calculation
        inductance = get_numeric_input("What is the inductance in mH? ")
        capacitance = get_numeric_input("What is the capacitance in uF? ")
        resistance = get_numeric_input("What is the resistance in ohms? ")
        
        resonance = calculate_resonance(inductance, capacitance)
        bandwidth = calculate_bandwidth(resistance, inductance)
        q_factor = calculate_qfactor(resonance, bandwidth)
        print(f"Q Factor: {q_factor:.2f}\n")
    else:
        print("Invalid choice. Please select a valid option (1-5 or Q to quit).")
