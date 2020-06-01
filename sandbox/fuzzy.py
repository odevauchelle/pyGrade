
from fuzzywuzzy import process

page = '''

  MENU Libération

      CONNEXION  ABONNEMENT

LES DOSSIERS DU FIL VERT ABONNÉS
La sobriété, une idée en pleine croissance

 Les dossiers du Fil vert #4 : la sobriété
LES DOSSIERS DU FIL VERT
Vers la sobriété: déconsommer sans modération

AU FIL DE LA JOURNÉE
Mort de George Floyd : nouvelle nuit de manifestations sous tension aux Etats-Unis

 Devant le Parlement britannique, à Londres, en octobre 2019.
COULISSES DE BRUXELLES
Et si le Royaume-Uni était toujours membre de l'Union européenne ?

FÉMINICIDES
Elle avait 84 ans, son mari l'a tuée à coup de crosse de fusil après cinquante ans de mariage

 A Paris le 23 avril.
JOURNAL D'ÉPIDÉMIE
Didier Raoult, général Boulanger de la médecine

ARCHIVES
Christo, l’art de s’emballer

 Libé du 30 mai 2020
Pour lire le journal en numérique
Souscrivez à l'offre 100% numérique:
1 € le 1er mois sans engagement
'''

names = ['Raoult', 'boulanger', 'Boulangère', 'Floyd', 'totolarder' ]

print( process.extract( page, names, limit = 2 ) )
