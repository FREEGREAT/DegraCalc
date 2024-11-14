import matplotlib.pyplot as plt

def plot_multiple_subplots(data):
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    
    # Лінійний графік
    data.plot(x='Date', y='Temperature', kind='line', ax=axs[0])
    axs[0].set(title='Temperature Over Time', xlabel='Date', ylabel='Temperature (°C)')

    # Діаграма розсіювання
    data.plot.scatter(x='Temperature', y='Humidity', ax=axs[1])
    axs[1].set(title='Temperature vs Humidity', xlabel='Temperature (°C)', ylabel='Humidity (%)')

    # Гістограма
    data['Humidity'].plot(kind='hist', bins=10, ax=axs[2])
    axs[2].set(title='Humidity Distribution', xlabel='Humidity (%)', ylabel='Frequency')

    plt.tight_layout()
    plt.show()
