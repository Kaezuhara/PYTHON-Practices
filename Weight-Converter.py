def determine_unit():
  while True:
    weightUnit = input("Enter your desired weight unit (kg/lb): ").lower()
    if weightUnit in ("kg", "lb"):
        return weightUnit
    else:
        print("Invalid unit.")


def determine_weight():
  while True:
    try: 
        weight = float(input("Enter your weight: "))
        if weight < 0:
           raise ValueError
        else:
            weight = round(weight, 2)
            return weight
    except ValueError:
       print("Invalid input.")

def convert(weightUnit, weight):
  if (weightUnit == "kg"):
    result = weight * 2.205
    print(f"{weight:.2f} {weightUnit} is {result:.2f} lb")
  else:
    result = weight / 2.205
    print(f"{weight:.2f} {weightUnit} is {result:.2f} kg")

def main():
  weightUnit = determine_unit()
  weight = determine_weight()
  convert(weightUnit, weight)

if __name__ == "__main__":
  main()