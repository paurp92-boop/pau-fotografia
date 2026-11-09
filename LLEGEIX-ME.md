# Pau Fotografia · com posar la web en marxa

La web llegeix tot el contingut de `content/site.json`. Aquest fitxer s'edita des de Pages CMS (Pages CMS), sense tocar codi.

## 1. GitHub (on es guarda la web)
1. Crea un compte a https://github.com (si no en tens).
2. Fes clic a **New repository** → nom: `pau-fotografia` → **Private** o Public → **Create repository**.
3. A la pàgina del repositori nou: **uploading an existing file** → arrossega-hi TOT el contingut d'aquesta carpeta (index.html, admin, content, images) → **Commit changes**.

## 2. Cloudflare Pages (on es publica)
1. Crea un compte a https://dash.cloudflare.com i ves a **Workers & Pages → Create → Pages → Connect to Git**.
2. Tria `pau-fotografia`. Nom del projecte `pau-fotografia`, branca de producció `main`, *Framework preset* `None`, *Build command* i *Output directory* buits. **Save and Deploy**.
3. En un minut tindràs `https://pau-fotografia.pages.dev`. Cada canvi a `main` es publica sol.

## 3. Panell d'edició (Pages CMS)
1. Ves a https://app.pagescms.org i entra amb GitHub.
2. Tria el repositori `pau-fotografia` i la branca `main`. La configuració és al fitxer `.pages.yml`.

## 4. Editar
Dins Pages CMS, obre **Tot el contingut de la web**:
- **Treballs**: afegeix fotos, canvia títols, categoria, format (vertical 2:3 / horitzontal 3:2) i dades (objectiu, diafragma, velocitat, ISO). Arrossega per reordenar.
- **General, Menú, About me, Equip, Personal, Peu**: tots els textos, correu, xarxes…
- Desa (**Save**) → en ~1 minut la web està actualitzada.

Consell: exporta les fotos a uns 2000 px pel costat llarg i en JPG (qualitat 80) perquè la web vagi ràpida.

## 5. Domini propi (opcional)
Cloudflare → el projecte → **Custom domains → Set up a custom domain**.
