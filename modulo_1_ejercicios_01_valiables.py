# EJERCICIOS ^^

# 1. Crea la variable `gatos` que sea un número con el valor `8`.

gatos = 8

# 2. Crea la variable `perros`  que sea un texto de seis caracteres: la palabra `cuatro`.

perros = "cuatro"

# 3. Imprime la variable `gatos`.

print(gatos)

# 4. Imprime la variable `perros`.

print(perros)

# 5. Imprime la variable `perros` seguida por la palabra `más` y la palabra `perros` otra vez.

print(perros, "mas", perros)

# 6. Consigue que el ordenador devuelva el siguiente texto, usando la variable `perros`: `cuatro más cuatro es igual a 8`.

print(perros, "mas", perros, "es igual a", gatos)

# 7. Consigue que el ordenador devuelva el siguiente texto, usando la variable`perros`: `cuatro + cuatro = 8`.

print(perros, "+" , perros, "=", gatos)

# 8. Define una variable `pizzas` con un valor `2` que sea del tipo float.
# 9. Define `magdalenas` con un valor `2` que sea del tipo string.
# 10. Define `postres` con un valor `0` que sea del tipo int.

pizzas = float(2)
magdalenas = str(2)
postres = int(0)

# 11. ¿Qué tipo de dato es la variable `pizzas`?

print(type(pizzas))

# 12. ¿Es la variable `magdalenas` de tipo string?

print(isinstance(magdalenas,str))

# 13. Define `postres` con un valor `0`.

postres = 0

# 14. Calcula la suma de `gatos` y `pizzas`.

print("la suma de 8 + 2_TipoFloat es igual a", gatos + pizzas)

# 15. Calcula la diferencia entre `gatos` y `pizzas`.

print("la diferencia es de", gatos - pizzas)

# 16. Multiplica las cantidad de gatos por 2.

print("8 * 2 =", gatos * 2)

# 17. Crea una variable `piezas` que sea 8 veces la cantidad de `pizzas`.

piezas = pizzas * 8

# 18. Haz que la cantidad de `piezas` se aumente en 3.

print("8 * 2 + 3 =", piezas + 3)

# 19. Calcula el cuadrado de 9 y guárdalo en una variable llamada `superficie`.

superficie = 9 ** 2

print("9² =",superficie)

# 20. ¿Cuánta superficie hay por gato?
  #No estoy segura a que se referia.

Superficie_por_gato = superficie / gatos

print("Hay",Superficie_por_gato, "de superficie por gato")

# 21.¿Cuántas piezas enteras hay por gato?

piezas_por_gato = piezas // gatos

print("Hay",piezas_por_gato, "por gato.")

# 22. ¿Cuántas piezas te quedan si cada gato se come 21 piezas?

print(piezas * gatos)
print("Te quedan",piezas - (gatos * 21), "por gato.")

# 23. ¿Cuánta superficie hay por gato en metros cuadrados? Redondeala a un sólo decimal. Intenta calcularlo dentro del mismo `print()` en una sola línea.

print(round(Superficie_por_gato / 2,1))

# 24. ¿Es verdad que hay más gatos que pizzas?

print(gatos > pizzas)

# 25. ¿Es verdad que hay menos gatos que superficie?

print(gatos < superficie)

# 26. ¿Es verdad que 2 veces la cantidad de pizzas es distinto de la cantidad de gatos?

print(pizzas ** 2 != gatos)

# 27. ¿Es falso que 2 veces la cantidad de pizzas es igual a la cantidad de gatos?

print(pizzas ** 2 == gatos)

# 28. La variable `piezas`, es mayor o igual a `pizzas` y `superficie` es distinto de cero?

print(piezas >= pizzas, superficie != 0)

# 29. La variable `piezas`, es mayor o igual a `pizzas` y menor que `superficie`?

print(piezas >= pizzas, piezas < superficie)

# 30. Me interesa saber si hay más pizzas que gatos, o si el residuo de piezas por gato es cero.

print(pizzas > gatos, (piezas % gatos) == 0)

# 31. Comprueba las comparaciones de 29. en una sola línea, sin usar la variable `piezas` más que una sola vez.

print(piezas >= pizzas
      and piezas < superficie)

# 32. Comprueba si `superficie` es diferente a cero sin usar `!=`.

print(superficie is not 0)

# 33. Usa `input()` para preguntar a un usuario el día de su cumpleaños y guarda la respuesta en la variable dia_cumple.

dia_cumple = input("Ingrese Día de cumpleaños:")
print("   " + dia_cumple + "   ")

# 34. Usa `input()` para preguntar a un usuario el mes de su cumpleaños y guarda la respuesta en la variable mes_cumple.

mes_cumple = input("Ingrese Mes de cumpleaños:")
print("   " + mes_cumple + "   ")

# 35. Usa `.strip()` en ambas de las variables definidas.

print(dia_cumple.strip())
print(mes_cumple.strip())

# 36. Haz que `fecha_cumple` sea un *string* compuesto por el día y el mes.

fecha_cumple = dia_cumple + "/" + mes_cumple
print(fecha_cumple)

# 37. Imprime `Fecha de cumpleaños es` más el día y el mes.

print("Fecha de cumpleaños es: " + fecha_cumple)

# 38. Imprime la variable perros en todas mayúsculas.

print(perros.upper())