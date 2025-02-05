import pandas as pd

def create_real_pred (y1, y2):
    "Prend 2 listes de prédictions et effectue les changements nécessaire pour obtenir les caractères souhaités"
    
    #Conversion des prédictions en ascii
    y1_asci = convert_ascii(y1)
    y2_asci = convert_ascii(y2)
    
    #Opération d'addition des deux images
    somme_ascii = [a + b for a, b in zip(y1_asci, y2_asci)]
    
    #Permet de gérer les valeurs asci > 122
    ascii = []
    for elem in somme_ascii:
        while elem > 122:
            elem -= 65
        ascii.append(elem)
        
    #converti les valeurs ascii par leur caractère correspondant
    real_pred = convert_asci_lettre(ascii)
    return real_pred

def convert_asci_lettre(y_pred):
    "Permet de convertir un vecteur de valeurs ascii [65-122] à une liste de caractères correspondant ascii"
    y_convert = [x - 65 for x in y_pred]
    y_preds = pd.DataFrame({'label' : y_convert})
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz"
    resultat = y_preds['label'].apply(lambda x: alphabet[x])
    return resultat

def convert_ascii(y_pred):
    "Converti une liste de prédictions [0-25] en liste correspondante ASCII"
    liste_ascii = [ord('A') + i  for i in y_pred]
    return liste_ascii


# au cas ou
def convert_lettre(y_pred):
    "Permet de convertir un vecteur de prédiction [0-25] à une liste [A-Z]"
    y_preds = pd.DataFrame({'label' : y_pred})
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    resultat = y_preds['label'].apply(lambda x: alphabet[x])
    return resultat