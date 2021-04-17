# Protocole 5

Le protocole permet d'étudier l'influence des clusters dans la prédiction de la dette.

La variable à expliquer est la moyenne de dette au cours de la période de location (absolue ou relative)

Les variables explicatives sont :
* locatives : loyer, caution
* attributs des individus (situation des individus)
* finances du ménage : revenus, ressources
* localisation : département et code postal

Données utilisées :
* shapefile de la France département et code postal (lien : https://www.data.gouv.fr/fr/datasets/contours-des-departements-francais-issus-d-openstreetmap/ )
* base de données habitat76 (lien : https://drive.google.com/file/d/1yQxmmQDDbHMkzWFma-s6FNs_TxTXYJuA/view?usp=sharing )


**Étapes du protocole :**
* pré-traitement des 2 jeux de données (moyenne des variables quantitatives et modification du statut en 0.5 si changement)pour aléger la manupulation des données.
* ajouter la moyenne de la variable à explique et l'aide étant aussi valeurs préléves dans le temps pour facilité la prédiction moyenne qui en suit.
* création d'un tableau individu variable avec la variable dette et un tableau avec l'agregation des individus au niveau de la localisation (département ou code postal)
* analyse exploratoire : analyse globale des variables
* modèle de prediction (fôret de regression) selon plusieurs méthodes de clustering et analyse de l'importance des variables dans le modèle

L'étude est composé de 2 directions, le même protocole est effectuée pour les directions de chaque étude : 
<ol>
<li>Utilisation de l'aspect de la localité:<br>Etant données que les indivudées sont disposées sur le terrain français, cette variable peut alors être choisi comme cluster. On dispose de la donnée au niveau code postal, où on peut déduire le département. Ces deux niveaux de granulaumétrie seront utilisées. Ainsi, cette direction permettra de voir si le niveau d'endettement d'un ménage a un lien avec la localisation, que ce soit une corrélation négative ou positive. Par conséquent, on a choisit cette valeur comme étant un random effect qui sera par la suite un moyen de distinction, de cluster, et aussi comme élement central pour 
le modéle MERF.</li>
<li>Clustering des individues :<br>ayant aucun facteur direct pour pouvoir caracteriser chaque individu; on a choisit de faire un clustering pour prendre en compte tous les déterminants des indivuds pour générer un aspect de réference. Un clustering a été réalisé, le nombre de cluster est choisi de façon optimal. Cette direction permettra de se rendre compte de l'importance de faire des clusters ou non de la population pour la prédiction

---
</li>
</ol>


