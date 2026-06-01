import streamlit as st
import os

# Configuration de la page
st.set_page_config(
    page_title="Herbek Services",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS PERSONNALISÉ SÉCURISÉ ---
st.markdown("""
<style>
    /* Arrière-plan global */
    .stApp {
        background-color: #0F111A;
    }
    h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    p, li, label, span {
        color: #A0A5B5 !important;
    }
    
    /* Style de la Sidebar fixe */
    [data-testid="stSidebar"] {
        background-color: #161925;
        border-right: 1px solid #24293E;
    }
    
    /* Cartes des Services */
    .service-card {
        background: #1E2235;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #2B314D;
        margin-bottom: 20px;
        height: 100%;
    }
    .service-icon {
        font-size: 35px;
        margin-bottom: 15px;
    }
    
    /* Grille de contact direct */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-bottom: 35px;
        margin-top: 20px;
    }
    .contact-card {
        background: #1E2235;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2B314D;
        text-align: center;
        text-decoration: none;
        transition: transform 0.2s;
        display: block;
    }
    .contact-card:hover {
        transform: translateY(-5px);
    }
    .icon-whatsapp { border-top: 4px solid #25D366; }
    .icon-phone { border-top: 4px solid #007BFF; }
    .icon-email { border-top: 4px solid #FFC107; }
    
    /* Séparateur de sections déroulantes */
    .section-container {
        padding: 60px 0;
        border-bottom: 1px solid #24293E;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR FIXE (MENU DE NAVIGATION INFORMATIF) ---
with st.sidebar:
    logo_path = "assets/logo.jpg"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.title("Herbek Services")
    st.caption("EXCELLENCE AU SERVICE DE VOTRE RÉUSSITE")
    st.markdown("---")
    
    st.markdown("### 🧭 Navigation Rapide")
    st.markdown("""
    <span style="color: #25D366; font-weight: bold;">Défilement Continu Actif</span>  
    Faites défiler la page centrale pour explorer l'ensemble de nos rubriques et offres.
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.info("Utilisez l'ascenseur de droite pour naviguer de l'Accueil jusqu'au Formulaire de contact.")

# --- CONTENU UNIQUE DÉROULANT (ONE-PAGE ARCHITECTURE) ---

# 1. SECTION : ACCUEIL
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.subheader("Votre partenaire de confiance")
st.title("Herbek Services")
st.markdown("#### *L'excellence au service de votre réussite*")
st.write("Nous fournissons des solutions de service professionnelles, fiables et parfaitement adaptées à vos exigences pour structurer, protéger et propulser vos projets.")
st.markdown('</div>', unsafe_allow_html=True)

# 2. SECTION : À PROPOS DE NOUS
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.title("🤝 À propos de nous")
st.write("Herbek Services est une structure d'élite et polyvalente, engagée activement dans le développement opérationnel, l'appui entrepreneurial et la gestion environnementale.")
st.write("Notre action s'articule autour de solutions concrètes pour assainir vos espaces, encadrer les talents émergents et maximiser l'efficacité de vos initiatives professionnelles.")

st.markdown("#### 🎯 Nos Piliers Majeurs d'Intervention :")
st.markdown("""
- **Assainissement & Environnement :** Prestations rigoureuses de salubrité et de nettoyage pour garantir des cadres de vie et professionnels sains.
- **Prestations de Services Diverses :** Gestion de vos besoins généraux, logistiques et administratifs courants avec une réactivité totale.
- **Soutien aux Projets des Jeunes Entrepreneurs :** Mentorat technique, aide à la modélisation commerciale et orientation stratégique.
- **Organisation de Salons de l'Emploi :** Conception de plateformes d'échange dynamiques pour interconnecter recruteurs et profils qualifiés.
""")
st.markdown('</div>', unsafe_allow_html=True)

# 3. SECTION : NOS SERVICES
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.title("💼 Nos Services Spécialisés")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">✨</div>
        <h3>Assainissement & Salubrité</h3>
        <p>Interventions complètes de nettoyage, de désinfection et de maintien de la propreté pour les infrastructures privées, commerciales et industrielles.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🚀</div>
        <h3>Soutien aux Jeunes Entrepreneurs</h3>
        <p>Accompagnement critique à la création d'entreprise : structuration du modèle économique, outils de pilotage et validation de plans d'action.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🛠️</div>
        <h3>Prestations de Services</h3>
        <p>Assistance externalisée pour la gestion de vos démarches administratives, logistiques et contractuelles en toute confidentialité.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🤝</div>
        <h3>Salons de l'Emploi & Recrutement</h3>
        <p>Planification et pilotage d'événements professionnels de l'emploi pour optimiser le maillage entre entreprises et chercheurs d'opportunités.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. SECTION : CONTACTEZ-NOUS (RÉPARATION DÉFINITIVE)
st.markdown('<div class="section-container" style="border-bottom: none;">', unsafe_allow_html=True)
st.title("✉️ Contactez-nous")
st.write("Une question, un besoin ou un projet ? Utilisez l'un de nos accès directs ou transmettez-nous votre demande via le formulaire sécurisé ci-dessous.")

# 📱 BOUTONS DE CONTACT DIRECT (WhatsApp, Appel, Mail)
st.markdown("""
<div class="contact-grid">
    <a href="https://wa.me/243977777737" target="_blank" class="contact-card icon-whatsapp">
        <h3 style="color:#25D366 !important; margin:0;">🟢 WhatsApp Direct</h3>
        <p style="margin:8px 0 0 0; font-size:14px;">Lancez une discussion instantanée</p>
    </a>
    <a href="tel:+243977777737" class="contact-card icon-phone">
        <h3 style="color:#007BFF !important; margin:0;">🔵 Appel Normal</h3>
        <p style="margin:8px 0 0 0; font-size:14px;">+243 977 777 737</p>
    </a>
    <a href="mailto:contact@herbek-services.com" class="contact-card icon-email">
        <h3 style="color:#FFC107 !important; margin:0;">🟡 E-mail de Service</h3>
        <p style="margin:8px 0 0 0; font-size:14px;">contact@herbek-services.com</p>
    </a>
</div>
""", unsafe_allow_html=True)

# 📝 FORMULAIRE SÉCURISÉ FORM_SUBMIT INTERPRÉTÉ
form_html = """
<form action="https://formsubmit.co/contact@herbek-services.com" method="POST" style="background:#1E2235; padding:35px; border-radius:12px; border:1px solid #2B314D; max-width:900px; margin: 0 auto;">
    <input type="hidden" name="_subject" value="Nouveau message - Site Herbek Services">
    <input type="hidden" name="_captcha" value="false">
    
    <div style="margin-bottom:20px;">
        <label style="color:white; display:block; margin-bottom:8px; font-weight:bold;">Nom complet :</label>
        <input type="text" name="name" required style="width:100%; padding:12px; border-radius:6px; border:1px solid #2B314D; background:#0F111A; color:white; font-size:15px;">
    </div>
    
    <div style="margin-bottom:20px;">
        <label style="color:white; display:block; margin-bottom:8px; font-weight:bold;">Adresse E-mail :</label>
        <input type="email" name="email" required style="width:100%; padding:12px; border-radius:6px; border:1px solid #2B314D; background:#0F111A; color:white; font-size:15px;">
    </div>
    
    <div style="margin-bottom:25px;">
        <label style="color:white; display:block; margin-bottom:8px; font-weight:bold;">Votre Message :</label>
        <textarea name="message" rows="5" required style="width:100%; padding:12px; border-radius:6px; border:1px solid #2B314D; background:#0F111A; color:white; font-size:15px; resize:vertical;"></textarea>
    </div>
    
    <div style="text-align: center;">
        <button type="submit" style="background:#007BFF; color:white; border:none; padding:14px 40px; border-radius:6px; font-weight:bold; cursor:pointer; font-size:16px; transition: background 0.3s;">🚀 Envoyer mon message</button>
    </div>
</form>
"""
st.markdown(form_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
