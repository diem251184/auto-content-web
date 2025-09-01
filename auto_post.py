import os
import datetime
import google.generativeai as genai

# Configuración Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Preguntamos al usuario el tema
topic = input("Tema del artículo: ")

# Generar contenido con Gemini
prompt = f"Escribe un artículo en español, estilo blog, sobre: {topic}. Añade subtítulos y párrafos claros."
response = model.generate_content(prompt)

content = response.text.strip()

# Crear nombre del archivo
date = datetime.date.today().strftime("%Y-%m-%d")
slug = topic.lower().replace(" ", "-").replace("ñ","n")
filename = f"content/posts/{date}-{slug}.md"

# Guardar en formato Hugo (Markdown con frontmatter)
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"""---
title: "{topic}"
date: {date}
draft: false
---

{content}
""")

print(f"✅ Artículo generado y guardado en {filename}")
