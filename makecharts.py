import pandas as pd
import matplotlib.pyplot as plt

def makeCharts():
    names = ["mr/part-00000", "mrd/part-00000", "dec_mean/part-00000"]
    try:   
        df = pd.read_csv(names[0], header=None)
        plt.figure(1)
        plt.bar(df[0], df[1])
        plt.title("Ilość najlepszych filmów w danym roku")
        plt.xlabel("rok produkcji")
        plt.ylabel("liczba filmów")
        # plt.show()
        plt.savefig('movies_num_per_year')
    except FileNotFoundError:
        print("File:", names[0], " not found")

    try:
        df = pd.read_csv(names[1], header=None)
        plt.figure(2)
        plt.bar(df[0], df[1], width=6)
        plt.title("Ilość najlepszych filmów w dekadzie")
        plt.xlabel("dekada")
        plt.ylabel("liczba filmów")
        # plt.show()
        plt.savefig('movies_num_per_decade')
    except FileNotFoundError:
        print("File ", names[1], " not found")

    try:
        df = pd.read_csv(names[2], header=None)
        plt.figure(3)
        plt.bar(df[0], df[1], width=6)
        plt.title("Średnia ocena najlepszych filmów w dekadzie")
        # plt.show()
        plt.xlabel("dekada")
        plt.ylabel("średnia ocena")
        plt.savefig('rating_mean_per_decade')
    except FileNotFoundError:
        print("File ", names[2], " not found")
