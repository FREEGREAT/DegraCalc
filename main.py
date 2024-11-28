import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"classes"))
sys.path.append(os.path.join(os.path.dirname(__file__),"functions"))

from calculator import Calculator
from ConvertDataType import ConvertNumTypes

calculator = Calculator()
result = 0

while(True):
	action = int(input("Select action: \n 1. Calculating\n 2. See History\n 3. Memory\n 4. Exit : "))
	match action:
		case 1:
			operator = input("Select operation( + | - | * | / | % | ): ")
			
			num1 = ConvertNumTypes(input("Input first num "))
			num2 = ConvertNumTypes(input("Input second num "))
			
			match operator:
				case "+":
					result = calculator.Add(num1,num2)
					print ("It`s equal:",result)
				case "-":
					result = calculator.Minus(num1,num2)
					print ("It`s equal:",result)
				case "*":
					result = calculator.Multiple(num1,num2)
					print ("It`s equal:",result)
				case "/":
					result = calculator.Div(num1,num2)
					print ("It`s equal:",result)
				case "%":
					result = calculator.Mod(num1,num2)
					print ("It`s equal:",result)

			if(input("Do you want to save result in memory?").upper() == "Y" ):
				calculator.MemorySave(result)

			if(input("Do you want to continue work? (Y/N)").upper() == "Y") : continue
			else : break
		case 2:
			calculator.GetHistory()
		case 3:
			operator = input("Select operation( MS | MR | M+ | M- | MC ): ")
			match operator:
				case "MS":
					calculator.MemorySave(result)
				case "M+":
					calculator.MemoryAdd(result)
				case "M-":
					calculator.MemorySub(result)
				case "MC":
					calculator.MemoryClear()
				case "MR":
					print(calculator.MemoryRead())
		case 4:
			exit()

	




