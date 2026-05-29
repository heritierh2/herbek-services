# Herbek Services — Site Web Vitrine Professionnel (Dark Mode)

Site web vitrine moderne et professionnel pour **Herbek Services**, construit avec Python et Streamlit. Thème sombre par défaut, design responsive et sidebar avec logo.

## 📁 Structure des fichiers

```
herbek-services/
├── app.py              # Application principale Streamlit
├── requirements.txt    # Dépendances Python
├── Procfile           # Commande de démarrage Render
├── runtime.txt        # Version Python (3.11.9)
├── assets/
│   ├── logo.jpg       # Logo officiel Herbek Services
│   └── logo\_alt.jpg   # Logo alternatif
└── README.md          # Ce fichier
```

## ✨ Fonctionnalités

* 🌙 Thème sombre (Dark Mode) par défaut — design professionnel et moderne
* 📱 Responsive (adapté PC et mobile)
* 🧭 Barre latérale de navigation avec logo officiel
* 🏠 Section Hero avec logo, slogan, mission et boutons d'action
* ℹ️ Section À propos avec valeurs de l'entreprise
* 🛠️ Section Services avec cartes visuelles (6 services)
* 🏆 Section Pourquoi nous choisir (3 atouts)
* 📝 Formulaire de contact avec affichage des messages soumis
* 💬 Bouton "Nous contacter sur WhatsApp" (https://wa.me/)
* 📞 Bouton "Nous appeler" (tel:)
* 📊 Barre de statistiques
* 📧 Coordonnées cliquables (email, téléphone, WhatsApp)

## 🚀 Déploiement sur Render (GRATUIT)

### Étape 1 : Préparer le dépôt GitHub

1. Créez un compte gratuit sur [github.com](https://github.com) si nécessaire.
2. Créez un nouveau dépôt (repository) nommé `herbek-services`.
3. Uploadez **tous les fichiers** de ce dossier dans le dépôt, y compris le dossier `assets/` avec votre logo.

### Étape 2 : Configurer Render

1. Créez un compte gratuit sur [render.com](https://render.com).
2. Cliquez sur **"New +"** puis **"Web Service"**.
3. Connectez votre compte GitHub et sélectionnez le dépôt `herbek-services`.
4. Configurez le service :

   * **Name** : `herbek-services`
   * **Runtime** : Python 3
   * **Build Command** : `pip install -r requirements.txt`
   * **Start Command** : `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false`
   * **Instance Type** : Free
5. Cliquez sur **"Create Web Service"**.
6. Attendez que le déploiement se termine (2-3 minutes).
7. Votre site sera accessible à l'adresse : `https://herbek-services.onrender.com`

## 🌐 Domaine personnalisé : herbek-services.com

Oui, il est tout à fait possible d'utiliser votre propre nom de domaine ! Voici la marche à suivre :

### Option 1 : Via Render (recommandé)

1. **Achetez le domaine** `herbek-services.com` chez un registraire (Namecheap, GoDaddy, OVH, etc.) — environ 8-12$/an.
2. Dans Render, allez dans les **Settings** de votre web service.
3. Cliquez sur **"Add Custom Domain"** et entrez `herbek-services.com`.
4. Render vous donnera des enregistrements DNS à configurer.
5. Chez votre registraire, ajoutez les enregistrements DNS fournis par Render :

   * Un enregistrement **CNAME** pointant vers `herbek-services.onrender.com`
   * Ou un enregistrement **A** avec l'IP fournie par Render
6. Attendez la propagation DNS (jusqu'à 48h, souvent quelques minutes).
7. Render active automatiquement le HTTPS (certificat SSL gratuit).

### Option 2 : Via Cloudflare (gratuit + CDN)

1. Achetez le domaine `herbek-services.com`.
2. Créez un compte gratuit sur [cloudflare.com](https://cloudflare.com).
3. Transférez les DNS du domaine vers Cloudflare.
4. Dans Cloudflare, ajoutez un enregistrement **CNAME** : `herbek-services.com` → `herbek-services.onrender.com`.
5. Activez le proxy Cloudflare (nuage orange) pour bénéficier du CDN gratuit et HTTPS.

> \*\*Coût\*\* : Le domaine coûte \~8-12$/an. L'hébergement Render + Cloudflare + HTTPS = \*\*0$\*\*.

## ⚙️ Personnalisation

Les constantes sont en haut du fichier `app.py` :

```python
WHATSAPP\_NUMBER = "243977777737"        # Numéro WhatsApp (format international sans +)
PHONE\_NUMBER = "+243977777737"          # Numéro de téléphone
EMAIL\_ADDRESS = "contact@herbek-services.com"  # Email de contact
```

Pour remplacer le logo, remplacez simplement le fichier `assets/logo.jpg` par votre propre image (même nom de fichier).

