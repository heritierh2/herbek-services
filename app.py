import streamlit as st
import os

# Configuration de la page
st.set_page_config(
    page_title="Herbek Services",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS PERSONNALISÉ (SÉCURISÉ) ---
st.markdown("""
<style>
    /* Arrière-plan global et polices */
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
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161925;
        border-right: 1px solid #24293E;
    }
    
    /* Cartes des services */
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
    
    /* Boutons */
    .btn-container {
        display: flex;
        gap: 15px;
        margin-top: 20px;
    }
    .btn-whatsapp {
        background-color: #25D366 !important;
        color: white !important;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
    }
    .btn-tel {
        background-color: #007BFF !important;
        color: white !important;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
    }
    
    /* Espacement des sections */
    .section-spacer {
        padding: 60px 0;
        border-bottom: 1px solid #1E2235;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR & LOGO ---
with st.sidebar:
    logo_path = "assets/logo.jpg"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.title("Herbek Services")
    
    st.caption("EXCELLENCE AU SERVICE DE VOTRE RÉUSSITE")
    st.markdown("---")
    st.markdown("### 📌 Navigation Rapide")
    st.info("Faites défiler la page vers le bas ou utilisez les liens pour naviguer.")

# --- CONTENU UNIQUE DÉROULANT (ONE-PAGE) ---

# 1. ACCUEIL
st.markdown('<div class="section-spacer">', unsafe_allow_html=True)
st.subheader("Votre partenaire de confiance")
st.title("Herbek Services")
st.markdown("#### *L'excellence au service de votre réussite*")
st.write(
    "Nous fournissons des solutions de service professionnelles, fiables et parfaitement adaptées "
    "à vos besoins spécifiques pour propulser vos projets et vos communications vers de nouveaux sommets."
)

# Intégration propre des boutons d'action rapide
st.markdown("""
<div class="btn-container">
    <a href="https://wa.me/243977777737" target="_blank" class="btn-whatsapp">💬 Discuter sur WhatsApp</a>
    <a href="tel:+243977777737" class="btn-tel">📞 Nous appeler au +243 977 777 737</a>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# 2. À PROPOS DE NOUS (ENRICHI)
st.markdown('<div class="section-spacer">', unsafe_allow_html=True)
st.title("🤝 À propos de nous")
st.write(
    "Herbek Services est une structure d'élite spécialisée dans l'accompagnement stratégique, "
    "la gestion opérationnelle et la transformation numérique des entreprises et des particuliers. "
    "Forts de notre expertise terrain et d'une parfaite maîtrise des outils technologiques modernes, "
    "nous intervenons comme un véritable catalyseur de croissance."
)
st.write(
    "Notre philosophie repose sur trois piliers fondamentaux : la rigueur administrative, l'innovation technologique "
    "par l'automatisation des processus, et le développement continu des compétences humaines. Que vous soyez une start-up "
    "en plein essor ou une organisation établie, nous concevons des solutions sur mesure qui optimisent votre quotidien."
)
st.markdown('</div>', unsafe_allow_html=True)


# 3. NOS SERVICES
st.markdown('<div class="section-spacer">', unsafe_allow_html=True)
st.title("💼 Nos Services de Pointe")
st.write("Découvrez les expertises clés que nous mettons à votre disposition :")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">📋</div>
        <h3>Conseil & Accompagnement Commercial</h3>
        <p>Un accompagnement stratégique personnalisé pour structurer vos projets professionnels. Nous analysons votre positionnement sur le marché, identifions les leviers de croissance et élaborons des plans d'action commerciaux percutants pour maximiser vos résultats.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">📊</div>
        <h3>Gestion & Administration</h3>
        <p>Optimisation complète de votre gestion administrative, comptable et logistique. Nous prenons en charge le suivi contractuel, l'organisation de vos flux internes et la structuration de vos rapports pour vous permettre de vous concentrer sur votre cœur de métier en toute sérénité.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">💻</div>
        <h3>Solutions Numériques & Automatisation</h3>
        <p>Conception de vitrines web modernes et mise en place d'architectures numériques avancées. Nous intégrons des systèmes d'automatisation de pointe (via WhatsApp Business et CRM) pour fluidifier vos communications clients, gérer vos listes de diffusion et moderniser votre présence en ligne.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <div class="service-icon">🎓</div>
        <h3>Formation & Renforcement des Capacités</h3>
        <p>Programmes de formation sur mesure conçus pour élever les compétences de vos équipes. Nos modules couvrent les techniques de vente modernes, la gestion de projet, l'appropriation des outils digitaux et les meilleures pratiques administratives.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# 4. POURQUOI NOUS
st.markdown('<div class="section-spacer">', unsafe_allow_html=True)
st.title("✨ Pourquoi choisir Herbek Services ?")
st.markdown("""
- **Professionnalisme de haut niveau :** Une rigueur et une réactivité totales à chaque étape de notre collaboration.
- **Approche orientée résultats :** Des solutions concrètes et adaptées qui répondent à vos indicateurs de performance.
- **Maîtrise technologique :** L'utilisation des meilleurs outils digitaux pour automatiser et valoriser vos activités.
- **Flexibilité et sur-mesure :** Chaque structure est unique, nos interventions le sont aussi.
""")
st.markdown('</div>', unsafe_allow_html=True)


# 5. CONTACT (CORRIGÉ ET SÉCURISÉ)
st.markdown('<div class="section-spacer">', unsafe_allow_html=True)
st.title("✉️ Contactez-nous")
st.write("Une question, un besoin ou un projet ? Remplissez ce formulaire sécurisé pour nous envoyer un message directement.")

form_html = """
<form action="https://formsubmit.co/contact@herbek-services.com" method="POST" style="background:#1E2235; padding:30px; border-radius:12px; border:1px solid #2B314D; max-width: 800px;">
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
    <button type="submit" style="background:#007BFF; color:white; border:none; padding:14px 30px; border-radius:6px; font-weight:bold; cursor:pointer; font-size:16px;">🚀 Envoyer le message</button>
</form>
"""
# L'ajout de unsafe_allow_html=True ici corrige définitivement l'affichage du formulaire !
st.markdown(form_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
