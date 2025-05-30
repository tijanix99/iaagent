import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

if not MONGO_DETAILS:
    raise ValueError("La variable d'environnement MONGO_DETAILS n'est pas définie. Assurez-vous qu'elle est dans le fichier .env")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Sélectionner la base de données. Vous pouvez changer 'whatsapp_agent_db' si nécessaire.
database = client.whatsapp_agent_db

# Optionnel : Fonctions pour gérer la connexion/déconnexion dans FastAPI
async def connect_to_mongo():
    # La connexion est établie lors de la création du client, mais on peut ajouter un ping pour vérifier
    try:
        await client.admin.command('ping')
        print("Connexion à MongoDB réussie !")
    except Exception as e:
        print(f"Erreur de connexion à MongoDB: {e}")

async def close_mongo_connection():
    client.close()
    print("Connexion à MongoDB fermée.")

# Fonction pour obtenir l'objet de la base de données (pourrait être utilisée par les routers)
def get_database():
    return database

