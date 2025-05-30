from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importer les fonctions de connexion DB
from database import connect_to_mongo, close_mongo_connection
# Importer les routers
from routers import product_router, order_router, user_router, message_router

# Créer l'instance de l'application FastAPI
app = FastAPI(
    title="Agent Commercial WhatsApp - Backend",
    description="API pour gérer les produits, commandes, utilisateurs et messages pour l'agent WhatsApp.",
    version="0.1.0"
)

# Configuration CORS
# Liste des origines autorisées (le frontend en développement)
# ATTENTION: Pour la production, il faudra restreindre ces origines !
origins = [
    "http://localhost:3000", # Origine typique pour Next.js en développement
    "http://localhost",      # Parfois utile
    # Ajoutez ici l'URL de votre frontend déployé si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Autorise les origines spécifiques
    allow_credentials=True,
    allow_methods=["*"], # Autorise toutes les méthodes (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Autorise tous les headers
)


# Événements de démarrage et d'arrêt pour gérer la connexion DB
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Inclure les routers dans l'application
app.include_router(product_router.router)
app.include_router(order_router.router)
app.include_router(user_router.router)
app.include_router(message_router.router)

# Route racine simple pour vérifier que l'API fonctionne
@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur l'API de l'Agent Commercial WhatsApp"}

# Point d'entrée pour Uvicorn (si exécuté directement, bien que uvicorn main:app soit préféré)
if __name__ == "__main__":
    import uvicorn
    # Note: Le host 0.0.0.0 est important pour l'accessibilité dans Docker/environnements conteneurisés
    # Le port 8000 est un exemple standard
    # Le reload=True est utile pour le développement
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

