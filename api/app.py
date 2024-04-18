from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': 'root',
    'database': 'mydb'
}

@app.route('/admin/addresses', methods=['POST'])
def create_address():
    data = request.get_json()
    numero_rue = data['numero_rue']
    nom_rue = data['nom_rue']
    ville = data['ville']
    code_postal = data['code_postal']

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO Adresse (numero_rue, nom_rue, ville, code_postal) VALUES (%s, %s, %s, %s)"
        values = (numero_rue, nom_rue, ville, code_postal)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Adresse créée avec succès"}), 201

    except mysql.connector.Error as error:
        return jsonify({"error": str(error)}), 500

@app.route('/users/addresses', methods=['GET'])
def get_addresses():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT * FROM Adresse"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        addresses = []
        for row in results:
            address = {
                'id': row[0],
                'numero_rue': row[1],
                'nom_rue': row[2],
                'ville': row[3],
                'code_postal': row[4]
            }
            addresses.append(address)

        return jsonify({"addresses": addresses}), 200

    except mysql.connector.Error as error:
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)