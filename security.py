from passlib.context import CryptContext

# Utiliser bcrypt comme schéma de hachage principal
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Vérifie si un mot de passe en clair correspond à un mot de passe haché."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Génère le hachage d'un mot de passe."""
    return pwd_context.hash(password)

