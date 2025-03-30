import csv
import subprocess

data_price = []
my_price = []

csv_file = "data.csv"
predict = "predict"

with open(csv_file, 'r', newline='') as fichier_csv:
	lecteur_csv = csv.reader(fichier_csv)
	next(lecteur_csv)
	for ligne in lecteur_csv:
		if ligne:
			valeur = ligne[0]
			data_price.append(ligne[1])
			try:
				subprocess.run(['py', predict, valeur], check=True)
				my_price.append(valeur)
				print(f"Programme exécuté avec la valeur : {valeur}")
			except subprocess.CalledProcessError as e:
				print(f"Erreur lors de l'exécution avec la valeur {valeur}: {e}")
			except Exception as e:
				print(f"Erreur inattendue avec la valeur {valeur}: {e}")

print("Traitement terminé - toutes les valeurs du CSV ont été utilisées")
print("Valeurs du CSV :")
print(data_price)
print("\n----------------------------\n")
print("my price :")
print(my_price)

#! need to change pc (never code on windows again)