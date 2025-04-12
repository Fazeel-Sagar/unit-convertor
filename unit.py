def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001,
        "inch": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mile": 0.000621371
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported units.")

    # Convert to meters first
    value_in_meters = value / conversion_factors[from_unit]
    # Convert to target unit
    converted_value = value_in_meters * conversion_factors[to_unit]
    return converted_value


# Example usage
val = float(input("Enter value: "))
from_u = input("From unit (e.g., m, cm, km): ")
to_u = input("To unit (e.g., inch, ft, yd): ")

try:
    result = convert_units(val, from_u, to_u)
    print(f"{val} {from_u} = {result:.4f} {to_u}")
except ValueError as e:
    print(e)