from tkinter import *

import matplotlib.pyplot as plt
import numpy as np

import temp


class mclass:
    def __init__(self, window):
        self.box = Entry(window)
        self.button = Button(window, text="2015", command=self.plot)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2016", command=self.plot1)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2017", command=self.plot2)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2018", command=self.plot3)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2019", command=self.plot4)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2020", command=self.plot5)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2021", command=self.plot6)
        self.box.pack()
        self.button.pack()
        self.box = Entry(window)
        self.button = Button(window, text="2022", command=self.plot7)
        self.box.pack()
        self.button.pack()

    def plot(self):
        height = [temp.temp2015[0], temp.temp2015[1], temp.temp2015[2], temp.temp2015[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2015', fontsize=16, color='#323232')

        plt.show();

    def plot1(self):
        height = [temp.temp2016[0], temp.temp2016[1], temp.temp2016[2], temp.temp2016[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2016', fontsize=16, color='#323232')

        plt.show();

    def plot2(self):
        height = [temp.temp2017[0], temp.temp2017[1], temp.temp2017[2], temp.temp2017[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2017', fontsize=16, color='#323232')

        plt.show();

    def plot3(self):
        height = [temp.temp2018[0], temp.temp2016[1], temp.temp2016[2], temp.temp2016[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2018', fontsize=16, color='#323232')

        plt.show();

    def plot4(self):
        height = [temp.temp2019[0], temp.temp2019[1], temp.temp2019[2], temp.temp2019[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2019', fontsize=16, color='#323232')

        plt.show();

    def plot5(self):
        height = [temp.temp2020[0], temp.temp2020[1], temp.temp2020[2], temp.temp2020[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2020', fontsize=16, color='#323232')

        plt.show();

    def plot6(self):
        height = [temp.temp2021[0], temp.temp2021[1], temp.temp2021[2], temp.temp2021[3]]
        bars = ('Nowy Rok', 'Wielkanoc', 'Swieto Pracy', 'Boze Cialo')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2021', fontsize=16, color='#323232')

        plt.show();

    def plot7(self):
        height = [temp.temp2022[0], temp.temp2022[1]]
        bars = ('Nowy Rok', 'Wielkanoc')
        y_pos = np.arange(len(height))

        # Figsize
        plt.figure(figsize=(10, 5))

        # Create bars
        plt.bar(y_pos, height, color='#969696')

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        plt.xlabel('Swieta', fontsize=12, color='#323232')
        plt.ylabel('Temperatura', fontsize=12, color='#323232')
        plt.title('Warszawa 2022', fontsize=16, color='#323232')

        plt.show();


window = Tk()

start = mclass(window)

window.mainloop()
