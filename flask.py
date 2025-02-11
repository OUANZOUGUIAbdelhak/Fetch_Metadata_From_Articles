from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
import os
import subprocess
import requests
import pandas as pd
from io import BytesIO
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
socketio = SocketIO(app)

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

# Modèle de base de données
class GlassData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_document = db.Column(db.String(100), nullable=True)
    titre = db.Column(db.String(200), nullable=True)
    reference = db.Column(db.String(200), nullable=True)
    premier_auteur = db.Column(db.String(100), nullable=True)
    nombre_types_verres = db.Column(db.Integer, nullable=True)
    glass_types = db.relationship('GlassType', backref='glass_data', lazy=True)

class GlassType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    glass_data_id = db.Column(db.Integer, db.ForeignKey('glass_data.id'), nullable=False)
    type_verre = db.Column(db.String(100), nullable=True)
    sio2 = db.Column(db.String(100), nullable=True)
    b2o3 = db.Column(db.String(100), nullable=True)
    na2o = db.Column(db.String(100), nullable=True)
    al2o3 = db.Column(db.String(100), nullable=True)
    fines = db.Column(db.String(100), nullable=True)
    densite = db.Column(db.String(100), nullable=True)
    homogeneite = db.Column(db.String(100), nullable=True)
    b_iv_pourcent = db.Column(db.String(100), nullable=True)
    irradie = db.Column(db.String(100), nullable=True)
    caracteristiques_irradie = db.Column(db.String(100), nullable=True)
    temperature = db.Column(db.String(100), nullable=True)
    statique_dynamique = db.Column(db.String(100), nullable=True)
    plage_granulo = db.Column(db.String(100), nullable=True)
    surface_specifique_geometrique = db.Column(db.String(100), nullable=True)
    surface_specifique_bet = db.Column(db.String(100), nullable=True)
    qualite_polissage = db.Column(db.String(100), nullable=True)
    masse_verre = db.Column(db.String(100), nullable=True)
    s_verre = db.Column(db.String(100), nullable=True)
    v_solution = db.Column(db.String(100), nullable=True)
    debit_solution = db.Column(db.String(100), nullable=True)
    ph_initial = db.Column(db.String(100), nullable=True)
    ph_final = db.Column(db.String(100), nullable=True)
    composition_solution = db.Column(db.String(100), nullable=True)
    duree_experience = db.Column(db.String(100), nullable=True)
    ph_final_amb = db.Column(db.String(100), nullable=True)
    ph_final_test = db.Column(db.String(100), nullable=True)
    normalisation_vitesse = db.Column(db.String(100), nullable=True)
    v0_si = db.Column(db.String(100), nullable=True)
    r_carre_si = db.Column(db.String(100), nullable=True)
    ordonnee_origine_si = db.Column(db.String(100), nullable=True)
    v0_b = db.Column(db.String(100), nullable=True)
    ordonnee_origine_b = db.Column(db.String(100), nullable=True)
    v0_na = db.Column(db.String(100), nullable=True)
    r_carre_na = db.Column(db.String(100), nullable=True)
    ordonnee_origine_na = db.Column(db.String(100), nullable=True)
    v0_dm = db.Column(db.String(100), nullable=True)
    congruence = db.Column(db.String(100), nullable=True)

# Créer la base de données si elle n'existe pas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    glass_data = GlassData.query.all()
    return render_template('index.html', glass_data=glass_data)

@app.route('/add_glass_data', methods=['POST'])
def add_glass_data():
    data = request.get_json()
    try:
        # Log des données reçues
        print(f"Données reçues: {data}")

        # Créer l'entrée principale dans GlassData
        new_entry = GlassData(
            type_document=data.get('type'),
            titre=data.get('titre'),
            reference=data.get('reference'),
            premier_auteur=data.get('premier_auteur'),
            nombre_types_verres=data.get('nombre_types_verres')
        )
        db.session.add(new_entry)
        db.session.commit()

        # Ajouter les types de verre
        for verre in data.get('verres', []):
            # Log des données de chaque type de verre
            #print(f"Données du verre: {verre}")

            glass_type_entry = GlassType(
                glass_data_id=new_entry.id,
                type_verre=verre.get('type'),
                sio2=verre.get('sio2'),
                b2o3=verre.get('b2o3'),
                na2o=verre.get('na2o'),
                al2o3=verre.get('al2o3'),
                fines=verre.get('fines'),
                densite=verre.get('densite'),
                homogeneite=verre.get('homogeneite'),
                b_iv_pourcent=verre.get('b_iv_pourcent'),
                irradie=verre.get('irradie'),
                caracteristiques_irradie=verre.get('caracteristiques_irradie'),
                temperature=verre.get('temperature'),
                statique_dynamique=verre.get('statique_dynamique'),
                plage_granulo=verre.get('plage_granulo'),
                surface_specifique_geometrique=verre.get('surface_specifique_geometrique'),
                surface_specifique_bet=verre.get('surface_specifique_bet'),
                qualite_polissage=verre.get('qualite_polissage'),
                masse_verre=verre.get('masse_verre'),
                s_verre=verre.get('s_verre'),
                v_solution=verre.get('v_solution'),
                debit_solution=verre.get('debit_solution'),
                ph_initial=verre.get('ph_initial'),
                ph_final=verre.get('ph_final_test'),
                composition_solution=verre.get('composition_solution'),
                duree_experience=verre.get('duree_experience'),
                ph_final_amb=verre.get('ph_final_amb'),
                ph_final_test=verre.get('ph_final_test'),
                normalisation_vitesse=verre.get('normalisation_vitesse'),
                v0_si=verre.get('v0_si'),
                r_carre_si=verre.get('r_carre_si'),
                ordonnee_origine_si=verre.get('ordonnee_origine_si'),
                v0_b=verre.get('v0_b'),
                ordonnee_origine_b=verre.get('ordonnee_origine_b'),
                v0_na=verre.get('v0_na'),
                r_carre_na=verre.get('r_carre_na'),
                ordonnee_origine_na=verre.get('ordonnee_origine_na'),
                v0_dm=verre.get('v0_dm'),
                congruence=verre.get('congruence')
            )
            db.session.add(glass_type_entry)
        db.session.commit()

        return "Données sur le verre ajoutées avec succès !", 200

    except Exception as e:
        return f"Erreur : {str(e)}", 500


@app.route('/delete_document_reference/<int:id>', methods=['POST'])
def delete_document_reference(id):
    glass_data = GlassData.query.get(id)
    db.session.delete(glass_data)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Call Docling script
        docling_script_path = '/home/intra.cea.fr/ao280403/Bureau/Docling_Langflow_flask/DLF/docling_script.py'

        if not os.path.exists(docling_script_path):
            return f"Docling script not found at: {docling_script_path}", 500

        process = subprocess.Popen(
            ["python", docling_script_path, filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Read the output and send progress updates
        total_pages = 0
        for line in process.stdout:
            logging.info(line.strip())
            if "Page" in line and "/" in line:
                parts = line.split(" ")
                current_page = int(parts[1].split("/")[0])
                total_pages = int(parts[1].split("/")[1])
                percent_complete = (current_page / total_pages) * 100
                socketio.emit('progress', {'percent_complete': percent_complete})
            elif "Table" in line or "Picture" in line:
                socketio.emit('progress', {'message': line.strip()})

        process.wait()

        # Construct the expected Markdown file path
        doc_filename = os.path.splitext(os.path.basename(filepath))[0]
        md_filepath = os.path.join('scratch', f"{doc_filename}-md", f"{doc_filename}-plain.md")

        # Verify the Markdown file exists
        if not os.path.exists(md_filepath):
            return f"Markdown file not found at: {md_filepath}", 500

        # Read the Markdown file
        with open(md_filepath, 'r') as md_file:
            md_content = md_file.read()

        # Call Langflow API
        response = requests.post(
            "http://127.0.0.1:7860/api/v1/run/a7e4b6a1-d444-487c-bec7-a954e6d42725?stream=false",
            json={
                "input_value": md_content,
                "output_type": "chat",
                "input_type": "text",
                "tweaks": {
                    "Prompt-F8PHW": {},
                    "ParseData-ggwft": {},
                    "ChatOutput-Uou7S": {},
                    "CustomComponent-OsOFR": {},
                    "File-yvKBt": {},
                    "TextInput-4LsXJ": {},
                    "GoogleGenerativeAIModel-Efdt7": {}
                }
            }
        )

        # Return a JSON response to update the frontend
        return jsonify({"message": "File processed successfully", "data": response.json()})

@app.route('/download_excel', methods=['GET'])
def download_excel():
    glass_data = GlassData.query.all()
    data = []
    for entry in glass_data:
        for glass_type in entry.glass_types:
            data.append({
                "Type": entry.type_document,
                "Titre": entry.titre,
                "Référence": entry.reference,
                "Premier Auteur": entry.premier_auteur,
                "Nombre de types de verres": entry.nombre_types_verres,
                "Type de verre": glass_type.type_verre,
                "SiO₂": glass_type.sio2,
                "B₂O₃": glass_type.b2o3,
                "Na₂O": glass_type.na2o,
                "Al₂O₃": glass_type.al2o3,
                "Fines": glass_type.fines,
                "Densité": glass_type.densite,
                "Homogénéité": glass_type.homogeneite,
                "% B(IV)": glass_type.b_iv_pourcent,
                "Irradié": glass_type.irradie,
                "Caractéristiques si irradié": glass_type.caracteristiques_irradie,
                "Température": glass_type.temperature,
                "Statique/dynamique": glass_type.statique_dynamique,
                "Plage granulo si poudre": glass_type.plage_granulo,
                "Surface spécifique géométrique si poudre": glass_type.surface_specifique_geometrique,
                "Surface spécifique BET si poudre": glass_type.surface_specifique_bet,
                "Qualité polissage si monolithe": glass_type.qualite_polissage,
                "Masse verre": glass_type.masse_verre,
                "S(verre)": glass_type.s_verre,
                "V(solution)": glass_type.v_solution,
                "Débit solution": glass_type.debit_solution,
                "pH initial (T amb)": glass_type.ph_initial,
                "pH final (T essai)": glass_type.ph_final,
                "Compo solution": glass_type.composition_solution,
                "Durée expérience": glass_type.duree_experience,
                "pH final (T amb)": glass_type.ph_final_amb,
                "pH final (T essai)": glass_type.ph_final_test,
                "Normalisation vitesse (Spm ou SBET)": glass_type.normalisation_vitesse,
                "V₀(Si)": glass_type.v0_si,
                "r²": glass_type.r_carre_si,
                "Ordonnée origine": glass_type.ordonnee_origine_si,
                "V₀(B)": glass_type.v0_b,
                "Ordonnée origine": glass_type.ordonnee_origine_b,
                "V₀(Na)": glass_type.v0_na,
                "r²": glass_type.r_carre_na,
                "Ordonnée origine": glass_type.ordonnee_origine_na,
                "V₀(ΔM)": glass_type.v0_dm,
                "Congruence": glass_type.congruence
            })

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Glass Data')
    output.seek(0)

    return send_file(output, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', as_attachment=True, download_name='glass_data.xlsx')

@socketio.on('connect')
def handle_connect():
    emit('status', {'msg': 'Connecté'})

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    socketio.run(app, debug=True, port=5001)
