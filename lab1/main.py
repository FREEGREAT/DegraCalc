
"""
Програма для роботи з калькулятором через текстовий інтерфейс.

Ця програма дозволяє виконувати основні математичні операції, працювати з історією обчислень, 
а також використовувати пам'ять для збереження проміжних результатів. 
Всі операції підтримують введення з конвертацією типів чисел.

Функціонал:
1. Виконання арифметичних операцій: додавання, віднімання, множення, 
ділення, добування кореня, модуль, піднесення до степеня.
2. Збереження історії виконаних операцій.
3. Робота з пам'яттю: збереження, додавання, віднімання, читання і очищення пам'яті.
4. Вихід з програми.

Залежності:
- math: Для виконання математичних операцій (наприклад, корінь квадратний).
- os: Для роботи з шляхами файлів.
- sys: Для динамічного підключення шляхів до модулів.
- calculator.Calculator: Клас калькулятора.
- ConvertDataType.ConvertNumTypes: Функція для конвертації типів введених чисел.

Імпортовані модулі:
- `Calculator` - клас для виконання математичних операцій.
- `ConvertNumTypes` - функція для конвертації числових типів (int або float).

Програма використовує наступні меню:
- **Головне меню**:
  1. Виконати обчислення.
  2. Переглянути історію.
  3. Виконати операції з пам'яттю.
  4. Вийти з програми.
- **Математичні операції**:
  Підтримує наступні операції:
    - Додавання (+)
    - Віднімання (-)
    - Множення (*)
    - Ділення (/)
    - Корінь квадратний (√ або sqrt)
    - Модуль (%)
    - Піднесення до степеня (** або ^)
- **Операції з пам'яттю**:
  MS - Зберегти результат в пам'ять.
  MR - Прочитати з пам'яті.
  M+ - Додати до результату з пам'яті.
  M- - Відняти від результату з пам'яті.
  MC - Очистити пам'ять.

Керування виконується через введення числового або текстового вибору у відповідь на підказки.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"classes"))
sys.path.append(os.path.join(os.path.dirname(__file__),"functions"))
from calculator import Calculator
from ConvertDataType import ConvertNumTypes

calculator = Calculator()
result = 0

while True:
	action = int( input("Select action: \n 1. Calculating\n 2. See History\n 3. Memory\n 4. Exit : "))
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
					print("Memory:", calculator.MemoryRead())
		case 4:
			exit()

	




