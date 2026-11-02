from compte_bancaire import CompteBancaire



if __name__ == "__main__":

    compte = CompteBancaire("Ali", 1000)

    compte.deposer(200)
    compte.retirer(150)

    print(compte)

    print("Solde accessible (lecture) :", compte.solde)

    # Tentative de modification directe
    compte.solde = 500