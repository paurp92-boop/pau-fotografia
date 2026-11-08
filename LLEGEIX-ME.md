# Pau Fotografia · com posar la web en marxa

La web llegeix tot el contingut de `content/site.json`. Aquest fitxer s'edita des del panell `/admin` (Decap CMS), sense tocar codi.

## 1. GitHub (on es guarda la web)
1. Crea un compte a https://github.com (si no en tens).
2. Fes clic a **New repository** → nom: `pau-fotografia` → **Private** o Public → **Create repository**.
3. A la pàgina del repositori nou: **uploading an existing file** → arrossega-hi TOT el contingut d'aquesta carpeta (index.html, admin, content, images) → **Commit changes**.

## 2. Netlify (on es publica)
1. Crea un compte a https://netlify.com amb el botó **Sign up with GitHub**.
2. **Add new project → Import an existing project → GitHub** → tria `pau-fotografia`.
3. Deixa en blanc *Build command*, i *Publish directory* buit (o `/`). **Deploy**.
4. En un minut tindràs una adreça del tipus `https://nom-aleatori.netlify.app`.

## 3. Activar el panell d'edició
1. A Netlify, dins el projecte: **Project configuration → Identity → Enable Identity**.
2. **Registration preferences → Invite only** (que ningú més s'hi pugui registrar).
3. **Services → Git Gateway → Enable Git Gateway**.
4. A la pestanya **Identity** (menú superior del projecte) → **Invite users** → el teu correu.
5. Obre el correu d'invitació, clica l'enllaç i tria una contrasenya.

## 4. Editar
Ves a `https://la-teva-web.netlify.app/admin`, entra amb el correu i la contrasenya, i:
- **Treballs**: afegeix fotos, canvia títols, categoria, format (vertical 2:3 / horitzontal 3:2) i dades (objectiu, diafragma, velocitat, ISO). Arrossega per reordenar.
- **General, Menú, About me, Personal, Peu**: tots els textos, correu, xarxes…
- Prem **Publish** → en ~1 minut la web està actualitzada.

Consell: exporta les fotos a uns 2000 px pel costat llarg i en JPG (qualitat 80) perquè la web vagi ràpida.

## 5. Domini propi (opcional)
Netlify → **Domain management → Add a domain** → segueix les instruccions (pots comprar-lo allà mateix o connectar-ne un que ja tinguis).
