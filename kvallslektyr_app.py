import streamlit as st
import random
import hashlib

# Riktiga tunga SOU:er från regeringen.se med PDF-länkar
# Sidantal är uppskattningar baserade på typiska SOU och PDF-storlek
SOU_LISTA = [
    {
        "titel": "Verktyg för en mer likvärdig resursfördelning – förslag för gymnasieskolan och anpassade gymnasieskolan",
        "sou": "SOU 2026:65",
        "sidor": 420,
        "departement": "Utbildningsdepartementet",
        "pdf": "https://www.regeringen.se/contentassets/18b08f61d7814fb0910a89afac53fcbc/verktyg-for-en-mer-likvardig-resursfordelning--forslag-for-gymnasieskolan-och-anpassade-gymnasieskolan-sou-202665.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2026/10/sou-202665/",
        "beskrivning": "Förslag på nationell skolpengsnorm för ökad likvärdighet. Tung läsning för den som vill förstå skolans finansiering."
    },
    {
        "titel": "Markerna berättar och minns – Konsekvenser för samer av svensk politik",
        "sou": "SOU 2026:58",
        "sidor": 780,
        "departement": "Kulturdepartementet",
        "pdf": "https://www.regeringen.se/contentassets/dc787ee8ec25446b8115675a94efe781/markerna-berattar-och-minns-sou-202658-volym-1.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2026/09/sou-202658/",
        "beskrivning": "Slutrapport från Sanningskommissionen. Flera volymer – riktigt kvällslektyr för den historiskt intresserade."
    },
    {
        "titel": "Förutsättningar för en likvärdig och språkutvecklande förskola",
        "sou": "SOU 2026:37",
        "sidor": 510,
        "departement": "Utbildningsdepartementet",
        "pdf": "https://www.regeringen.se/contentassets/92545fba19c94c6baaea89607295a3df/sou-202637.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2026/06/sou-202637/",
        "beskrivning": "Förslag om obligatorisk språkförskola och likvärdiga förutsättningar."
    },
    {
        "titel": "Fler möjligheter till ökat välstånd",
        "sou": "SOU 2025:96",
        "sidor": 650,
        "departement": "Finansdepartementet",
        "pdf": "https://www.regeringen.se/contentassets/473a81415a454a85b36b0af5c044a96c/sou-202596.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2025/10/sou-202596/",
        "beskrivning": "Slutbetänkande från Produktivitetskommissionen. Omfattande analys."
    },
    {
        "titel": "Digitala verktyg inom bolagsrätten",
        "sou": "SOU 2026:26",
        "sidor": 340,
        "departement": "Justitiedepartementet",
        "pdf": "https://www.regeringen.se/contentassets/3dc359ad60b0456aa99ded7d01621811/sou-202626.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2026/04/sou-202626/",
        "beskrivning": "Genomförande av EU:s direktiv om digitalisering inom bolagsrätten."
    },
    {
        "titel": "En reformerad samhällsorientering för bättre integration",
        "sou": "SOU 2025:55",
        "sidor": 390,
        "departement": "Arbetsmarknadsdepartementet",
        "pdf": "https://www.regeringen.se/contentassets/874886bd9fb44b0d9adb30a79b31cd1e/sou-202555.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2025/05/sou-202555/",
        "beskrivning": "Förslag på obligatorisk samhällsorientering med skriftligt prov."
    },
    {
        "titel": "Övergångsrestriktioner – ökat förtroende för offentlig verksamhet",
        "sou": "SOU 2023:45",
        "sidor": 280,
        "departement": "Finansdepartementet",
        "pdf": "https://www.regeringen.se/contentassets/18a3260e4ace43b6b5d7f8380c520e03/sou-202345.pdf",
        "sida": "https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2023/08/sou-202345/",
        "beskrivning": "Restriktioner vid övergång från offentlig till annan verksamhet."
    },
]

def berakna_kostnad(sidor: int) -> int:
    """Enligt Avgiftsförordningen (1992:191): 1–9 sidor gratis, 10:e sidan 50 kr, därefter 2 kr/sida."""
    if sidor < 10:
        return 0
    return 50 + 2 * (sidor - 10)

def uppskatta_vikt(sidor: int) -> float:
    """Uppskattning: ca 5 gram per A4-sida (80 gsm, enkel)."""
    return round(sidor * 0.005, 2)  # kg

def hitta_sou(namn: str, forvantningar: int):
    if not namn:
        return random.choice(SOU_LISTA)
    seed = int(hashlib.md5(namn.lower().encode()).hexdigest(), 16)
    random.seed(seed)
    # Filtrera lite efter förväntningar
    if forvantningar >= 8:
        tunga = [s for s in SOU_LISTA if s["sidor"] >= 500]
        return random.choice(tunga) if tunga else random.choice(SOU_LISTA)
    elif forvantningar <= 3:
        lätta = [s for s in SOU_LISTA if s["sidor"] <= 400]
        return random.choice(lätta) if lätta else random.choice(SOU_LISTA)
    return random.choice(SOU_LISTA)

st.set_page_config(page_title="Kvällslektyr Beställare", page_icon="📚", layout="wide")

st.title("📚 Kvällslektyr Beställare")
st.markdown(
    "**En webapp som automatiskt söker upp och beställer tunga offentliga handlingar "
    "(SOU från [regeringen.se](https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/)) "
    "hem till den som förtjänar lite kvällslektyr.**"
)

st.info("Offentlighetsprincipen i praktiken – med riktiga PDF-länkar, kostnadsräknare enligt Avgiftsförordningen och leveransadress.")

col_left, col_right = st.columns([2, 1])

with col_left:
    namn = st.text_input("Mottagarens namn (den som förtjänar kvällslektyr)", placeholder="Anna Andersson")
    forvantningar = st.slider("Hur mycket kvällslektyr förtjänar personen?", 1, 10, 7)
    
    st.subheader("📦 Leveransadress")
    gata = st.text_input("Gatuadress", placeholder="Storgatan 1")
    postnr = st.text_input("Postnummer", placeholder="123 45")
    ort = st.text_input("Ort", placeholder="Stockholm")

with col_right:
    st.subheader("💰 Kostnadsräknare")
    st.caption("Enligt Avgiftsförordningen (1992:191)")
    st.markdown("""
    - **1–9 sidor:** Gratis  
    - **10:e sidan:** 50 kr  
    - **Varje sida därefter:** 2 kr  
    - *Räknas per sida (dubbelsidigt papper = 2 sidor)*  
    - Porto tillkommer vid >20 g
    """)

if st.button("🔍 Sök upp & beställ hem", type="primary", use_container_width=True):
    if not namn.strip():
        st.warning("Ange ett namn först.")
    else:
        with st.spinner("Söker bland tunga SOU:er på regeringen.se..."):
            dok = hitta_sou(namn, forvantningar)
        
        kostnad = berakna_kostnad(dok["sidor"])
        vikt = uppskatta_vikt(dok["sidor"])
        
        st.success(f"Beställning bekräftad för **{namn}**!")
        
        st.subheader(f"{dok['titel']}")
        st.markdown(f"**{dok['sou']}** · {dok['departement']}")
        st.write(dok["beskrivning"])
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Sidor", dok["sidor"])
        m2.metric("Uppskattad vikt", f"{vikt} kg")
        m3.metric("Kostnad (exkl. porto)", f"{kostnad} kr")
        m4.metric("Förväntningar", f"{forvantningar}/10")
        
        st.markdown("### Länkar")
        st.link_button("📄 Ladda ner PDF", dok["pdf"])
        st.link_button("🔗 Sida på regeringen.se", dok["sida"])
        
        st.markdown("---")
        st.markdown("### 📮 Leveransdetaljer")
        adress = f"{namn}\n{gata}\n{postnr} {ort}".strip()
        st.code(adress if gata else "Adress ej ifylld – fyll i för korrekt leverans")
        st.markdown(f"Uppskattad vikt på försändelsen: **{vikt} kg** (ca {dok['sidor']} A4-sidor à 5 g).")
        
        if kostnad > 0:
            st.warning(f"Att betala: **{kostnad} kr** (enligt Avgiftsförordningen).")
            st.markdown("**Betalning med Swish** – de asen vill ha Swish.")
            
            # Swish-knapp
            if st.button("💳 Betala med Swish", type="primary", use_container_width=True):
                st.balloons()
                st.success(f"Swish-betalning på **{kostnad} kr** mottagen! Beställningen är nu betald och skickas till {namn}.")
                st.info("Demoläge – ingen riktig betalning har skett. I verkligheten öppnas Swish-appen eller visas en QR-kod.")
            
            st.caption("Swish-nummer (demo): 123 456 7890 · I verkligheten skickar myndigheten betalningsinformation efter att du accepterat kostnaden.")
        else:
            st.success("Avgiftsfritt – under 10 sidor! Ingen Swish behövs.")
        
        st.caption("Alla handlingar är offentliga. Detta är en demonstrativ app med verkliga SOU-länkar. "
                   "Kostnader baseras på Avgiftsförordningen (1992:191): första 9 sidor gratis, därefter 50 kr + 2 kr/sida.")

st.markdown("---")
st.caption("Byggd i Python med Streamlit • Automatiskt söker upp tunga offentliga handlingar från regeringen.se/SOU • För den som förtjänar lite kvällslektyr")
