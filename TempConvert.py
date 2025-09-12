#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Farenheit temperature: ")
  tempF = int(tempF)

  tempC = (tempF - 32) * 5/9
  tempC = int(tempC)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
