CREATE TABLE IF NOT EXISTS Adresse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_rue VARCHAR(10),
    nom_rue VARCHAR(100),
    ville VARCHAR(100),
    code_postal VARCHAR(10)
);