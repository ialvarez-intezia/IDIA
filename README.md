# Sistema de Propuestas — Intezia

Repositorio de Markdown que organiza la información de Intezia y guía a Claude para producir **propuestas comerciales** (slides HTML), **diseño curricular** y **calendario** de cada capacitación.

Intezia opera bajo dos divisiones (**Fundación** y **Educación**) y produce tres categorías de documento curricular: **Charla**, **Curso/Diplomado**, **Taller/Capacitación In-Company**.

## Estructura

```
.
├── CLAUDE.md                 ← router (Claude lo lee primero, siempre)
├── aprendizajes.md           ← changelog del sistema
├── logos/{fundacion,educacion}/{BLANCO,NEGRO}.png
├── empresa/                  ← información estática
│   ├── identidad.md          ← misión, visión, tono
│   ├── divisiones.md         ← Fundación vs Educación
│   ├── marca-visual.md       ← logos, colores, tipografía
│   ├── tipos-de-documento.md ← 3 categorías y reglas duras
│   ├── catalogo.md           ← programas reales
│   └── politicas-comerciales.md
├── plantillas/
│   ├── propuesta-comercial.md
│   ├── calendario.md
│   └── diseno-{charla,taller,capacitacion,curso,diplomado}.md
├── fuentes/formatos-oficiales/  ← PDFs oficiales (referencia inmutable)
├── scripts/{listar-pdfs,ver-pdf}.sh
└── clientes/propuestas/<empresa-slug>/   ← todo plano dentro
    ├── brief.md
    ├── programa.md
    ├── calendario.md
    ├── index.html                        ← entregable web
    ├── styles.css
    └── propuesta.pdf                     ← entregable visible para el cliente
```

## Cómo se usa

Abre Claude en esta carpeta y conversa:

> "Arma una propuesta para Banco Pacífico — taller de liderazgo, 2 grupos de 15, en mayo."

Claude leerá `CLAUDE.md`, te preguntará primero **¿Fundación o Educación?** (regla bloqueante) e identificará el tipo de documento. Luego generará todo en `clientes/banco-pacifico/`.

## Scripts de terminal

```bash
./scripts/listar-pdfs.sh                 # listar todos los PDFs
./scripts/listar-pdfs.sh -- liderazgo    # filtrar por término
./scripts/ver-pdf.sh catalogo            # abrir por nombre o término
./scripts/ver-pdf.sh -q catalogo.pdf     # vista rápida (Quick Look)
```

Todos aceptan `-h` para ayuda.

## Lo que tienes que llenar tú

Archivos con placeholders esperando tu contenido real:

1. `empresa/identidad.md` — misión, visión, tono.
2. `empresa/divisiones.md` — qué hace Fundación y qué hace Educación.
3. `empresa/marca-visual.md` — paleta de colores y tipografía oficial.
4. `empresa/catalogo.md` — programas reales que ofreces.
5. `empresa/politicas-comerciales.md` — tarifas y condiciones.

Mientras estos archivos no estén completos, Claude usa neutros y avisa cuando tiene que asumir algo.

## Convenciones

- **Slug de cliente**: minúsculas, sin tildes, espacios → guiones. "Banco del Pacífico" → `banco-del-pacifico`.
- **Fechas**: ISO `YYYY-MM-DD`.
- **Códigos de programa**: `TA-###` (taller), `CAP-###` (capacitación), `CU-###` (curso), `DIP-###` (diplomado). Charlas no llevan código.
- **División en `brief.md`**: campo `division: fundacion | educacion` obligatorio.
