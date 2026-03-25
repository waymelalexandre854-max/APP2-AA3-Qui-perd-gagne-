# APP2-AA3-Qui-perd-gagne-


Verify the comphrension of the problem / Set the structural challenges:

**Why the the 0 price is not a dominant strategy with the risque bonus ?**

With a relatively high value of the intensity of the risk premium alpha(α) ,rushing directly toward zero is not a predomiant strategy:
bid_cost(price) = base_cost + α/(price+1)

**Is the system a null sum system ? Justify** 

**What kind of informations are necessary to determine the winner?** 

The informations necessary to determine the winner is too reach the lowest score/price

• Peut-on déterminer le gagnant sans trier les prix ?

• Existe-t-il des structures qui permettent de maintenir les prix ordonnés
dynamiquement ?
• Quelle différence entre trier à la fin et maintenir l’ordre en permanence ?
• Si les mises arrivent en flux continu, quelle solution est la plus adaptée ?

Quelle est la complexité d’une insertion dans :
o Un tableau trié ?
o Un ABR équilibré ?
o Un dictionnaire + tri à la fin ?
• Dans quel cas un ABR peut-il devenir inefficace ?
• Comment éviter la dégénérescence ?

Dans votre modèle, si tous les joueurs jouent aléatoirement, que se passe-t-il ?
• Si tous jouent 0 ?
• Existe-t-il un prix “stable” vers lequel le système converge ?

Un script Python fonctionnel respectant les exigences ci-dessus.
• Contraintes techniques
o Implémenter un Arbre Binaire de Recherche (ABR).
o Gérer plusieurs joueurs pour une même clé.
o Permettre :
i. Insertion, parcours infixe, recherche du plus bas unique,
suppression conditionnelle, Simuler plusieurs manches.
o Produire une analyse argumentée.
o Interdictions :
i. Pas de tri Python pour résoudre le problème principal.
• Un rapport synthétique expliquant :
o La structure du projet.
o Les choix techniques : structure de donnée, algorithmes utilisés, …
o Les difficultés rencontrées et leur résolution.
