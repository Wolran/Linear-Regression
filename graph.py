import os
import csv
import subprocess
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data_price = []
my_price = []
mileage = []

csv_file = "data.csv"
predict = "predict.py"

def graph(mileage, price, name, reset):
	mileage = np.array(mileage, dtype=float)
	price = np.array(price, dtype=float)

	if reset == 1:
		plt.scatter(mileage, price, color='green', label="Données")
	else :
		plt.scatter(mileage, price, color='red', label="Données")
	X = np.array(mileage).reshape(-1, 1)
	y = np.array(price)

	model = LinearRegression()
	model.fit(X, y)
	y_pred = model.predict(X)

	plt.plot(mileage, y_pred, color='blue', label="Régression linéaire")

	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.title("Relation entre le kilométrage et le prix")
	plt.legend()

	plt.savefig(f"{name}.png")
	if reset == 1:
		plt.clf()

if __name__ == "__main__":
	with open(csv_file, 'r', newline='') as fichier_csv:
		lecteur_csv = csv.reader(fichier_csv)
		next(lecteur_csv)
		for ligne in lecteur_csv:
			if ligne:
				valeur = ligne[0]
				data_price.append(ligne[1])
				mileage.append(valeur)
				try:
					result = subprocess.run(["python3", predict, valeur], capture_output=True, text=True, check=True)
					my_price.append(result.stdout.strip())
				except subprocess.CalledProcessError as e:
					print(f"Erreur lors de l'exécution avec la valeur {valeur}: {e}")
				except Exception as e:
					print(f"Erreur inattendue avec la valeur {valeur}: {e}")

	graph_dir = "./graph"
	if not os.path.exists(graph_dir):
		os.makedirs(graph_dir)

	graph(mileage, my_price, "./graph/my price", 0)
	graph(mileage, data_price, "./graph/all price", 1)
	graph(mileage, data_price, "./graph/data price", 0)

	print("Graphiques générés avec succès.")

