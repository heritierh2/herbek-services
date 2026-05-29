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
    [data-testid="stSidebar"] {
        background-color: #161925;
        border-right: 1px solid #24293E;
    }
    /* Style des boutons radio du menu */
    div.row-widget.stRadio > div{
        background-color: #1E2235;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #2B314D;
    }
    div.row-widget.stRadio th, div.row-widget.stRadio label {
        color: white !important;
    }
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
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 35px;
    }
    .contact-card {
        background: #1E2235;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2B314D;
        text-align: center;
        text-decoration: none;
        transition: transform 0.2s;
    }
    .contact-card:hover {
        transform: translateY(-5px);
    }
    .icon-whatsapp { border-left: 4px solid #25D366; }
    .icon-phone { border-left: 4px solid #007BFF; }
    .icon-email { border-left: 4px solid #FFC107; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (MENU DE NAVIGATION) ---
with st.sidebar:
    logo_path = "assets/logo.jpg"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.title("Herbek Services")
    st.caption("EXCELLENCE AU SERVICE DE VOTRE RÉUSSITE")
    st.markdown("---")
    
    st.markdown("### 🧭 Navigation")
    menu = st.radio(
        "Aller vers :",
        ["🏠 Accueil", "🤝 À propos de nous", "💼 Nos Services", "✉️ Contact"]
    )

# --- CONTENU DYNAMIQUE SELON LE MENU ---

# 1. ACCUEIL
if menu == "🏠 Accueil":
    st.subheader("Votre partenaire de confiance")
    st.title("Herbek Services")
    st.markdown("#### *L'excellence au service de votre réussite*")
    st.write("Fournir des solutions de service professionnelles, fiables et adaptées à vos besoins spécifiques pour propulser vos projets vers de nouveaux sommets.")
    
    # Boutons d'accès rapide sur l'accueil
    st.markdown("""
    <div style="display: flex; gap: 15px; margin-top: 25px;">
        <a href="https://wa.me/243977777737" target="_blank" style="background-color: #25D366; color: white; font-weight: bold; padding: 12px 24px; border-radius: 8px; text-decoration: none;">💬 WhatsApp Direct</a>
        <a href="tel:+243977777737" style="background-color: #007BFF; color: white; font-weight: bold; padding: 12px 24px; border-radius: 8px; text-decoration: none;">📞 Nous appeler</a>
    </div>
    """, unsafe_allow_html=True)

# 2. À PROPOS DE NOUS
elif menu == "🤝 À propos de nous":
    st.title("🤝 À propos de nous")
    st.write("Herbek Services est une structure dynamique et polyvalente dédiée au développement socio-économique et à l'accompagnement opérationnel des professionnels et des particuliers.")
    
    st.markdown("### 🎯 Nos Piliers d'Intervention")
    st.markdown("""
    - **Assainissement & Environnement :** Nous proposons des prestations complètes pour garantir des espaces de vie et de travail sains, propres et durables.
    - **Prestations de Services Diverses :** Un support logistique et opérationnel sur mesure pour répondre aux défis quotidiens de votre structure.
    - **Soutien aux Jeunes Entrepreneurs :** Accompagnement stratégique, orientation et mentorat pour transformer les idées innovantes des jeunes en entreprises viables.
    - **Organisation de Salons de l'Emploi :** Création de plateformes de rencontre d'élite entre recruteurs et talents pour dynamiser le marché du travail.
    """)

# 3. NOS SERVICES
elif menu == "💼 Nos Services":
    st.title("💼 Nos Services de Pointe")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🌱</div>
            <h3>Assainissement & Nettoyage</h3>
            <p>Solutions de nettoyage industriel, entretien des espaces et gestion de la salubrité pour les entreprises et collectivités.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🚀</div>
            <h3>Soutien aux Jeunes Entrepreneurs</h3>
            <p>Programmes d'incubation, aide à la structuration de business plans et conseils pour le lancement de projets de jeunes start-ups.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🛠️</div>
            <h3>Prestations de Services</h3>
            <p>Assistance administrative, suivi de contrats et solutions opérationnelles externalisées pour optimiser votre temps.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🤝</div>
            <h3>Salons de l'Emploi & Recrutement</h3>
            <p>Conception et organisation d'événements de recrutement majeurs pour connecter les entreprises avec les meilleurs profils.</p>
        </div>
        """, unsafe_allow_html=True)

# 4. CONTACT
elif menu == "✉️ Contact":
    st.title("✉️ Contactez-nous")
    st.write("Choisissez le canal de communication qui vous convient le mieux pour nous joindre instantanément :")
    
    # 📱 BLOC DES BOUTONS DE CONTACT DIRECT
    st.markdown("""
    <div class="contact-grid">
        <a href="https://wa.me/243977777737" target="_blank" class="contact-card icon-whatsapp">
            <h3 style="color:#25D366 !important; margin:0;">🟢 WhatsApp</h3>
            <p style="margin:5px 0 0 0;">Discutez en direct avec nous</p>
        </a>
        <a href="tel:+243977777737" class="contact-card icon-phone">
            <h3 style="color:#007BFF !important; margin:0;">🔵 Appel Normal</h3>
            <p style="margin:5px 0 0 0;">+243 977 777 737</p>
        </a>
        <a href="mailto:contact@herbek-services.com" class="contact-card icon-email">
            <h3 style="color:#FFC107 !important; margin:0;">🟡 Email de Service</h3>
            <p style="margin:5px 0 0 0;">contact@herbek-services.com</p>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # ✉️ FORMULAIRE DE CONTACT PAR EMAIL
    st.markdown("### 📝 Ou laissez-nous un message écrit")
    form_html = """
    <form action="https://formsubmit.co/contact@herbek-services.com" method="POST" style="background:#1E2235; padding:30px; border-radius:12px; border:1px solid #2B314D; max-width:800px;">
        <input type="hidden" name="_subject" value="Nouveau message de votre site web Herbek Services !">
        <input type="hidden" name="_captcha" value="false">
        <div style="margin-bottom:15px;">
            <label style="color:white; display:block; margin-bottom:5px; font-weight:bold;">Votre Nom complet :</label>
            <input type="text" name="name" required style="width:100%; padding:12px; border-radius:6px; border:1px solid #2B314D; background:#0F111A; color:white;">
        </div>
        <div style="margin-bottom:15px;">
            <label style="color:white; display:block; margin-bottom:5px; font-weight:bold;">Votre Adresse E-mail :</label>
            <input type="email" name="email" required style="width:100%; padding:12px; border-radius:6px; border:1px solid #2B314D; background:#0F111A; color:white;">
        </div>
        <div style="margin-bottom:15px;">
            <label style="color:white; display:block; margin-bottom:5px; font-weight:bold;">Votre Message :</label>
            <textarea name="message" rows="5" required style="width:100%; padding:12px; border-radius:6px; border:1px solid #2B314D; background:#0F111A; color:white; resize:vertical;"></textarea>
        </div>
        <button type="submit" style="background:#007BFF; color:white; border:none; padding:14px 30px; border-radius:6px; font-weight:bold; cursor:pointer; font-size:16px;">🚀 Envoyer le formulaire</button>
    </form>
    """
    st.markdown(form_html, unsafe_allow_html=True)
