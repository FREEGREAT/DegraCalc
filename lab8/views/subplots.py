"""
multiple_subplots.py

Цей модуль містить функцію для побудови декількох підграфіків, 
що ілюструють різні аспекти даних, такі як зміна температури, 
співвідношення температури та вологості, а також розподіл вологості.

Імпортовані модулі:
    import matplotlib.pyplot as plt:
        Використовується для побудови графіків.

Функції:
    plot_multiple_subplots(data):
        Будує кілька підграфіків для візуалізації даних.
"""

import matplotlib.pyplot as plt

def plot_multiple_subplots(data):
    """
    Створює три підграфіки для аналізу даних.

    Параметри:
        data (pandas.DataFrame): Табличні дані, які повинні містити такі стовпці:
            - 'Date' для відображення дати;
            - 'Temperature' для значень температури;
            - 'Humidity' для значень вологості.

    Підграфіки:
        1. Лінійний графік зміни температури за часом:
            - Вісь X: Дата.
            - Вісь Y: Температура (°C).
            - Заголовок: "Temperature Over Time".
        2. Графік розсіювання (scatter plot) температури та вологості:
            - Вісь X: Температура (°C).
            - Вісь Y: Вологість (%).
            - Заголовок: "Temperature vs Humidity".
        3. Гістограма розподілу вологості:
            - Вісь X: Вологість (%).
            - Вісь Y: Частота.
            - Заголовок: "Humidity Distribution".

    Виводить:
        Візуалізацію у вигляді трьох підграфіків, вирівняних горизонтально.
    """
    axs = plt.subplots(1, 3, figsize=(18, 5))
    # Лінійний графік температури
    data.plot(x='Date', y='Temperature', kind='line', ax=axs[0])
    axs[0].set(title='Temperature Over Time', xlabel='Date', ylabel='Temperature (°C)')

    # Графік розсіювання (Temperature vs Humidity)
    data.plot.scatter(x='Temperature', y='Humidity', ax=axs[1])
    axs[1].set(title='Temperature vs Humidity', xlabel='Temperature (°C)', ylabel='Humidity (%)')

    # Гістограма вологості
    data['Humidity'].plot(kind='hist', bins=10, ax=axs[2])
    axs[2].set(title='Humidity Distribution', xlabel='Humidity (%)', ylabel='Frequency')

    # Коригування відступів
    plt.tight_layout()
    plt.show()
