# Objectif

# Prendre un dossier en input et parcourir recursivement
# tous les sous dossier
# Tous les fichiers trouver devront ensuite etre copier et placer dans des dossiers avec l arbo suivante
## Annee > Mois > Jour
from sys import argv
import computation

if (len(argv) < 2):
    print('Il manque le chemin à traiter')
    print('Exemple d\'éxecution')
    print('main.exe C:/cheminversmondossier')
else:
    file_group = computation.__group_files_by_date(argv[1])
    for k, v in file_group.items():
        computation.__copy_to_folder(argv[1], k, v)

# Pour un repertoire, retourne un tuple avec (directories, files)
