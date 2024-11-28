import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"classes"))
sys.path.append(os.path.join(os.path.dirname(__file__),"functions"))

from calculator import Calculator, Memory
from ConvertNumberType import ConvertNumberType
from ErrorHandler import *

calculator = Calculator()
memory = Memory()
result = 0
operator_list = ["+", "-", "*", "/", "√", "sqrt", "%", "**"]

while(True):
	try:
		action = int(input("Виберіть дію: \n 1. Обчислення\n 2. Переглянути історію\n 3. Пам'ять\n 4. Вихід : "))
	except ValueError:
		print("Помилка введення. Будь ласка виберіть дію в діапазоні (1-4).")
	match action:
		case 1 :
			operator = GetOperator()
			num1, num2 = (ConvertNumberType(GetNumber()), None) if operator == "sqrt" else (ConvertNumberType(GetNumber()), ConvertNumberType(GetNumber()))					
			match operator:
				case "+" : result = calculator.Add( num1, num2 )
				case "-" : result = calculator.Subtract(num1,num2 )
				case "*" : result = calculator.Multiply(num1,num2 )
				case "/" : result = calculator.Divide(num1,num2 )
				case "sqrt" : result = calculator.SquareRoot(num1 )
				case "%" : result = calculator.Mod(num1,num2 )
				case "**" : result = calculator.Exponentiate(num1,num2) 
			if(input("Хочете продовжити роботу? (Y/N)").strip().upper() == "Y") : continue 
			else : exit()
		case 2 : calculator.GetHistory()
		case 3 :
			match input("Виберіть операцію ( MR | M+ | M- | MC ): ").strip().upper():
				case "M+" : memory.Add(result)
				case "M-" : memory.Subtract(result)
				case "MC" : memory.Clear()
				case "MR" : print(memory.Read())
				case _: print("Помилка в роботі з пам'ятю.")
		case 4: exit()

	




