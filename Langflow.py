from langflow.custom import Component
from langflow.io import Output, MessageTextInput
from langflow.schema import Data
import requests

class EnvoyerDonneesVerreTableComponent(Component):
    display_name = "Envoyer Données Verre à la Table"
    description = "Envoyer la composition détaillée du verre et les informations de référence du document au serveur Flask."
    icon = "table"

    inputs = [
        MessageTextInput(
            name="texte_extrait",
            display_name="Texte Extrait",
            info=(
                "Texte extrait contenant la référence du document et les informations sur la composition du verre."
            ),
            value=(
                "1. Type du document : Article scientifique\n"
                "2. Titre du document : Can a simple topological-constraints-based model predict the initial dissolution rate of borosilicate and aluminosilicate glasses?\n"
                "3. Référence : npj Materials Degradation (2020) 4:6 ; https://doi.org/10.1038/s41529-020-0111-4\n"
                "4. Premier Auteur : Stéphane Gin\n"
                "5. Nombre de types de verres : 3\n"
                "6. Verre_type1 : NBS14/18\n"
                "7. SiO₂(Verre_type1) : 67.8\n"
                "8. B₂O₃(Verre_type1) : 18.0\n"
                "9. Na₂O(Verre_type1) : 14.2\n"
                "10. Al₂O₃(Verre_type1) : 0\n"
                "11. Fines(Verre_type1) : 100-125 µm\n"
                "12. Densité(Verre_type1) : 2.451\n"
                "13. Homogénéité(Verre_type1) : Homogène\n"
                "14. % B(IV)(Verre_type1) : 66\n"
                "15. Irradié(Verre_type1) : N\n"
                "16. Caractéristiques si irradié(Verre_type1) : Non disponible\n"
                "17. Température(Verre_type1) : 90 °C\n"
                "18. Statique/dynamique(Verre_type1) : Statique\n"
                "19. Plage granulo si poudre(Verre_type1) : 100-125 µm\n"
                "20. Surface spécifique géométrique si poudre(Verre_type1) : 19.9 cm²\n"
                "21. Surface spécifique BET si poudre(Verre_type1) : Non disponible\n"
                "22. Qualité polissage si monolithe(Verre_type1) : Non disponible\n"
                "23. Masse verre(Verre_type1) : 0.095 g\n"
                "24. S(verre)(Verre_type1) : 19.9 cm²\n"
                "25. V(solution)(Verre_type1) : 0.231 L\n"
                "26. Débit solution(Verre_type1) : Non disponible\n"
                "27. pH initial (T amb)(Verre_type1) : Non disponible\n"
                "28. pH initial (T essai)(Verre_type1) : 9\n"
                "29. Compo solution(Verre_type1) : Eau déionisée, pH ajusté à 9 avec LiOH 1M\n"
                "30. Durée expérience(Verre_type1) : 5.5 h\n"
                "31. pH final (T amb)(Verre_type1) : Non disponible\n"
                "32. pH final (T essai)(Verre_type1) : 9.0\n"
                "33. Normalisation vitesse (Spm ou SBET)(Verre_type1) : Surface géométrique\n"
                "34. V₀(Si)(Verre_type1) : Non disponible\n"
                "35. r²(Si)(Verre_type1) : 0.999\n"
                "36. Ordonnée origine(Verre_type1) : 0.2\n"
                "37. V₀(B)(Verre_type1) : Non disponible\n"
                "38. Ordonnée origine(Verre_type1) : Non disponible\n"
                "39. V₀(Na)(Verre_type1) : Non disponible\n"
                "40. r²(Na)(Verre_type1) : Non disponible\n"
                "41. Ordonnée origine(Verre_type1) : Non disponible\n"
                "42. V₀(ΔM)(Verre_type1) : Non disponible\n"
                "43. Congruence(Verre_type1) : Congruente (presque)\n"
                "44. Verre_type2 : NSAC19\n"
                "45. SiO₂(Verre_type2) : 55.3\n"
                "46. B₂O₃(Verre_type2) : 0\n"
                "47. Na₂O(Verre_type2) : 19.0\n"
                "48. Al₂O₃(Verre_type2) : 9.9\n"
                "49. Fines(Verre_type2) : 20-40 µm\n"
                "50. Densité(Verre_type2) : 2.591\n"
                "51. Homogénéité(Verre_type2) : Homogène\n"
                "52. % B(IV)(Verre_type2) : Non disponible\n"
                "53. Irradié(Verre_type2) : N\n"
                "54. Caractéristiques si irradié(Verre_type2) : Non disponible\n"
                "55. Température(Verre_type2) : 90 °C\n"
                "56. Statique/dynamique(Verre_type2) : Statique\n"
                "57. Plage granulo si poudre(Verre_type2) : 20-40 µm\n"
                "58. Surface spécifique géométrique si poudre(Verre_type2) : 132 cm²\n"
                "59. Surface spécifique BET si poudre(Verre_type2) : Non disponible\n"
                "60. Qualité polissage si monolithe(Verre_type2) : Non disponible\n"
                "61. Masse verre(Verre_type2) : 0.165 g\n"
                "62. S(verre)(Verre_type2) : 132 cm²\n"
                "63. V(solution)(Verre_type2) : 0.490 L\n"
                "64. Débit solution(Verre_type2) : Non disponible\n"
                "65. pH initial (T amb)(Verre_type2) : Non disponible\n"
                "66. pH initial (T essai)(Verre_type2) : 9\n"
                "67. Compo solution(Verre_type2) : Eau déionisée, pH ajusté à 9 avec LiOH 1M\n"
                "68. Durée expérience(Verre_type2) : 4.1 h\n"
                "69. pH final (T amb)(Verre_type2) : Non disponible\n"
                "70. pH final (T essai)(Verre_type2) : 8.8\n"
                "71. Normalisation vitesse (Spm ou SBET)(Verre_type2) : Surface géométrique\n"
                "72. V₀(Si)(Verre_type2) : Non disponible\n"
                "73. r²(Si)(Verre_type2) : 0.998\n"
                "74. Ordonnée origine(Verre_type2) : 0.05\n"
                "75. V₀(B)(Verre_type2) : Non disponible\n"
                "76. Ordonnée origine(Verre_type2) : Non disponible\n"
                "77. V₀(Na)(Verre_type2) : Non disponible\n"
                "78. r²(Na)(Verre_type2) : Non disponible\n"
                "79. Ordonnée origine(Verre_type2) : Non disponible\n"
                "80. V₀(ΔM)(Verre_type2) : Non disponible\n"
                "81. Congruence(Verre_type2) : Incongruente\n"
                "82. Verre_type3 : NSA\n"
                "83. SiO₂(Verre_type3) : 75.0\n"
                "84. B₂O₃(Verre_type3) : 0\n"
                "85. Na₂O(Verre_type3) : 12.5\n"
                "86. Al₂O₃(Verre_type3) : 12.5\n"
                "87. Fines(Verre_type3) : 50-100 µm\n"
                "88. Densité(Verre_type3) : 2.340\n"
                "89. Homogénéité(Verre_type3) : Homogène\n"
                "90. % B(IV)(Verre_type3) : Non disponible\n"
                "91. Irradié(Verre_type3) : N\n"
                "92. Caractéristiques si irradié(Verre_type3) : Non disponible\n"
                "93. Température(Verre_type3) : 90 °C\n"
                "94. Statique/dynamique(Verre_type3) : Statique\n"
                "95. Plage granulo si poudre(Verre_type3) : 50-100 µm\n"
                "96. Surface spécifique géométrique si poudre(Verre_type3) : 88.3 cm²\n"
                "97. Surface spécifique BET si poudre(Verre_type3) : Non disponible\n"
                "98. Qualité polissage si monolithe(Verre_type3) : Non disponible\n"
                "99. Masse verre(Verre_type3) : 0.276 g\n"
                "100. S(verre)(Verre_type3) : 88.3 cm²\n"
                "101. V(solution)(Verre_type3) : 0.482 L\n"
                "102. Débit solution(Verre_type3) : Non disponible\n"
                "103. pH initial (T amb)(Verre_type3) : Non disponible\n"
                "104. pH initial (T essai)(Verre_type3) : 9\n"
                "105. Compo solution(Verre_type3) : Eau déionisée, pH ajusté à 9 avec LiOH 1M\n"
                "106. Durée expérience(Verre_type3) : 121 h\n"
                "107. pH final (T amb)(Verre_type3) : Non disponible\n"
                "108. pH final (T essai)(Verre_type3) : 8.9\n"
                "109. Normalisation vitesse (Spm ou SBET)(Verre_type3) : Surface géométrique\n"
                "110. V₀(Si)(Verre_type3) : Non disponible\n"
                "111. r²(Si)(Verre_type3) : 0.995\n"
                "112. Ordonnée origine(Verre_type3) : 0.02\n"
                "113. V₀(B)(Verre_type3) : Non disponible\n"
                "114. Ordonnée origine(Verre_type3) : Non disponible\n"
                "115. V₀(Na)(Verre_type3) : Non disponible\n"
                "116. r²(Na)(Verre_type3) : Non disponible\n"
                "117. Ordonnée origine(Verre_type3) : Non disponible\n"
                "118. V₀(ΔM)(Verre_type3) : Non disponible\n"
                "119. Congruence(Verre_type3) : Congruente (presque)\n"
            ),
            tool_mode=True,
        ),
    ]

    outputs = [
        Output(display_name="Réponse", name="sortie", method="construire_sortie"),
    ]

    def construire_sortie(self) -> Data:
        texte_extrait = self.texte_extrait
        print(f"Texte Extrait: {texte_extrait}")

        try:
            # Nettoyer et analyser le texte
            lignes = [ligne.strip() for ligne in texte_extrait.split("\n") if ligne.strip()]

            # Extraction des données générales
            type_doc = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("1. Type du document :")), None)
            titre = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("2. Titre du document :")), None)
            reference = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("3. Référence :")), None)
            premier_auteur = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("4. Premier Auteur :")), None)
            nombre_types_verres = int(next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("5. Nombre de types de verres :")), None))

            # Initialisation des données pour chaque type de verre
            donnees_verres = []

            for i in range(3):
                verre_data = {}
                verre_type_key = f"Verre_type{i+1}"
                verre_data["type"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{6 + i * 38}. {verre_type_key} :")), None)

                # Extraction des caractéristiques pour chaque type de verre
                verre_data["sio2"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{7 + i * 38}. SiO₂({verre_type_key}) :")), None)
                verre_data["b2o3"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{8 + i * 38}. B₂O₃({verre_type_key}) :")), None)
                verre_data["na2o"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{9 + i * 38}. Na₂O({verre_type_key}) :")), None)
                verre_data["al2o3"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{10 + i * 38}. Al₂O₃({verre_type_key}) :")), None)
                verre_data["fines"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{11 + i * 38}. Fines({verre_type_key}) :")), None)
                verre_data["densite"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{12 + i * 38}. Densité({verre_type_key}) :")), None)
                verre_data["homogeneite"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{13 + i * 38}. Homogénéité({verre_type_key}) :")), None)
                verre_data["b_iv_pourcent"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{14 + i * 38}. % B(IV)({verre_type_key}) :")), None)
                verre_data["irradie"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{15 + i * 38}. Irradié({verre_type_key}) :")), None)
                verre_data["caracteristiques_irradie"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{16 + i * 38}. Caractéristiques si irradié({verre_type_key}) :")), None)
                verre_data["temperature"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{17 + i * 38}. Température({verre_type_key}) :")), None)
                verre_data["statique_dynamique"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{18 + i * 38}. Statique/dynamique({verre_type_key}) :")), None)
                verre_data["plage_granulo"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{19 + i * 38}. Plage granulo si poudre({verre_type_key}) :")), None)
                verre_data["surface_specifique_geometrique"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{20 + i * 38}. Surface spécifique géométrique si poudre({verre_type_key}) :")), None)
                verre_data["surface_specifique_bet"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{21 + i * 38}. Surface spécifique BET si poudre({verre_type_key}) :")), None)
                verre_data["qualite_polissage"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{22 + i * 38}. Qualité polissage si monolithe({verre_type_key}) :")), None)
                verre_data["masse_verre"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{23 + i * 38}. Masse verre({verre_type_key}) :")), None)
                verre_data["s_verre"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{24 + i * 38}. S(verre)({verre_type_key}) :")), None)
                verre_data["v_solution"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{25 + i * 38}. V(solution)({verre_type_key}) :")), None)
                verre_data["debit_solution"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{26 + i * 38}. Débit solution({verre_type_key}) :")), None)
                verre_data["ph_initial"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{27 + i * 38}. pH initial (T amb)({verre_type_key}) :")), None)
                verre_data["ph_initial_test"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{28 + i * 38}. pH initial (T essai)({verre_type_key}) :")), None)
                verre_data["composition_solution"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{29 + i * 38}. Compo solution({verre_type_key}) :")), None)
                verre_data["duree_experience"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{30 + i * 38}. Durée expérience({verre_type_key}) :")), None)
                verre_data["ph_final_amb"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{31 + i * 38}. pH final (T amb)({verre_type_key}) :")), None)
                verre_data["ph_final_test"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{32 + i * 38}. pH final (T essai)({verre_type_key}) :")), None)
                verre_data["normalisation_vitesse"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{33 + i * 38}. Normalisation vitesse (Spm ou SBET)({verre_type_key}) :")), None)
                verre_data["v0_si"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{34 + i * 38}. V₀(Si)({verre_type_key}) :")), None)
                verre_data["r_carre_si"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{35 + i * 38}. r²(Si)({verre_type_key}) :")), None)
                verre_data["ordonnee_origine_si"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{38 + i * 38}. Ordonnée origine({verre_type_key}) :")), None)
                verre_data["v0_b"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{37 + i * 38}. V₀(B)({verre_type_key}) :")), None)
                verre_data["ordonnee_origine_b"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{38 + i * 38}. Ordonnée origine({verre_type_key}) :")), None)
                verre_data["v0_na"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{39 + i * 38}. V₀(Na)({verre_type_key}) :")), None)
                verre_data["r_carre_na"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{40 + i * 38}. r²(Na)({verre_type_key}) :")), None)
                verre_data["ordonnee_origine_na"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{41 + i * 38}. Ordonnée origine({verre_type_key}) :")), None)
                verre_data["v0_dm"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{42 + i * 38}. V₀(ΔM)({verre_type_key}) :")), None)
                verre_data["congruence"] = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{43 + i * 38}. Congruence({verre_type_key}) :")), None)

                donnees_verres.append(verre_data)

            # Préparer les données
            url = 'http://127.0.0.1:5001/add_glass_data'
            donnees = {
                "type": type_doc,
                "titre": titre,
                "reference": reference,
                "premier_auteur": premier_auteur,
                "nombre_types_verres": nombre_types_verres,
                "verres": donnees_verres
            }
            print(f"Envoi des données: {donnees}")

            reponse = requests.post(url, json=donnees)

            if reponse.status_code == 200:
                return Data(value="Données du verre ajoutées avec succès!")
            else:
                return Data(value=f"Erreur lors de l'ajout des données du verre. Code d'état: {reponse.status_code} - {reponse.text}")

        except Exception as e:
            return Data(value=f"Exception survenue: {str(e)}")
