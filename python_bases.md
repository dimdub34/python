# Python

<img src="img/logo.png" alt="Python" style="height: 200px">

## Content

- [Introduction](#/1)
- [Installation](#/2)
- [Règles d'écriture](#/3)
- [Variables et types](#/4)
- [Chaînes de caractères](#/5)
- [Types numériques](#/6)
- [Booléen](#/7)
- [Liste](#/8)
- [Tuple](#/9)
- [Dictionnaire](#/10)
- [Set](#/11)

# Introduction

- créé par Guido Van Rossum (Néerlandais)
- la 1ère version en 1991
- géré par la Python Software Fondation, depuis 2001
- site web : [https://www.python.org](https://www.python.org)
- Python vient de "Monty Python" une troupe d'humoristes anglais ([wikipedia](https://fr.wikipedia.org/wiki/Monty_Python))
- actuellement version 3.12

<img src="img/guido.jpg" alt="Guido Van Rossum" style="height: 200px">

- language de haut niveau
- syntaxe simple
- language interprété
- multiplateforme
- peut être utilisé pour des scripts simples ou des applications complexes
- utilisation croissante pour l'analyse de données et le machine learning

# Installation

## Anaconda 

- distribution Python avec de nombreux packages et outils pré-installés
- permet une installation séparée de celle du système d'exploitation
- permet de créer des environnements virtuels, c'est à dire différentes installations de Python (versions et/ou packages)
- site web : [https://www.anaconda.com](https://www.anaconda.com)

<img src="img/anaconda.png" alt="Anaconda Logo" style="width: 250px">

## L'interpréteur Python

L'interpréteur Python exécute le code Python ligne par ligne, permettant une exécution immédiate : 
- Traduction du code source Python en instructions machine compréhensibles par l'ordinateur.
- Interaction interactive via le mode REPL (**Read-Eval-Print Loop**).

L'interpréteur Python installé avec Anaconda peut-être démarré en ouvrant un terminal Anaconda (Anaconda Prompt) puis en tapant `python`.

## L'interpréteur Jupyter

- Un environnement interactif utilisé pour écrire et exécuter du code dans un navigateur.
- Idéal pour des démonstrations et des analyses de données.
- La distribution **Anaconda** inclut Jupyter Notebook par défaut.
- Permet d'exécuter des cellules contenant du code, du texte ou des graphiques.

Pour démarrer Jupyter, ouvrir un terminal Anaconda (Anaconda Prompt) puis taper `jupyter-lab`

## Pratique

Démarrer Jupyter-lab et créer un notebook.

# Règles d'écriture

## The Zen of Python

Le *Zen of Python*, écrit par Tim Peters, est une collection de principes qui guide la conception de Python. Ces principes peuvent être affichés en tapant `import this` dans un interpréteur Python. Ces principes ne sont pas absolus, mais ils reflètent la philosophie générale de Python et encouragent des pratiques de programmation propres et efficaces.

1. **Beautiful is better than ugly.** : La beauté est préférable à la laideur.
2. **Explicit is better than implicit.** : L'explicite est préférable à l'implicite.
3. **Simple is better than complex.** : La simplicité est préférable à la complexité.
4. **Complex is better than complicated.** : La complexité est préférable à la complication.
5. **Flat is better than nested.** : Le plat est préférable à l'imbrication.
6. **Sparse is better than dense.** : L'aéré est préférable au dense.
7. **Readability counts.** : La lisibilité compte.
8. **Special cases aren't special enough to break the rules.** : Les cas particuliers ne sont pas suffisamment spéciaux pour briser les règles.

9. **Although practicality beats purity.** : Cependant, la praticité l'emporte sur la pureté.
10. **Errors should never pass silently.** : Les erreurs ne devraient jamais passer silencieusement.
11. **Unless explicitly silenced.** : Sauf si elles sont explicitement ignorées.
12. **In the face of ambiguity, refuse the temptation to guess.** : Face à l'ambiguïté, refusez la tentation de deviner.
13. **There should be one-- and preferably only one --obvious way to do it.** : Il devrait y avoir une — et de préférence une seule — manière évidente de le faire.
14. **Although that way may not be obvious at first unless you're Dutch.** : Cependant, cette manière peut ne pas être évidente au premier abord, sauf si vous êtes Néerlandais.
15. **Now is better than never.** : Maintenant est préférable à jamais.
16. **Although never is often better than *right* now.** : Bien que jamais soit souvent préférable à "tout de suite".
17. **If the implementation is hard to explain, it's a bad idea.** : Si l'implémentation est difficile à expliquer, c'est une mauvaise idée.
18. **If the implementation is easy to explain, it may be a good idea.** : Si l'implémentation est facile à expliquer, c'est peut-être une bonne idée.
19. **Namespaces are one honking great idea -- let's do more of those!** : Les espaces de noms sont une idée géniale – utilisons-les davantage !

## Indentation

- Python utilise l'**indentation** pour structurer le code (au lieu des accolades `{}` dans d'autres langages).
- Chaque niveau doit être **aligné** (généralement 4 espaces par niveau).

*Exemple* :

```python
if x > 0:
    print("x est positif")
else:
    print("x est négatif ou nul")
```

## Sensibilité à la casse

Python est sensible à la casse : `Variable` et `variable` sont deux noms différents.  
Bonne pratique : utiliser des noms en minuscules pour les variables et des MajusculesInitiales pour les classes.

## Noms de variables

Caractères autorisés : Lettres (a-z, A-Z), chiffres (0-9), underscore (_).  
Ne pas commencer par un chiffre.  
Interdits : Noms réservés comme `if`, `for`, `print`, etc.  

Utiliser des noms explicites

```python
age_utilisateur = 30  # Clair
a = 30  # Peu clair
```

## Commentaires

Commentaires sur une seule ligne : Utiliser `#`.

```python
print("Bonjour")  # Commentaire en ligne
```

Commentaires multi-lignes : Utiliser des guillemets triples `"""` ou `'''`.

```python
"""
Ce programme calcule la somme
de deux nombres.
"""
```

## Guillemets

Python accepte les guillemets simples `'` ou doubles `"`.

```python
texte1 = "Bonjour"
texte2 = 'Bienvenue'
```

Pour des chaînes contenant des guillemets, alterner ou échapper

```python
texte1 = "Il a dit : 'Python est génial !'"
texte2 = "Il a dit : \"Python est génial !\""
```

# Variables et Types

## Création de variable

Une variable est une étiquette pour un objet stocké en mémoire. 
Utilisation du signe `=` 

```python
x = 5  # Affectation d'un entier
y = "Python"  # Affectation d'une chaîne de caractères
print(x, y)  # Affiche : 5 Python
```

La fonction `print` affiche des valeurs ou des messages dans la console.

## Typage dynamique 

L'interpréteur Python détermine automatiquement le `type` de la variable, en fonction de la valeur qui lui est affectée.  
La fonction `type()` appelée avec une variable en argument retourne le type de la variable.

```python
x = 42
print(type(x))  # Affiche : <class 'int'>
x = "Bonjour"
print(type(x))  # Affiche : <class 'str'>
```

## Les types intégrés (built-in types)

"Intégré" signifie que ces types sont fournis par défaut dans Python.  
Ces types permettent de :

- Représenter des données courantes (nombres, texte, etc.).
- Réaliser des opérations de base comme des calculs, des manipulations de texte, ou la gestion de collections.

- `None`: Valeur spéciale représentant "rien" ou "absence" (None).  
- `str` : Texte (ex. "Bonjour", 'Python')   
- `int` : Entiers (ex. 42, -5)
- `float` : Nombres décimaux (ex. 3.14, -0.01)
- `complex` : Nombres complexes (ex. 3 + 4j)
- `bool` : Valeurs logiques (True, False)
- `list` : Liste ordonnée, modifiable (ex. `[1, 2, 3]`)
- `tuple` : Liste ordonnée, non modifiable (ex. `(1, 2, 3)`)
- `dict` : Association clé-valeur (ex. `{"nom": "Alice", "âge": 30}`)
- `set` : Ensemble non ordonné, sans doublons (ex. `{1, 2, 3}`)

# Les chaînes de caractères

## Présentation 

- Une **chaîne de caractères** (type `str`) est une séquence de caractères.
- Elle est délimitée par des guillemets simples `'` ou doubles `"`.

_Exemples_ :

```python
texte1 = "Bonjour"
texte2 = 'Python est génial !'
```

Indexation possible : Chaque caractère est accessible par son indice.

```python
texte = "Python"
print(texte[0])  # Affiche : P
print(texte[1]) # Affiche : y
```

Une fois créées, les chaînes ne peuvent pas être modifiées directement, on dit quelles sont `immuables`.  

```python
texte[0] = "L"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [3], in <cell line: 1>()
----> 1 texte[0] = "L"

TypeError: 'str' object does not support item assignment
```

## Méthodes courantes pour les chaînes de caractères

- **`upper()`** : Convertit la chaîne en majuscules.
- **`lower()`** : Convertit la chaîne en minuscules.
- **`count(substring)`** : Compte le nombre d’occurrences d’un sous-texte.
- **`replace(old, new)`** : Remplace une sous-chaîne par une autre.

_Exemples_ : 
```python
texte = "Bonjour"
print(texte.upper())  # Affiche : BONJOUR
print(texte.lower())  # Affiche : bonjour

texte = "Python est Pythonique"
print(texte.count("Python"))  # Affiche : 2
print(texte.replace("Python", "Génial"))  # Affiche : Génial est Génialique
```

## Gestion des espaces et découpage

- **`strip()`** : Supprime les espaces au début et à la fin.
- **`split(separator)`** : Découpe une chaîne en liste.
- **`join(iterable)`** : Assemble une liste en chaîne.

_Exemples_ : 

```python
texte = "  Bonjour Python  "
print(texte.strip())  # Affiche : Bonjour Python

texte2 = "Python est génial"
print(texte2.split())  # Affiche : ['Python', 'est', 'génial']

liste = ["Python", "est", "génial"]
print(" ".join(liste))  # Affiche : Python est génial
```

## Les f-strings

- Pour formater les chaînes.
- Permettent d’insérer des variables ou des expressions directement dans une chaîne.
- Syntaxe : **`f"texte {variable}"`**

_Exemples_ :
```python
nom = "Alice"
age = 30

print(f"Bonjour {nom}, vous avez {age} ans.")
# Affiche : Bonjour Alice, vous avez 30 ans.

# Calculs dans les f-strings
print(f"5 + 3 = {5 + 3}")
# Affiche : 5 + 3 = 8
```

## Pratique

### Exercice 1 : Manipuler la casse
1. Déclarez une variable contenant le texte : `"Python est amusant !"`.
2. Convertissez cette chaîne en majuscules.
3. Convertissez cette chaîne en minuscules.
4. Affichez les résultats avec la fonction `print`.

### Exercice 2 : Compter et remplacer

1. Déclarez une chaîne contenant : `"Python est Pythonique car Python est simple."`
2. Comptez combien de fois le mot `"Python"` apparaît dans cette chaîne.
3. Remplacez tous les `"Python"` par `"Génial"`.
4. Affichez les résultats.

### Exercice 3 : Découper et assembler

1. Déclarez une chaîne contenant : `"Apprendre Python pas à pas"`.
2. Séparez cette chaîne en une liste de mots.
3. Réassemblez les mots en une nouvelle chaîne, séparés par un tiret `"-"`.
4. Affichez la liste des mots et la nouvelle chaîne.

### Exercice 4 : Les f-strings

1. Déclarez deux variables : `nom = "Alice"` et `age = 25`.
2. Utilisez un f-string pour afficher : `"Bonjour Alice, vous avez 25 ans."`
3. Modifiez la variable `age` en lui ajoutant 5, et affichez à nouveau la phrase : `"Bonjour Alice, vous aurez 30 ans dans 5 ans."`

### Exercice 5 : Combiner les méthodes

1. Déclarez une chaîne : `"   Python est simple mais puissant.   "`
2. Supprimez les espaces au début et à la fin de la chaîne.
3. Convertissez la chaîne en majuscules.
4. Remplacez `"PUISSANT"` par `"INCROYABLE"`.
5. Séparez les mots dans une liste et affichez-les.

# Les types numériques

## Liste des types et caractéristiques 

- **int** : Entiers (ex. `42`, `-5`)
- **float** : Nombres décimaux (ex. `3.14`, `-0.01`)
- **complex** : Nombres complexes (ex. `2 + 3j`)

**Caractéristiques**
- Les entiers (`int`) peuvent être de taille illimitée.
- Les flottants (`float`) utilisent une précision limitée (base 64 bits).
- Les conversions entre types se font facilement

```python
  print(float(42))  # 42.0
  print(int(3.14))  # 3
  print(complex(2, 3))  # (2+3j)
```

## Opérations sur les types numériques

- Addition : `+`
- Soustraction : `-`
- Multiplication : `*`
- Division : `/`
- Division entière : `//`
- Modulo : `%`
- Puissance : `**`

_Exemples_ :
```python
print(10 + 3)  # 13
print(10 // 3)  # 3
print(2 ** 3)  # 8
print(10 % 3)  # 1
```

## Fonctions courantes
- `abs(x)` : Valeur absolue.
- `round(x, n)` : Arrondit x à n décimales.
- `pow(x, y)` : Puissance de x à la y.
- `divmod(a, b)` : Retourne `(a // b, a % b)`.

_Exemples_ :
```python
print(abs(-42))  # 42
print(round(3.14159, 2))  # 3.14
print(pow(2, 3))  # 8
print(divmod(10, 3))  # (3, 1)
```

## Le module `math`

Contient des attributs et méthodes utiles :  
- `sqrt(x)` : Racine carrée.
- `log(x)` : Logarithme naturel.
- `sin(x)`, `cos(x)` : Fonctions trigonométriques.
- `pi` : le nombre Pi

```python
import math
print(math.sqrt(16))  # 4.0
print(math.log(10))  # 2.302585...
```

## Le module `decimal`

- En Python, les flottants (`float`) sont représentés selon la norme **IEEE 754** (base 64 bits).
- Cette représentation peut entraîner des erreurs d’arrondi, comme :
  ```python
  print(0.1 + 0.2)  # Affiche : 0.30000000000000004
  ```

Le module decimal permet de manipuler des nombres en évitant ces erreurs.  

```python
from decimal import Decimal
x = Decimal("0.1")
y = Decimal("0.2")
print(x + y)  # Affiche : 0.3
```

Utiliser des chaînes de caractères pour initialiser les `Decimal`.

La précision peut être configurée avec `getcontext`

```python
from decimal import Decimal, getcontext
getcontext().prec = 50  # Définit la précision à 50 chiffres

x = Decimal("1") / Decimal("7")
print(x)  # Affiche : 0.14285714285714285714285714285714285714285714285714
```

Le module `decimal` est adapté aux applications financières, scientifiques ou toute situation où les erreurs d’arrondi doivent être évitées. Mais, attention , il est plus lent que les flottants natifs, car Decimal effectue des calculs supplémentaires pour maintenir la précision.

## Pratique

### Exercice 1 : Opérations simples
- Créez deux variables a et b contenant respectivement les valeurs 15 et 7.
- Calculez et affichez :
    + La somme de a et b.
    + Leur différence.
    + Leur produit.
    + Le quotient (division).
    + Le reste de la division de a par b.

### Exercice 2 : Puissance et racine carrée

- Calculez $2^8$ (2 puissance 8).
- La racine carrée de 144 (utilisez le module math).

### Exercice 3 : Calculs avec des flottants

- Déclarez deux nombres flottants x = 0.1 et y = 0.2.
- Calculez et affichez :
    - Leur somme (montrez l'erreur d'arrondi de Python).
    - Leur somme précise en utilisant le module decimal.

### Exercice 4 : Utilisation de divmod()

- Déclarez deux variables a = 50 et b = 6.
- Utilisez la fonction divmod() pour obtenir :
    - Le quotient entier.
    - Le reste.
- Affichez les résultats séparément.

# Le type booléen

## Présentation

- Un booléen peut être :
  - `True` : Vrai
  - `False` : Faux
- Utilisé pour contrôler la logique des programmes :
  - Conditions
  - Boucles
  - Expressions logiques

## Fonction `bool()`

- En Python, tout objet peut être converti en booléen.
- Les valeurs suivantes sont `False` :
  - `0`, `0.0`
  - `None`
  - Chaîne vide : `""`
  - Liste/dictionnaire/vecteur vide : `[]`, `{}`

_Exemples_ :
```python
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("Hello")) # True
```

## Les opérateurs logiques

- **`and`** : Vrai si **les deux** conditions sont vraies.
- **`or`** : Vrai si **au moins une** condition est vraie.
- **`not`** : Inverse la valeur logique.

_Exemples_ :
```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

## Les opérateurs de comparaison

- Égalité : `==`
- Différence : `!=`
- Plus grand/plus petit : `>`, `<`, `>=`, `<=`

_Exemple_ :
```python
x = 10
y = 20

print(x > y)   # False
print(x == 10) # True
```

## Pratique

### Exercice 1 : Comprendre les booléens

Déclarez deux variables :
```python
a = True
b = False
```
Calculez et affichez :
```python
a and b
a or b
not a
```

### Exercice 2 : Conversion en booléen

Déclarez les variables suivantes :
```python
x = 0
y = 42
texte = ""
texte2 = "Python"
```

Affichez leur conversion en booléen avec bool().

### Exercice 3 : Comparaisons

- Déclarez deux variables `a = 10` et `b = 20`.
- Effectuez et affichez les comparaisons suivantes :
    - `a > b`
    - `a == b`
    - `a <= b`
    - `a != b`

### Exercice 4 : Expression logique combinée

- Déclarez une variable `x = 15`.
- Évaluez et affichez les expressions suivantes :
    - `(x > 10) and (x < 20)`
    - `(x < 10) or (x == 15)`
    - `not (x == 15)`

# La liste

## Présentation

- Une liste est une collection **ordonnée** et **modifiable** : les éléments ont un index, de `0` à `len(liste)-1`.
- Elle peut contenir des éléments de types différents.
- Définie par des crochets `[]` et séparée par des virgules.

_Exemple_ :
```python
ma_liste1 = [1, 2, 3, "Python", True]
print(ma_liste1)  # [1, 2, 3, 'Python', True]

ma_liste2 = ["a", "b", "c"]
print(ma_liste2[0])  # 'a' (1er élément)
print(ma_liste2[-1]) # 'c' (dernier élément)
```

## Ajouter des éléments

1. **`append(element)`** : Ajoute un élément à la fin.
2. **`extend(iterable)`** : Ajoute plusieurs éléments à la fin.
3. **`insert(index, element)`** : Insère un élément à un index spécifique.

_Exemple_ :
```python
ma_liste = [1, 2, 3]
ma_liste.append(4)       # [1, 2, 3, 4]
ma_liste.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
ma_liste.insert(2, "X")  # [1, 2, 'X', 3, 4, 5, 6]
```

## Supprimer des éléments

- **`remove(element)`** : Supprime la 1re occurrence d’un élément.
- **`pop(index)`** : Supprime l’élément à un index (par défaut, le dernier).
- **`clear()`** : Vide complètement la liste.

```python
ma_liste = [1, 2, 3, 4]
ma_liste.remove(3)   # [1, 2, 4]
ma_liste.pop(1)      # [1, 4]
ma_liste.clear()     # []
```

## Trier et inverser une liste

1. **`sort()`** : Trie une liste en place (croissant par défaut).
2. **`reverse()`** : Inverse l’ordre des éléments.

_Exemple_ :
```python
ma_liste = [4, 1, 3, 2]
ma_liste.sort()      # [1, 2, 3, 4]
ma_liste.reverse()   # [4, 3, 2, 1]
```

## Autres méthodes utiles

- **`count(element)`** : Retourne le nombre d'occurrences d’un élément.
- **`index(element)`** : Retourne l’index de la 1re occurrence d’un élément.

```python
ma_liste = [1, 2, 3, 2, 1]
print(ma_liste.count(2))  # 2
print(ma_liste.index(3))  # 2
```

## Accéder à des sous-listes (découpage ou "slicing")

```python
ma_liste = [0, 1, 2, 3, 4, 5]
print(ma_liste[1:4])  # [1, 2, 3]
print(ma_liste[:3])   # [0, 1, 2]
print(ma_liste[3:])   # [3, 4, 5]
```

## Parcourir une liste avec une boucle for

Par valeur 

```python
ma_liste = ["Python", "est", "génial"]
for element in ma_liste:
    print(element)
# Affiche : Python, est, génial
```

Par index et valeur avec `enumerate`

```python
ma_liste = ["Python", "est", "génial"]
for index, element in enumerate(ma_liste):
    print(f"{index}: {element}")
# Affiche : 0: Python, 1: est, 2: génial
```

## Pratique

### Exercice 1 : Création et accès aux éléments

- Créez une liste contenant les éléments suivants : "Python", "Java", "C++", "Ruby".
- Affichez :
    - Le premier élément.
    - Le dernier élément.
    - Les deux premiers éléments (en utilisant le slicing).

### Exercice 2 : Ajouter et supprimer des éléments

- Créez une liste vide.
- Ajoutez successivement les nombres 1, 2 et 3 à la liste.
- Supprimez le deuxième élément (index 1).
- Affichez la liste après chaque opération.

### Exercice 3 : Parcourir une liste

- Créez une liste contenant les nombres de 1 à 5.
- Parcourez la liste avec une boucle et affichez chaque élément multiplié par 2.

### Exercice 4 : Trier et inverser une liste

- Créez une liste contenant les nombres suivants : 4, 1, 3, 2.
- Triez la liste en ordre croissant.
- Inversez l’ordre des éléments.
- Affichez les résultats après chaque opération.

### Exercice 5 : Méthodes count et index

- Créez une liste contenant : `[1, 2, 3, 2, 4, 2]`.
- Comptez combien de fois le nombre 2 apparaît dans la liste.
- Trouvez l’index de la première occurrence du nombre 3.

### Exercice 6 : Sous-listes (slicing)

- Créez une liste contenant les nombres de 0 à 9.
- Extrayez et affichez :
    - Les trois premiers éléments.
    - Les trois derniers éléments.
    - Les éléments situés aux index pairs (0, 2, 4…).

# Le tuple

## Présentation

- Un **tuple** est une collection **ordonnée** et **non modifiable** (*immuable*, une fois créé, un tuple ne peut pas être modifié).
- Comme les listes, un tuple peut contenir des éléments de types différents.
- Délimité par des parenthèses `()`.

_Exemple_ :
```python
mon_tuple = (1, 2, 3, "Python", True)
print(mon_tuple)  # (1, 2, 3, 'Python', True)
```

## Avantages des tuples

1. **Immuabilité** :
   - Idéal pour des données constantes.
   - Plus sûr, car les tuples ne peuvent pas être modifiés accidentellement.
2. **Efficacité** :
   - Les tuples sont généralement plus rapides que les listes.
3. **Clé dans un dictionnaire** :
   - Les tuples peuvent être utilisés comme clés (contrairement aux listes).

_Cas d'utilisation_ :
```python
coordonnees = (43.6, 3.9)  # Latitude, longitude
jours_semaine = ("lundi", "mardi", "mercredi", "jeudi", "vendredi")
```

## Accès aux éléments

- Comme les listes, on utilise les **indices** pour accéder aux éléments.
- **Découpage (slicing)** est également possible.

_Exemple_ :
```python
mon_tuple = (10, 20, 30, 40, 50)
print(mon_tuple[1])    # 20
print(mon_tuple[:3])   # (10, 20, 30)
print(mon_tuple[-2:])  # (40, 50)
```

## Opérations courantes

- Concaténation : Ajouter deux tuples ensemble.
- Répétition : Répéter un tuple plusieurs fois.

```python
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)   # (1, 2, 3, 4, 5)
print(t1 * 2)    # (1, 2, 3, 1, 2, 3)
```

## Vérification d'appartenance

`in` : Vérifie si un élément est dans un tuple.

```python
mon_tuple = (1, 2, 3, 4)
print(3 in mon_tuple)   # True
print(5 in mon_tuple)   # False
```

## Méthodes

- **`count(element)`** : Compte le nombre d’occurrences d’un élément.
- **`index(element)`** : Retourne l’index de la première occurrence d’un élément.

_Exemple_ :
```python
mon_tuple = (1, 2, 2, 3, 4)
print(mon_tuple.count(2))  # 2
print(mon_tuple.index(3))  # 3
```

## Conversion entre liste et tuple

**tuple vers liste**

```python
t = (1, 2, 3)
l = list(t)
print(l)  # [1, 2, 3]
```

**liste vers tuple**

```python
l = [4, 5, 6]
t = tuple(l)
print(t)  # (4, 5, 6)
```

## Itération et déballage

**Itération** 

```python
mon_tuple = ("a", "b", "c")
for element in mon_tuple:
    print(element)
# Affiche : a, b, c
```

**Déballage**

```python
coordonnees = (43.6, 3.9)
latitude, longitude = coordonnees
print(latitude)  # 43.6
print(longitude) # 3.9
```

## La fonction `zip`

- La fonction **`zip`** combine plusieurs collections (listes, tuples, etc.) **élément par élément**.
- Retourne un objet `zip` contenant des **tuples** regroupant les éléments correspondants de chaque collection.
- Les collections doivent avoir des tailles similaires pour que tous les éléments soient pris en compte.
- Si les collections ont des longueurs différentes, zip s'arrête au plus court.

_Exemple_ :

```python
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

resultat = zip(noms, ages)
print(list(resultat))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

`*` pour "dézipper" des collections combinées.

```python
combines = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
noms, ages = zip(*combines)

print(noms)  # ('Alice', 'Bob', 'Charlie')
print(ages)  # (25, 30, 35)
```

## Pratique

### Exercice 1 : Création et accès

- Créez un tuple contenant les éléments suivants : ("Python", "Java", "C++", "Ruby").
- Affichez :
    - Le premier élément.
    - Le dernier élément.
    - Les deux premiers éléments (en utilisant le slicing).

### Exercice 2 : Déballage d’un tuple

- Créez un tuple contenant : (2024, "Décembre", 1).
- Déballez ce tuple dans trois variables : annee, mois, jour.
- Affichez ces variables.

### Exercice 3 : Conversion liste ↔ tuple

- Créez une liste contenant : `[10, 20, 30]`.
- Convertissez cette liste en un tuple.
- Convertissez ce tuple en une liste et ajoutez-y l’élément 40.

### Exercice 4 : Combinaison de collections

- Créez deux listes :
    - noms = ["Alice", "Bob", "Charlie"]
    - ages = [25, 30, 35]
- Utilisez zip pour associer chaque nom à un âge.
- Affichez le résultat sous forme de liste de tuples.

### Exercice 5 : Dézipper des données

- Créez une liste : `[("Alice", 25), ("Bob", 30), ("Charlie", 35)]`.
- Utilisez zip pour séparer les noms et les âges dans deux tuples distincts.
- Affichez-les.

### Exercice 6 : Liste indexée

- Créez une liste contenant les éléments suivants : ["Chat", "Chien", "Oiseau"].
- Transformez cette liste en une liste de tuples avec les indices en utilisant enumerate.

# Le dictionnaire

## Présentation

- Un **dictionnaire** est une collection modifiable et indexée.
- Il associe des **clés** à des **valeurs**. Chaque clé est unique et sert d’identifiant pour accéder à une valeur.
- Délimité par des accolades `{}`.

_Exemple_ :

```python
mon_dictionnaire = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(mon_dictionnaire["nom"])  # Alice
print(mon_dictionnaire["âge"])  # 25
print(mon_dictionnaire)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

## Caractéristiques

- Clés uniques : Chaque clé dans un dictionnaire est unique.
- Indexation par clé : Les valeurs sont accessibles via leur clé.
- Modifiable : Les paires clé-valeur peuvent être ajoutées, modifiées ou supprimées.
- Types acceptés :
    - Les clés doivent être immutables (types : `str`, `int`, `tuple`, etc.).
    - Les valeurs peuvent être de tout type.

## Ajouter ou modifier une paire clé-valeur

```python
    dictionnaire["nouvelle_cle"] = "nouvelle_valeur"
    
    mon_dictionnaire = {"nom": "Alice"}
    mon_dictionnaire["age"] = 25  # Ajout
    mon_dictionnaire["nom"] = "Bob"  # Modification
    print(mon_dictionnaire)  # {'nom': 'Bob', 'age': 25}
```

## Supprimer une paire clé-valeur

- `pop(key)` : Supprime une clé et retourne sa valeur.
- `del dictionnaire[key]` : Supprime la clé sans retour de valeur.
- `clear()` : Vide complètement le dictionnaire.

```python
mon_dictionnaire = {"nom": "Alice", "age": 25}
mon_dictionnaire.pop("age")         # Supprime et retourne 25
del mon_dictionnaire["nom"]         # Supprime la clé "nom"
mon_dictionnaire.clear()            # Vide le dictionnaire
```

## Obtenir les clés, valeurs, et paires clé-valeur

1. **`keys()`** : Retourne les clés du dictionnaire.
2. **`values()`** : Retourne les valeurs.
3. **`items()`** : Retourne les paires clé-valeur sous forme de tuples.

_Exemple_ :
```python
mon_dictionnaire = {"nom": "Alice", "age": 25}
print(mon_dictionnaire.keys())   # dict_keys(['nom', 'age'])
print(mon_dictionnaire.values()) # dict_values(['Alice', 25])
print(mon_dictionnaire.items())  # dict_items([('nom', 'Alice'), ('age', 25)])
```

## Parcourir les clés, les valeurs, et les paires clé-valeur

**Les clés** 

```python
mon_dictionnaire = {"nom": "Alice", "âge": 25, "ville": "Paris"}
for cle in mon_dictionnaire:
    print(cle)
# Affiche : nom, âge, ville
```
**Les valeurs** 
```python
for valeur in mon_dictionnaire.values():
    print(valeur)
# Affiche : Alice, 25, Paris
```

**Les paires**
```python
for cle, valeur in mon_dictionnaire.items():
    print(f"{cle}: {valeur}")
# Affiche :
# nom: Alice
# âge: 25
# ville: Paris
```

## Créer un dictionnaire avec `zip`

```python
cles = ["nom", "age", "ville"]
valeurs = ["Alice", 25, "Paris"]
dictionnaire = dict(zip(cles, valeurs))
print(dictionnaire)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

## Trier un dictionnaire 

**Par clé**
```python
scores = {"Bob": 75, "Alice": 50, "Charlie": 100}
scores_tries = dict(sorted(scores.items())
print(scores_tries)  # {'Alice': 50, 'Bob': 75, 'Charlie': 100}
```

**Par valeur**
```python
scores = {"Alice": 50, "Bob": 75, "Charlie": 100}
scores_tries = dict(sorted(scores.items(), key=lambda x: x[1]))
print(scores_tries)  # {'Alice': 50, 'Bob': 75, 'Charlie': 100}
```

## Fusionner deux dictionnaires

```python
dict1 = {"nom": "Alice", "âge": 25}
dict2 = {"ville": "Paris", "profession": "Ingénieure"}
fusion = {**dict1, **dict2}
print(fusion)
# {'nom': 'Alice', 'âge': 25, 'ville': 'Paris', 'profession': 'Ingénieure'}
```

## Pratique

### Exercice 1 : Création et accès

- Créez un dictionnaire contenant les informations suivantes :
    - nom: "Alice"
    - âge: 25
    - ville: "Paris"
- Affichez :
    - La valeur associée à la clé "nom".
    - La valeur associée à la clé "âge".
- Ajoutez une nouvelle clé profession avec la valeur "Ingénieure".

### Exercice 2 : Modification et suppression

- Modifiez l’âge de l’étudiante "Alice" à 30.
- Supprimez la clé "ville".
- Affichez le dictionnaire mis à jour.

### Exercice 3 : Vérification d’existence

- Créez un dictionnaire `inventaire = {"pommes": 10, "bananes": 20, "oranges": 15}`.
- Vérifiez si les clés "pommes" et "raisins" existent dans le dictionnaire.
- Ajoutez "raisins" avec une quantité de 5 uniquement si cette clé n’existe pas encore.

### Exercice 4 : Parcourir un dictionnaire

- Créez un dictionnaire contenant :
    - math: 18
    - anglais: 16
    - informatique: 20
- Parcourez le dictionnaire pour afficher :
    - Chaque matière et sa note.
    - La moyenne des notes.

### Exercice 5 : Compter les occurrences

- Créez une chaîne de caractères : "abracadabra".
- Comptez le nombre d’occurrences de chaque caractère dans la chaîne et stockez-les dans un dictionnaire.


### Exercice 6 : Fusionner deux dictionnaires

- Créez deux dictionnaires :
    - `personne = {"nom": "Alice", "âge": 25}`
    - `infos = {"ville": "Paris", "profession": "Ingénieure"}`
- Fusionnez-les dans un nouveau dictionnaire.

### Exercice 7 : Trier un dictionnaire

- Créez un dictionnaire contenant les notes suivantes : `{"Alice": 85, "Bob": 70, "Charlie": 90}`
- Triez le dictionnaire :
    - Par clé (ordre alphabétique).
    - Par valeur (ordre croissant).

# Le set

## Présentation

- Un **set** est une collection **non ordonnée** et **sans doublons**.
- Délimité par des accolades `{}` ou créé avec la fonction **`set()`**.
- Utile pour effectuer des opérations mathématiques comme les **unions**, **intersections**, et **différences**.

_Exemple_ :

```python
mon_set = {1, 2, 3, 3, 4}
print(mon_set)  # {1, 2, 3, 4} (les doublons sont supprimés)

vide = set()  # Créer un set vide
print(type(vide))  # <class 'set'>
```

## Caractéristiques

- Non ordonnés : Les éléments ne sont pas stockés dans un ordre particulier.
- Sans doublons : Chaque élément est unique.
- Modifiables : Vous pouvez ajouter ou supprimer des éléments.
- Incompatibles avec des types non hashables : les clés doivent être immuables (pas de listes ou dictionnaires dans un set).

## Ajouter des éléments

```python
mon_set = {1, 2, 3}
mon_set.add(4)
print(mon_set)  # {1, 2, 3, 4}
```



## Supprimer des éléments

- **`remove(element)`** : Supprime un élément. Lève une erreur si l’élément n’existe pas.
- **`discard(element)`** : Supprime un élément sans lever d’erreur.
- **`pop()`** : Supprime un élément arbitraire (car le set est non ordonné).
- **`clear()`** : Vide le set.

```python
mon_set = {1, 2, 3}
mon_set.remove(2)   # Supprime 2
mon_set.discard(4)  # Ne fait rien (4 n'existe pas)
print(mon_set)      # {1, 3}
```

## Opérations sur les ensembles

### Union

Combine les éléments de deux sets (**`|`** ou **`union()`**).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)          # {1, 2, 3, 4, 5}
print(set1.union(set2))     # {1, 2, 3, 4, 5}
```

### Intersection

Trouve les éléments communs (& ou intersection()).

```python
print(set1 & set2)          # {3}
print(set1.intersection(set2))  # {3}

```

### Différence

Trouve les éléments dans un set mais pas dans l’autre (- ou difference()).
```python
print(set1 - set2)          # {1, 2}
print(set1.difference(set2))  # {1, 2}
```


### Différence symétrique

Trouve les éléments présents dans un seul des deux sets (^ ou symmetric_difference()).

```python
print(set1 ^ set2)                  # {1, 2, 4, 5}
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}
```

## Applications pratiques 

### Suppression des doublons

```python
liste = [1, 2, 3, 1, 2, 4]
unique = set(liste)
print(unique)  # {1, 2, 3, 4}
```

### Union, intersection et différence

```python
maths = {"Alice", "Bob", "Charlie"}
informatique = {"Alice", "David", "Charlie"}

# Étudiants inscrits à au moins une matière
print(maths | informatique)  # Union

# Étudiants inscrits aux deux matières
print(maths & informatique)  # Intersection

# Étudiants inscrits uniquement en maths
print(maths - informatique)  # Différence
maths = {"Alice", "Bob", "Charlie"}
informatique = {"Alice", "David", "Charlie"}
```

## Pratique

### Exercice 1 : Création et ajout

- Créez un set contenant les éléments suivants : 1, 2, 3.
- Ajoutez les éléments 4 et 5 au set.
- Affichez le set mis à jour.

### Exercice 2 : Suppression d’éléments

- Créez un set contenant les éléments suivants : 10, 20, 30, 40.
- Supprimez l’élément 20 en utilisant remove().
- Essayez de supprimer l’élément 50 avec discard().
- Affichez le set après chaque opération.

### Exercice 3 : Suppression des doublons dans une liste

- Créez une liste contenant les éléments suivants : `[1, 2, 2, 3, 4, 4, 5]`.
- Transformez cette liste en un set pour supprimer les doublons.
- Convertissez à nouveau le set en liste.

### Exercice 4 : Vérification d’appartenance

- Créez un set contenant : `{"Alice", "Bob", "Charlie"}`.
- Vérifiez si "Alice" et "David" sont dans le set.

### Exercice 5 : Opérations ensemblistes

- Créez deux sets :
    - `set1 = {1, 2, 3, 4}`
    - `set2 = {3, 4, 5, 6}`
- Effectuez et affichez les résultats des opérations suivantes :
    - Union.
    - Intersection.
    - Différence (set1 - set2).
    - Différence symétrique.


### Exercice 6 : Opérations sur des mots

- Créez deux sets :
  - `vowels = {"a", "e", "i", "o", "u"}`
  - `letters_in_word = set("abracadabra")`
- Affichez :
  - Les voyelles présentes dans le mot (intersection).
  - Les voyelles absentes dans le mot (difference).


### Exercice 7 : Suppression des doublons et tri

- Créez une liste contenant les éléments suivants : `[4, 1, 3, 2, 3, 4, 5]`.
- Transformez la liste en set pour supprimer les doublons.
- Affichez les éléments triés.

# Structures conditionnelles et boucles
