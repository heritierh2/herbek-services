import streamlit as st
import os

# Configuration de la page
st.set_page_config(
    page_title="Herbek Services",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé pour soigner l'interface
st.markdown("""
<style>
    /* Arrière-plan global et polices */
    .stApp {
        background-color: #0F111A;
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    p, li, label {
        color: #A0A5B5 !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161925;
        border-right: 1px solid #24293E;
    }
    
    /* Cartes des services améliorées */
    .service-card {
        background: #1E2235;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #2B314D;
        margin-bottom: 20px;
        height: 100%;
        transition: transform 0.3s ease;
    }
    .service-card:hover {
        transform: translateY(-5px);
        border-color: #007BFF;
    }
    .service-icon {
        font-size: 35px;
        margin-bottom: 15px;
    }
    
    /* Boutons personnalisés */
    .btn-whatsapp {
        background-color: #25D366 !important;
        color: white !important;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin-right: 10px;
        text-align: center;
    }
    .btn-tel {
        background-color: #007BFF !important;
        color: white !important;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }
</style>
""", unsafe_index=True)

# --- SIDEBAR & LOGO ---
with st.sidebar:
    logo_path = "assets/logo.jpg"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        # En attendant que l'image soit bien placée sur GitHub
        st.title("Herbek Services")
    
    st.caption("EXCELLENCE AU SERVICE DE VOTRE RÉUSSITE")
    st.markdown("---")
    
    # Navigation interne fluide
    menu = st.radio("Navigation", ["Accueil", "À propos", "Nos Services", "Pourquoi nous", "Contact"])

# --- CONTENU PRINCIPAL ---

if menu == "Accueil":
    st.subheader("Votre partenaire de confiance")
    st.title("Herbek Services")
    st.markdown("#### *L'excellence au service de votre réussite*")
    st.write("Fournir des solutions de service professionnelles, fiables et adaptées à vos besoins spécifiques pour propulser vos projets vers de nouveaux sommets.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Boutons d'action directs et fonctionnels
    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        st.markdown('<a href="https://wa.me/243977777737" target="_blank" class="btn-whatsapp">💬 WhatsApp</a>', unsafe_allow_html=True)
    with col_btn2:
        st.markdown('<a href="tel:+243977777737" class="btn-tel">📞 Nous appeler</a>', unsafe_allow_html=True)

elif menu == "À propos":
    st.title("À propos de nous")
    st.write("Herbek Services est une structure dédiée à l'accompagnement et au développement des entreprises et des particuliers. Nous combinons expertise locale et standards professionnels pour offrir des résultats concrets.")

elif menu == "Nos Services":
    st.title("Nos Services de Pointe")
    st.write("Découvrez les expertises que nous mettons en avant pour votre croissance :")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">📋</div>
            <h3>Conseil & Accompagnement</h3>
            <p>Un accompagnement stratégique personnalisé pour vous guider dans vos projets professionnels et entrepreneuriaux. Nous analysons votre situation, identifions les opportunités et vous proposons un plan d'action concret.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">📊</div>
            <h3>Gestion & Administration</h3>
            <p>Services de gestion administrative, comptable et organisationnelle pour optimiser le fonctionnement de votre entreprise et vous libérer du temps précieux.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">💻</div>
            <h3>Solutions Numériques</h3>
            <p>Création de sites web, solutions digitales et transformation numérique pour propulser votre présence en ligne. Nous concevons des outils adaptés à votre secteur d'activité.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🎓</div>
            <h3>Formation & Capacitation</h3>
            <p>Programmes de formation adaptés pour développer vos compétences et celles de vos collaborateurs via des modules pratiques, interactifs et directement applicables.</p>
        </div>
        """, unsafe_allow_html=True)

elif menu == "Pourquoi nous":
    st.title("Pourquoi choisir Herbek Services ?")
    st.write("- **Professionnalisme :** Une équipe rigoureuse à votre écoute.\n- **Solutions sur mesure :** Chaque client bénéficie d'une approche unique.\n- **Disponibilité et réactivité :** Nous répondons rapidement à vos urgences.")

elif menu == "Contact":
    st.title("Contactez-nous")
    st.write("Une question ou un projet ? Remplissez ce formulaire pour recevoir une réponse rapide par e-mail.")
    
    # Configuration du formulaire pour envoyer un VRAI e-mail vers contact@herbek-services.com
    # Utilisation du service sécurisé et gratuit FormSubmit
    form_html = """
    <form action="https://formsubmit.co/contact@herbek-services.com" method="POST" style="background:#1E2235; padding:30px; border-radius:12px; border:1px solid #2B314D;">
        <input type="hidden" name="_subject" value="Nouveau message de votre site web Herbek Services !">
        <input type="hidden" name="_captcha" value="false">
        
        <div style="margin-bottom:15px;">
            <label style="color:white; display:block; margin-bottom:5px;">Votre Nom complet :</label>
            <input type="text" name="name" required style="width:100%; padding:10px; border-radius:5px; border:1px solid #2B314D; background:#0F111A; color:white;">
        </div>
        <div style="margin-bottom:15px;">
            <label style="color:white; display:block; margin-bottom:5px;">Votre Adresse E-mail :</label>
            <input type="email" name="email" required style="width:100%; padding:10px; border-radius:5px; border:1px solid #2B314D; background:#0F111A; color:white;">
        </div>
        <div style="margin-bottom:15px;">
            <label style="color:white; display:block; margin-bottom:5px;">Votre Message :</label>
            <textarea name="message" rows="5" required style="width:100%; padding:10px; border-radius:5px; border:1px solid #2B314D; background:#0F111A; color:white;"></textarea>
        </div>
        <button type="submit" style="background:#007BFF; color:white; border:none; padding:12px 25px; border-radius:5px; font-weight:bold; cursor:pointer;">Envoyer le message</button>
    </form>
    """
    st.markdown(form_html, unsafe_allow_html=True)
