# AXE 3

## Problématique

**Pour un individu en dette, est ce que sa dette va augmenter, rester constante ou diminuer au bout de quelques mois ?**

De cette problématique ressortent trois lignes principales:
- L’étude du problème sous forme de séries temporelles.
- L’étude comme problème de régression.

## Séries temporelles

Nous cherchons ici à labelliser des séries temporelles (Time Series Classification), Le principe est d’analyser la suite de valeurs numériques qui représente l’évolution de la dette au cours du temps afin de prédire les valeurs qu’elle pourrait prendre dans le futur, cela en prenant en compte les caractéristiques intrinsèques de l’individu.

### Fichiers utilisés

- Time-Series-Analysis 21 mois.ipynb
- clients_clustered_by_arima_coef.csv
- clients_clustered_by_arima_coef_DBSCAN.csv
- arimax_dataset.csv 
- mse_ar_ma_arma_arima.ipynb
- clustering_clients_by_arima_coef_DBSCAN.ipynb
- clustering_clients_by_arima_coef_KMEANS.ipynb
- mse_ar_ma_arma_arima.ipynb
- clients_menages_tabular_transfo.csv

## Régression

Dans cette approche, nous souhaitons faire une régression et ainsi omettre l’aspect daté de nos données. On cherche dans un premier temps à prédire le solde puis la dette relative du prochain mois (variable à expliquer) par le solde (puis la dette relative) des x mois précédents (variables explicatives), avec x à déterminer.

### Fichiers utilisés

- AP01_TimePeriod_Selection.ipynb
- 4mois_Regression_regression_sur_la_dette.ipynb
- 7mois_Regression_regression_sur_la_dette.ipynb
- 10mois_Regression_regression_sur_la_dette.ipynb
- regression_sur_la_dette.ipynb
- Clean_Dataset_output_clients_menages_tabular.csv

### Précisions

Le notebook AP01_TimePeriod_Selection.ipynb permet d'obtenir des informations sur les périodes les plus intéressantes à traiter, les notebook de régression 4mois, 7mois et 10mois appliquent les observations sur ces périodes.






