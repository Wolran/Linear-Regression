import sys

def load_value():
	try:
		with open("theta_values.txt", "r") as file:
			lines = file.readlines()
			theta0 = float(lines[0].strip())
			theta1 = float(lines[1].strip())
	except FileNotFoundError:
		print("Erreur : Fichier 'theta_values.txt' non trouvé. Utilisation des valeurs par défaut (0).")
		theta0 = 0
		theta1 = 0
	except ValueError:
		print("Erreur : Les valeurs dans le fichier ne sont pas des nombres valides. Utilisation des valeurs par défaut (0).")
		theta0 = 0
		theta1 = 0
	return theta0, theta1

def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def main():
	theta0, theta1 = load_value()
	try:
		# mileage = float(input("Entrez le kilométrage de la voiture : "))
		if len(sys.argv) != 2:
			print("Erreur : Veuillez fournir un kilométrage en argument.")
			return
		mileage = float(sys.argv[1])
		if mileage < 0:
			print("Erreur : Le kilométrage ne peut pas être négatif.")
		else:
			predicted_price = estimatePrice(mileage, theta0, theta1)
			print(f"{(int)(predicted_price)}")
	except ValueError:
		print("Erreur : Veuillez entrer un kilométrage valide.")
	

if __name__ == "__main__":
	main()