# AP01 : Science des données pour la gestion de l’immobilier

Cet Atelier projet vise à explorer une base de données volumineuse liée à la gestion des locataires d'un bailleur social, notamment pour pouvoir identifier les locataires risquant de présenter des défauts de paiement, et pour leur apporter l'aide nécessaire au règlement de leur dette (que ce soit via de simples rappels ou des visites personnalisées). Ce projet se fait en lien avec SOPRA/STERIA d'une part, et le bailleur Habitat 76 d'autres part, qui apporteront la base de données et leur expertise sur le domaine.

L’objectif de cette collaboration est d’aider le bailleur dans sa prise de décision pour des problématiques liées aux locataires en défaut de paiement.

## Organisation du repo 

Le repo actuel est organisé par Axe:

### Axe 1 

Quelles sont les périodes de surendettement (été, Noël, début d’année) ? Quels sont les paramètres à l’origine de ce surendettement ? En déduire la probabilité qu’un individu possède une dette en vue de la période ?

* clustering
* classification

### Axe 2

Le but de l'étude dans l'axe 2 est de prédire si un individu sera endetté dans  les mois futurs en fonction de son historique. Plus précisément, nous voulons savoir si le client sera endetté dans trois mois.

* classification

### Axe 3

Le but de l'étude dans l'axe 3 est de répondre à la problématique suivante:  pour un individu en dette, sa dette va-t-elle augmenter, rester constante ou bien diminuer au bout de quelques mois ?

* séries temporlles
* régression

### Axe 4

Etude de l'impact de la clusturisation des individus. Est-ce que prédire la dette sur des sous groupes de population est plus précis ? quel est l'impact de la position géographique dans le niveau de la dette ?

* clusturing
* regression