chemin_fichier_original = input("entrez le chemin de fichier original:")
chemin_fichier_copie = input("entrez le chemin de fichier copie:")
fichier_en_lecture = open(chemin_fichier_original,'rb')
suite_doctes = []
print('#'*20)
for block_octes in fichier_en_lecture :
    suite_doctes.append(block_octes)

fichier_en_ecriture = open(chemin_fichier_copie,'wb')
for octes in suite_doctes:
    fichier_en_ecriture.write(octes)

fichier_en_ecriture.close()
