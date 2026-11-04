Kvällslektyr Beställare
=======================

En webapp som automatiskt söker upp och beställer tunga offentliga handlingar
(SOU från regeringen.se) hem till den som förtjänar lite kvällslektyr.

Funktioner
----------
- Riktiga SOU:er med PDF-länkar från regeringen.se/SOU
- Kostnadsräknare enligt Avgiftsförordningen (1992:191):
  * 1–9 sidor: gratis
  * 10:e sidan: 50 kr
  * Varje sida därefter: 2 kr
- Sidräknare och uppskattad vikt (ca 5 g/sida)
- Leveransadress
- Swish-knapp (demoläge)
- Slider för hur mycket kvällslektyr personen “förtjänar”

Köra appen lokalt
-----------------
1. Installera beroenden:
   pip install -r requirements.txt

2. Starta appen:
   streamlit run kvallslektyr_app.py

3. Öppna webbläsaren på http://localhost:8501

Deploya på Streamlit Cloud
--------------------------
1. Lägg upp filerna i ett publikt GitHub-repo.
2. Gå till share.streamlit.io och logga in.
3. Klicka "New app", välj ditt repo och sätt main file till kvallslektyr_app.py.
4. Deploy.

Filer
-----
- kvallslektyr_app.py   Huvudappen
- requirements.txt      Beroenden (streamlit)
- README.txt            Den här filen

Källor
------
- Avgiftsförordningen (1992:191)
- Regeringen.se (Statens offentliga utredningar)

Byggd i Python med Streamlit.
För den som förtjänar lite kvällslektyr.
