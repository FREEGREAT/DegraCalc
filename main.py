import math
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
			operator = input("Select operation( + | - | * | / | √ (= sqrt) | % | ** (= ^) ): ")
			
			if(operator == "sqrt" or operator == "√") :
				num1 = ConvertNumTypes(input("Input Number "))
			else:
				num1 = ConvertNumTypes(input("Input first num "))
				num2 = ConvertNumTypes(input("Input second num "))
			
			match operator:
				case "+":
					result = calculator.Add(num1,num2)
					print(result)
				case "-":
					result = calculator.Minus(num1,num2)
					print(result)
				case "*":
					result = calculator.Multiple(num1,num2)
					print(result)
				case "/":
					result = calculator.Div(num1,num2)
					print(result)
				case "sqrt":
					result = calculator.Sqrt(num1)
					print (result)
				case "%":
					result = calculator.Mod(num1,num2)
				case "**":
					result = calculator.Exponentiation(num1,num2)

			if(input("Do you want to save result in memory?") == "Y" ):
				calculator.MemorySave(result)

			if(input("Do you want to continue work? (Y/N)") == "Y") : continue
			else : break

		case 2:
			calculator.GetHistory()

		case 3:
			operator = string(input("Select operation( MS | MR | M+ | M- | MC ): "))
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
					calculator.MemoryRead()
		case 4:
			exit()

	




