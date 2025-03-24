# 1. Declarar una lista vacía
empty_list = []

# 2. Declarar una lista con más de 5 elementos
my_list = [10, 20, 30, 40, 50, 60]

# 3. Encontrar la longitud de tu lista
print("Longitud de la lista:", len(my_list))

# 4. Obtener el primer elemento, el del medio y el último elemento de la lista
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]
print("Primer elemento:", first_item)
print("Elemento del medio:", middle_item)
print("Último elemento:", last_item)

# 5. Declarar una lista llamada mixed_data_types con información personal
mixed_data_types = ["TuNombre", 25, 1.75, "Soltero/a", "TuDirección"]
print("Lista de datos mixtos:", mixed_data_types)

# 6. Declarar una lista llamada it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista
print("Empresas de TI:", it_companies)

# 8. Imprimir el número de empresas
print("Número de empresas:", len(it_companies))

# 9. Imprimir la primera, media y última empresa
print("Primera empresa:", it_companies[0])
print("Empresa del medio:", it_companies[len(it_companies) // 2])
print("Última empresa:", it_companies[-1])

# 10. Modificar una empresa y mostrar la lista
it_companies[0] = "Meta"
print("Lista modificada:", it_companies)

# 11. Agregar una empresa de TI
it_companies.append("Spotify")
print("Lista con empresa añadida:", it_companies)

# 12. Insertar una empresa en el medio
it_companies.insert(len(it_companies) // 2, "Tesla")
print("Lista después de insertar en el medio:", it_companies)

# 13. Cambiar una empresa a mayúsculas (excluyendo IBM)
it_companies[1] = it_companies[1].upper()
print("Lista con una empresa en mayúsculas:", it_companies)

# 14. Unir las empresas con un separador
joined_companies = " #;&nbsp; ".join(it_companies)
print("Empresas unidas:", joined_companies)

# 15. Verificar si una empresa está en la lista
company_to_check = "Google"
print(f"¿{company_to_check} está en la lista?", company_to_check in it_companies)

# 16. Ordenar la lista
it_companies.sort()
print("Lista ordenada:", it_companies)

# 17. Revertir el orden de la lista
it_companies.reverse()
print("Lista en orden descendente:", it_companies)

# 18. Extraer las primeras 3 empresas
print("Primeras 3 empresas:", it_companies[:3])

# 19. Extraer las últimas 3 empresas
print("Últimas 3 empresas:", it_companies[-3:])

# 20. Extraer las empresas del medio
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print("Empresas del medio:", it_companies[middle_index-1:middle_index+1])
else:
    print("Empresa del medio:", it_companies[middle_index])

# 21. Eliminar la primera empresa
it_companies.pop(0)
print("Lista después de eliminar la primera empresa:", it_companies)

# 22. Eliminar la(s) empresa(s) del medio
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index-1:middle_index+1]
else:
    del it_companies[middle_index]
print("Lista después de eliminar la(s) empresa(s) del medio:", it_companies)

# 23. Eliminar la última empresa
it_companies.pop(-1)
print("Lista después de eliminar la última empresa:", it_companies)

# 24. Eliminar todas las empresas de la lista
it_companies.clear()
print("Lista después de eliminar todas las empresas:", it_companies)

# 25. Destruir la lista
del it_companies
# print(it_companies) # Esto causará un error porque la lista ya no existe.

# 26. Unir listas front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Full Stack:", full_stack)

# 27. Copiar la lista y añadir Python y SQL después de Redux
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Redux") + 2, "SQL")
print("Full Stack actualizado:", full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista y encontrar el mínimo y máximo
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Agregar el mínimo y máximo de nuevo a la lista
ages.append(min_age)
ages.append(max_age)

# Encontrar la mediana
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
else:
    median_age = ages[len(ages) // 2]

# Encontrar el promedio
average_age = sum(ages) / len(ages)

# Encontrar el rango
age_range = max_age - min_age

# Comparar (min - promedio) y (max - promedio) usando abs()
compare_min_avg = abs(min_age - average_age)
compare_max_avg = abs(max_age - average_age)

# Imprimir los resultados
print("Edades ordenadas:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)
print("Mediana:", median_age)
print("Promedio:", average_age)
print("Rango:", age_range)
print("|min - promedio|:", compare_min_avg)
print("|max - promedio|:", compare_max_avg)


# Puedes usar esta lista como referencia inicial:
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria"
]  # Usa la lista completa desde el enlace si necesitas más.

# Encontrar el país o los países del medio
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]

print("País(es) del medio:", middle_countries)

# Dividir la lista en dos partes
half = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:half]
    second_half = countries[half:]
else:
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]

print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic_countries = countries

print("Primeros tres países:", first, second, third)
print("Países escandinavos:", scandic_countries)
