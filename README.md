# Proyecto Final: El Dividendo Educativo en México
**Autor:** Diego Flores Prudente
**Proyecto de Data Storytelling e Inteligencia de Negocios**

## Descripción del Proyecto
Este proyecto de análisis de datos y visualización interactiva somete a prueba una de las premisas más antiguas de la política pública: ¿El esfuerzo de mantener a la población en las aulas se traduce realmente en una mayor riqueza (PIB) para los estados en México? A través de una narrativa de datos (Data Storytelling), exploramos 20 años de rezago, clústeres geográficos de riqueza y el impacto social de la desigualdad económica.

## Despliegue en Línea
🔗 **https://proyecto-final-diego.runmercury.com/**

## Fuente de Datos
Los datos utilizados en este proyecto provienen de fuentes oficiales del Gobierno de México y repositorios de código abierto:

1. **Educación (Grado Promedio de Escolaridad por Entidad Federativa):**
   * **Fuente:** INEGI (Censos y Conteos de Población y Vivienda).
   * **URL Exacta:** https://www.inegi.org.mx/app/tabulados/interactivos/?pxq=Educacion_Educacion_05_2f6d2a08-babc-442f-b4e0-25f7d324dfe0
   * **Fecha de descarga:** Abril de 2026.
   * **Formato original:** CSV.
2. **Economía (Producto Interno Bruto por Entidad Federativa):**
   * **Fuente:** INEGI (Sistema de Cuentas Nacionales de México).
   * **URL Exacta:** https://www.inegi.org.mx/app/tabulados/default.aspx?pr=17&vr=6&in=2&tp=20&wr=1&cno=2
   * **Fecha de descarga:** Abril de 2026.
   * **Formato original:** CSV.
3. **Cartografía (Polígonos de México):**
   * **Fuente:** Repositorio GitHub de angelnmara (GeoJSON).
   * **URL Exacta:** https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json

## Instrucciones para Ejecución Local
Para replicar este proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio: `git clone https://github.com/DiegoPrudente/proyecto-final-brecha-educativa.git`
2. Crea un entorno virtual e instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el servidor de Mercury en tu terminal: `mercury`
4. Abre tu navegador en la dirección `http://127.0.0.1:8000`
