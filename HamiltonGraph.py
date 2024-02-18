################################# GP PAR PILOTE ################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données depuis le fichier CSV
data = pd.read_csv('F1seasons.csv')

################## GP GAGNÉS PAR TOUT LES PILOTES

data = data[['Grand Prix', 'Winner']] # Sélectionner uniquement les colonnes nécessaires pour le graphique

winners_count = data['Winner'].value_counts() # Compter le nombre de victoires par pilote

# Créer un nouvel espace de tracé pour des graphiques
plt.figure(figsize=(15, 10))  # Définir la taille du graphique

# Créer des sous-graphiques qui sur un quadrillage de 2 lignes et 2 colonnes, on commençera par un graphique en haut à gauche (position 1)
plt.subplot(2, 2, 1)

color_rgb_purple = [104/255, 65/255, 234/255] # Couleur mauve
colors_graphique_1 = [color_rgb_purple] + ['grey'] * (len(winners_count) - 1)  # Créer une palette de couleur : la première sera mauve et le reste gris
sns.barplot(x=winners_count.values, y=winners_count.index, palette=colors_graphique_1)  # Tracer un Histogramme avec la palette 1 précédemment crée
plt.xlabel('Number of victories', fontsize=14) # Nom (et taille du nom) de l'axe des abscisses
plt.ylabel('Pilots', fontsize=14) # Nom (et taille du nom) de l'axe des ordonnées
plt.title('GP victories 2012-2022', fontsize=18, fontweight='bold') # Titre du graphique
plt.grid(axis='x', linestyle='-', alpha=0.5) # Lignes Verticales dans le graphique en un trait simple


# Ajouter des lignes verticales à intervalles de 5 en 5 moins opaques
for i in range(5, 80, 5):
    plt.axvline(x=i, color='grey', linestyle='-', alpha=0.1)

# Ajuster automatiquement les sous-graphiques
plt.tight_layout()


################## GP GAGNÉS PAR LEWIS HAMILTON

# Nettoyer les espaces supplémentaires et convertir en minuscules
data['Winner'] = data['Winner'].str.strip().str.lower()

# Filtrer pour ne garder que les victoires de Lewis Hamilton
data_hamilton = data.loc[data['Winner'] == 'lewis hamilton']

# Compter le nombre de victoire de Grand Prix par Hamilton
winners_count = data_hamilton['Grand Prix'].value_counts()

# Sous-Graphique à la position en haut à droite de la page (Position 2)
plt.subplot(2, 2, 2)

# Créer une palette de couleurs : les 5 premières barres colorées et les autres sont grises
colors_graphique_2 = [color_rgb_purple, 'black', 'red', 'orange', 'green'] + ['grey'] * (len(winners_count) - 5)

sns.barplot(y=winners_count.values, x=winners_count.index, palette=colors_graphique_2) # Tracer un Histogramme avec la palette 2 précédemment crée

plt.xlabel('Grand Prize', fontsize=14) # Nom (et taille du nom) de l'axe des abscisses
plt.ylabel('Number of victories', fontsize=14) # Nom (et taille du nom) de l'axe des ordonnées
plt.title('Hamilton GP victories 2012-2022', fontsize=18, fontweight='bold') # Titre du graphique
plt.xticks(rotation=45, ha='right') # Inclinaison des abscisses pour une meilleure lecture
plt.grid(axis='y', linestyle='-', alpha=0.5) # Lignes Horizontales dans le graphique en un trait simple

# Ajuster automatiquement les sous-graphiques
plt.tight_layout()


################## ÉVOLUTION DES TEMPS DE COURSE DE LEWIS HAMILTON AU CIRCUIT GREAT BRITAIN, USA, CANADA, HUNDARY, ITALY

# Données des années et des temps de course sur différents circuits
annees_Great = [2020, 2019, 2017, 2016, 2015, 2014]
temps_Great = [1.4678333333333333, 1.218452, 1.357430, 1.9158316666666667, 1.524729, 2.449094]

annees_Canada = [2019, 2017, 2016, 2015, 2012]
temps_Canada = [1.4845166666666666, 1.551430, 1.5174633333333334, 1.5355291666666666, 1.538493]

annees_hungary = [2019, 2018, 2016, 2013, 2012]
temps_hungary = [1.5837966666666667, 1.561427, 1.675115, 1.704445, 1.684503]

annees_Italy = [2018, 2017, 2015, 2014, 2012]
temps_Italy = [1.109484, 1.092312, 1.133688, 1.191236, 1.194221]

annees_cota = [2017, 2016, 2015, 2014, 2012]
temps_cota = [1.573991, 1.923618, 2.112703, 1.604785, 1.359269]

# Sous-Graphique à la position en bas à gauche de la page (Position 3)
plt.subplot(2, 2, 3)

# Caractéristique des courbes des différents temps de course
plt.plot(annees_Great, temps_Great, marker='o', label='Great Britain', color=color_rgb_purple)
plt.plot(annees_cota, temps_cota, marker='x', label='United States', color='black')
plt.plot(annees_Canada, temps_Canada, marker='s', label='Canada', color='red')
plt.plot(annees_hungary, temps_hungary, marker='d', label='Hungary', color='orange')
plt.plot(annees_Italy, temps_Italy, marker='^', label='Italy', color='green')

# Ajouter des titres et des libellés
plt.title("Evolution of Lewis Hamilton's race times \n on his best circuits since 2012", fontsize=18, fontweight='bold')
plt.xlabel("Years", fontsize=14) # Nom (et taille du nom) de l'axe des abscisses
plt.ylabel("Race Time (Hours)", fontsize=14) # Nom (et taille du nom) de l'axe des ordonnées
plt.legend() # Afficher la légende
plt.grid(True) # Active l'affichage du quadrillage


# Ajuster l'espacement entre les sous-graphiques
plt.subplots_adjust(hspace=0.7, bottom=0.06, top = 0.95)  # Ajuster les valeurs selon vos besoins

# Afficher les graphiques
plt.show()