# AP01 : Science des données pour la gestion de l’immobilier

Cet Atelier projet vise à explorer une base de données volumineuse liée à la gestion des locataires d'un bailleur social, notamment pour pouvoir identifier les locataires risquant de présenter des défauts de paiement, et pour leur apporter l'aide nécessaire au règlement de leur dette (que ce soit via de simples rappels ou des visites personnalisées). Ce projet se fait en lien avec SOPRA/STERIA d'une part, et le bailleur Habitat 76 d'autres part, qui apporteront la base de données et leur expertise sur le domaine.

L’objectif de cette collaboration est d’aider le bailleur dans sa prise de décision pour des problématiques liées aux locataires en défaut de paiement.

## Protocole 2

Dans cette étude nous voulons prédire la dette de l’individu dans les mois futurs en fonction de son historique. Plus précisément, nous voulons savoir si le client sera en dette dans trois mois.

1. Ajouter les colonnes Loyer et dette aux jeu de données produit initialement dans “clients_menages_tabular.csv”. On aura donc accès aux données liées au client (compte client / contrat) et à son occupant social (ménage)
2. nous souhaitons produire un data set transformé : 

Au lieux d’afficher les colonnes (Février, Mars, Avril…, Décembre,) nous voulons le nombre de mois d’écart par rapport au mois présent décrit par “0”. En négative cela correspond à des mois passés. En positif, cela correspond à des mois futurs.

| **variables (x)**                  |                 |                 |                |                                    |
| ---------------------------------- | --------------- | --------------- | -------------- | ---------------------------------- |
| **autres variables client/menage** | **solde t(-k)** | **solde t(-1)** | **solde t(0)** | **présence de la dette t+2/3 (y)** |
| ...                                | NaN             | 0               | 0              | 0                                  |
| ...                                | 100             | 112             | 150            | 1                                  |
| ...                                | 15              | 0               | 12             | 0                                  |

1. Nous procédons ensuite à une suppression des colonnes avec un proportion de valeurs non renseignées supérieur à 99%

2. Imputation de variable manquantes avec une méthode multivariée.

3. Calcul de baselines qui permettrons l’évaluation des performances des modèles.

4. 1. utilisation d’une constante
   2. utilisation d’une statistique univariée 
   3. utilisation des informations les plus récentes (condition sur le dernier solde par exemple)

5. Entrainement d’un classifier régression logistique. Utiliser la régularisation “l1” lasso pour voir l’effet d’élimination de certaines variables et faire de la feature sélection implicitement

6. Entrainement d’un arbre de décision. 

7. Calcul des ROC et comparaison des performances des deux modèles

9. Création des Visuels

10. 1. afficher (au moins le début) de l’arbre de décision
    2. roc pous les différents classifieurs
    3. les matrices de confusion
    4. Erreur en fonction de l’éloignement dans le temps de la prédiction
    5. Erreur en fonction du nombre de mois considérés pour entrainer les modèles

### Instructions

```sh
cd axe2/Clean_Dataset
```

Normalement le dossier contient le fichier `Clean_Dataset_output_clients_menages_tabular.csv` qui est le fichier csv contruit à partir du code de Soundouss.

Vous deviez vérifier l'existance du fichier `df_protocole_2_lessNans.csv`.

Si il est absent, vous pouvez le générer:

```sh
jupyter nbconvert --execute Creation_du_tableau_individu_variables_protocole 2.ipynb 
```

Maintenant vous pouvez ouvrir le dossier `Classification` et ouvrir l'analyse qui implémente le protocole

```sh
cd axe2/Classification
jupyter notebook Etude_protocole2_classification.ipynb 
```

