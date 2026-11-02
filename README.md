# TP 2 : Encapsulation et Composition en Python

## Module
Programmation orientée objet (POO) – Python

## Objectifs pédagogiques
- Comprendre le principe de l'encapsulation.
- Protéger les attributs d'une classe avec des attributs privés.
- Utiliser les méthodes pour accéder et modifier les données.
- Comprendre l'association entre classes à travers la composition.
- Mettre en pratique la relation « A un » (*Has-A*).

## Exercice 1 : Encapsulation
Mise en œuvre de l'encapsulation en Python afin de protéger les données d'un objet et contrôler leur accès à travers des méthodes appropriées.

## Exercice 2 : Composition entre classes

Création de deux classes :

**1. Classe `CompteBancaire`**
- Attribut privé `__solde`.
- Méthode `deposer(montant)` pour ajouter de l'argent.
- Méthode `retirer(montant)` pour effectuer un retrait.
- Méthode `get_solde()` pour consulter le solde.

**2. Classe `Client`**
- Attribut `nom`.
- Attribut `compte` contenant une instance de `CompteBancaire`.
- Méthode `afficher()` pour afficher les informations du client et le solde bancaire.




**Résultat obtenu :**

```text
Client : Yassir, Solde : 250.0€
```

## 📸 Captures d'écran

<img width="1366" height="768" alt="Capture d&#39;écran 2026-11-02 172819" src="https://github.com/user-attachments/assets/184f021c-94e6-4168-837d-a832a7222402" />

<img width="1366" height="768" alt="Capture d&#39;écran 2026-11-02 173716" src="https://github.com/user-attachments/assets/6cad76a9-08e4-43ef-b719-0c8b9d3d3e6e" />

##  Notions apprises
- Encapsulation et attributs privés.
- Constructeurs `__init__()`.
- Méthodes d'instance.
- Composition entre classes.
- Communication entre objets.
- Protection et manipulation des données.

##  État du TP
- Exercice 1 : Terminé
- Exercice 2 : Terminé



