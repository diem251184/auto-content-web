import os
import datetime
import google.generativeai as genai

# Configurar Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Input de tema
topic = input("Escribe el tema del artículo: ")

# Prompt para Gemini
prompt = f"Escribe un artículo en español estilo blog sobre: {topic}. Incluye subtítulos y párrafos claros."
response = model.generate_content(prompt)
content = response.text.strip()

# Generar nombre de archivo
date = datetime.date.today().strftime("%Y-%m-%d")
slug = topic.lower().replace(" ", "-").replace("ñ","n")
filename = f"content/blog/{date}-{slug}.md"

# Guardar en Hugo
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"""---
title: "{topic}"
date: {date}
draft: false
---

{content}
""")

print(f"✅ Artículo generado y guardado en {filename}")
print("💡 Ahora abrí http://localhost:1313/ para ver el post en tu web local")
