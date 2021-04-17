# AXE 1

## Problématique

Quelles sont les périodes de surendettement (été, Noël, début d'année)? Quels sont les paramètres à l’origine de ce surendettement ? En déduire la probabilité qu'un individu possède une dette en vue de la période? 

## Objectif du code 

Ce protocole permet de prédire les périodes de surendettement. Il vise dans un premier temps à observer et mettre en avant des périodes propices au surendettement (été, Noël, début d’année …). 
Puis dans un second temps à analyser les paramètres à l'origine de ces tendances  par des méthodes de sélection de variables. Pour finir, ce protocole vise à prédire la probabilité qu’un nouveau client s’endette en vue de sa période d’entrée et des variables le caractérisant. 

## Contexte 

Pour répondre à cette problématique, il convient tout d’abord de définir ce qui caractérise un individu "endetté" ainsi qu’une période de "surendettement". En effet, ce n’est pas parce qu’un individu présente un solde débiteur pour un mois M unique que nous ne le représentons pas comme endetté. De même, si une personne observe une dette faible et constante sur plusieurs mois, nous ne la considérons pas comme endettée. 

Ainsi, nous avons choisi de réunir deux critères : un individu endetté est un individu qui contracte une dette d’un montant au moins supérieur à la moitié de son loyer et sur une période d’au moins deux mois consécutifs. Nous estimons judicieux de placer la durée à deux mois consécutifs car c’est le délai à partir duquel un propriétaire peut commencer des procédures de résiliations de baux en cas de loyers impayés. 
Concernant la définition de périodes de surendettement nous avons choisi de réunir un seul critère : une période de surendettement correspond à un laps de temps durant lequel le pourcentage de personnes endettées est nettement supérieur à la moyenne. 


## Données utilisées

Le jeu de données utilisé  est le fichier  csv “clients_menages_tabular.csv” résultant du code “preparation_donnees_tabulaire.py”. Le jeu de données obtenu s’intéresse uniquement aux données liées au client (compte client / contrat) et à son occupant social (ménage). Il décrit l’historique des clients locataires, avec chaque exemple (ligne) représentant un client unique et son historique collecté à partir du data warehouse. 

Le jeu de données final a été transformé et nettoyé, ce qui permet d’une part de supprimer les colonnes avec plus de 99.5% de données manquantes et les colonnes avec une seule valeur unique. Puis de réaliser des transformations permettant d’éviter la redondance des variables dont les valeurs ne changent pas aux cours du temps (comme les données relatives à l’élément louable) et de créer un dataframe avec une seule occurrence de ces valeurs mais avec l’intégralité de l’historique correspondant aux données relatives aux soldes qui fluctuent au cours du temps. 
De plus, nous avons transformé ce dataset en ne gardant seulement les ménages possédant un bail à partir du premier mois jusqu’au dernier. Ce choix nous permet de suivre l’évolution des dettes plus précisément sans que celle-ci soit biaisée par les locataires arrivant au cours de la période d’étude. 


## Méthodes utilisées

> La réalisation de ce protocole s’effectue par l’intermédiaire des étapes décrites ci-dessous.

> **1**. Réalisation d’une fonction dont les paramètres correspondent au critère défini ci-dessus de “surendettement” ainsi que le dataset. La sortie de 2. cette fonction est un graphique (histogramme, plot, boxplot …) permettant de visualiser les mois/périodes de surendettement. 

> **2**. Après isolation de ces périodes, pré-traitement des variables en ôtant les paramètres qui ont une corrélation supérieure à 0.9 avec le solde débiteur et en regroupant les paramètres fortement corrélés. Ces paramètres sont porteurs de la même information ce qui pourrait contrefaire notre sélection de variables à l’origine des périodes de surendettement. 

> **3** Aprés avoir étudié la corrélation de nos différents paramètres, nous avons décidé de garder uniquement les paramètres caractéristiques aux ménages et en oubliant les variables liées à une information à caractère économique. Réalisation de clustering à l'aide de méthode du coude et des K-Means. Analyse de la dispersion du montant de la dette ainsi que le pourcentage de personnes en surendettement en fonction de la période. 

> **4**. Étant donné le nombre important de prédicteurs nous allons effectuer une sélection de variables afin de ne garder que celles essentielles à notre étude. Nous allons envisager une telle sélection par pénalisation (Lasso, Ridge, Elastic net, Random Forest)

> **5**. Sélection du meilleur modèle minimisant un critère donné (Mean square error) ou par pénalisation. Pour comparer efficacement les modèles nous tracerons des boxplots des erreurs de Cross Validation et Nested Validation ainsi que les intervalles de confiances sur ces mêmes erreurs. 

> **6**. Après sélection des variables nous allons appliquer des algorithmes de classification binaire permettant de séparer nos clients en fonction de la présence d’un surendettement ou non. 

> **7**. Dans un premier temps nous allons parcourir l’intégralité du dataset afin de marquer par 1 les clients présentant un surendettement et par 0 les autres. 

> **8**. Sélection du meilleur modèle minimisant le taux d’erreur. Pour comparer efficacement les modèles nous tracerons des boxplots des erreurs de Cross Validation et Nested Validation ainsi que les intervalles de confiances sur ces mêmes erreurs. 

> **9**. Calcul d’un intervalle de confiance à l’aide de l’accuracy ainsi que la probabilité qu'une personne présente un surendettement en fonction de ses propres paramètres. 

