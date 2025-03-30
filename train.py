import pandas as pd
import numpy as np

def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

try:
	data = pd.read_csv("data.csv")
	if "km" not in data.columns or "price" not in data.columns:
		raise ValueError("Le fichier CSV doit contenir les colonnes 'km' et 'price'.")
	mileage = data["km"].values
	price = data["price"].values
except FileNotFoundError:
	print("Erreur : Le fichier 'data.csv' n'a pas été trouvé.")
	exit(1)
except Exception as e:
	print(f"Erreur lors de la lecture du fichier CSV : {e}")
	exit(1)

# m = sum(1 for row in data if row[0].strip())
m = len(mileage) # ca fonctionne aussi
print(f"Nombre de lignes dans le dataset : {m}")
if m == 0:
	print("Erreur : Le fichier CSV est vide.")
	exit(1)

# Normalisation (entre 0 et 1)
mileage_min, mileage_max = np.min(mileage), np.max(mileage)
price_min, price_max = np.min(price), np.max(price)

if mileage_max != mileage_min:
	mileage_normalized = (mileage - mileage_min) / (mileage_max - mileage_min)
else:
	mileage_normalized = mileage
if price_max != price_min:
	price_normalized = (price - price_min) / (price_max - price_min)
else:
	price_normalized = price

theta0, theta1 = 0, 0
# Nombre d'itérations et de taux d'appprentissage, a changer a voir
iterations = 10000
learningRate = 0.01

#####   algo   #####
for _ in range(iterations):
	sum_theta0 = 0
	sum_theta1 = 0
	
	for i in range(m):
		estimated_price = estimatePrice(mileage_normalized[i], theta0, theta1)
		error = estimated_price - price_normalized[i]
		sum_theta0 += error
		sum_theta1 += error * mileage_normalized[i]
	
	tmp_theta0 = learningRate * (1 / m) * sum_theta0
	tmp_theta1 = learningRate * (1 / m) * sum_theta1
	
	theta0 -= tmp_theta0
	theta1 -= tmp_theta1

theta0_final = price_min + (price_max - price_min) * (theta0 - theta1 * mileage_min / (mileage_max - mileage_min))
theta1_final = (price_max - price_min) * theta1 / (mileage_max - mileage_min)

print(f"Valeurs finales :")
print(f"theta0 = {theta0_final}")
print(f"theta1 = {theta1_final}")

def write_values(theta0, theta1):
	try:
		with open("theta_values.txt", "w") as file:
			file.write(f"{theta0}\n")
			file.write(f"{theta1}\n")
	except Exception as e:
		print(f"Erreur lors de la sauvegarde des valeurs : {e}")

#todo need to add function for more visibility