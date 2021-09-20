import math

annee = 2021
mois = 9
jour = 20

joursDateChoisie = 1461 * annee // 4
joursDateFixe = 719484

totalJours = (joursDateChoisie - joursDateFixe) + math.ceil((306 * (mois - 3) - 5) / 10) + jour

print(totalJours, "jours se sont écoulés depuis le 1 janvier 1970")