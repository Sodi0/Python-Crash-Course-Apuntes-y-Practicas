text = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."

#Encontrar la cantidad de veces que aparece la palabra "better"
count_better = text.count("better")
print(f"La palabra 'better' aparece {count_better} veces.")

#Mostrar todo el texto en mayúsculas
upper_text = text.upper()
print("Texto en mayúsculas:" + "\n" + upper_text)

#Reemplazar la letra "i" por "&"
replaced_text = text.replace("i", "&")
print("Texto con 'i' reemplazada por '&':" + "\n" + replaced_text)