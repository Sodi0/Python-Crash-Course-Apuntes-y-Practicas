temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

if temperatura_celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")