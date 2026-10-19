#-------------------------------------------------------------#
#        MANEJO DE NUMEROS Y BOOLEANOS EN PYTHON
#-------------------------------------------------------------#
"""
PORTADA
Nombre: Aldo Manuel Castañon Garcia 
Matricula: 2630174 
Grupo: IM 1-2
"""
#-------------------------------------------------------------#
#  RESUMEN EJECUTIVO 
#-------------------------------------------------------------#
"""
En Python, el tipo de dato `int` se utiliza para representar números enteros, 
mientras que `float` permite trabajar con números decimales, la principal 
diferencia es que los enteros no tienen parte decimal y los flotantes sí
pueden tenerla. Los booleanos son un tipo de dato que representa dos valores:
`True` y `False` estos valores se obtienen mediante comparaciones, como 
verificar si un número es mayor, menor o igual que otro. Validar rangos es 
importante para asegurar que los datos ingresados estén dentro de los límites
permitidos. También es necesario evitar la división entre cero, ya que provoca 
un error durante la ejecución del programa. En este documento se describirá 
cada problema, incluyendo el diseño de sus entradas y salidas. Además, 
se explicarán las validaciones aplicadas y el uso de `int`, `float` y booleanos para 
tomar decisiones y obtener resultados correctos.
--------------------------------------------------
PRINCIPIOS Y BUENAS PRÁCTICAS 
--------------------------------------------------
- Usar tipos apropiados: int para contadores, float para cantidades con decimales.
- Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
- Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
- Usar nombres de variables descriptivos y mensajes claros para el usuario.
- Documentar claramente cómo se interpretan los booleanos (qué significa true y qué significa false en cada contexto).

"""
#-------------------------------------------------------------#
#       PROBLEMAS
#-------------------------------------------------------------#
#Problem 1: Temperature converter and range flag
#-------------------------------------------------------------#
"""
Descripción:
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, 
determina un valor booleano is_high_temperature que sea true si la temperatura en Celsius 
es mayor o igual que 30.0 y false en caso contrario.

Entradas:
- temp_c (float; temperatura en °C).

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Test cases:
1) Normal: 35 -> high temperature: true
2) Border: -273.15 -> Kelvin: 0.0
3) Error: abc -> invalid input
"""
print("\nfirst problem".upper())
print("Temperature converter and range flag\n".title())

try:
    temp_c = float(input("Enter temperature in Celsius: "))

    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: impossible Kelvin temperature")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: invalid input")

#-------------------------------------------------------------#
#Problem 2 Work Hours and Overtime Payment
#-------------------------------------------------------------#
"""
Descripción:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate 
(float). Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera 
un booleano has_overtime que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 45 hours, rate 100
2) Border: 40 hours, rate 100
3) Error: -5 hours, rate 100
"""
print("\nsecond problem".upper())
print("Work Hours and Overtime Payment\n".title())

try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", has_overtime)

except ValueError:
    print("Error: invalid input")

#-------------------------------------------------------------#
# Problem 3: Discount Eligibility with Booleans
#-------------------------------------------------------------#
"""
Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Entradas:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Salidas:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Test cases:
1) Normal: 1200, YES, NO -> eligible
2) Border: 1000, NO, NO -> eligible
3) Error: -10, YES, NO -> invalid input
"""
print("\nthird problem".upper())
print("Discount Eligibility with Booleans\n".title())

try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

    if (purchase_total < 0 or
        is_student_text not in ("YES", "NO") or
        is_senior_text not in ("YES", "NO")):
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000.0
        )

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", round(final_total, 2))

except ValueError:
    print("Error: invalid input")


#-------------------------------------------------------------#
# Problem 4: Basic Statistics of Three Integers
#-------------------------------------------------------------#
"""
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo 
y un booleano all_even que indique si los tres números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Test cases:
1) Normal: 2, 4, 6 -> all even: true
2) Border: 0, 0, 0 -> all even: true
3) Error: 2, abc, 6 -> invalid input
"""

print("\nfourth problem".upper())
print("Basic Statistics of Three Integers\n".title())

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (
        n1 % 2 == 0 and
        n2 % 2 == 0 and
        n3 % 2 == 0
    )

    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)

except ValueError:
    print("Error: invalid input")

#-------------------------------------------------------------#
# Problem 5: Loan Eligibility
#-------------------------------------------------------------#
"""
Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Entradas:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Salidas:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 10000, 2000, 700 -> eligible
2) Border: 8000, 3200, 650 -> eligible
3) Error: 0, 1000, 700 -> invalid input
"""

print("\nfifth problem".upper())
print("Loan Eligibility\n".title())

try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if (monthly_income <= 0 or monthly_debt < 0
            or credit_score < 0):
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", eligible)

except ValueError:
    print("Error: invalid input")


#-------------------------------------------------------------#
# Problem 6: Body Mass Index (BMI)
#-------------------------------------------------------------#
"""
Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Entradas:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Salidas:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 70 kg, 1.75 m -> normal
2) Border: 50 kg, 1.70 m -> underweight
3) Error: 70 kg, 0 m -> invalid input
"""

print("\nsixth problem".upper())
print("Body Mass Index\n".title())

try:
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)

except ValueError:
    print("Error: invalid input")
#-------------------------------------------------------------#
#   CONCLUSIONES
#-------------------------------------------------------------#
"""
Al final se concluye que el manejo de números y booleanos en Python es fundamental para la
resolución de problemas que involucran cálculos y decisiones lógicas. El uso adecuado de estos
tipos de datos permite implementar validaciones y cálculos precisos por la facilidad de herramientas
que ofrece Python desde la escala binaria para la toma de deciciones, como los calculos que se 
pueden realizar con los tipos de datos `int` y `float`, así como la evaluación de condiciones con booleanos.
"""
#-------------------------------------------------------------#
#    Referencias
#-------------------------------------------------------------#
"""
1 https://ellibrodepython.com/booleano-python
2 https://cjtu-github-io.translate.goog/spirl/python_basic-types.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
3 https://missyera.com/guias/python-desde-cero/variables-y-tipos/?srsltid=AU7gw4Uhj3vo0vkI81roIP5jLyzReWr5eM91BJ0OuWljRphizIgoiSqX
4 https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwiflK6HssWXAxVLIEQIHQaHA9kQtwJ6BAgSEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DcWtePcvuSIk&usg=AOvVaw3kaTz3JC0y3DxSAw6TqdVv&opi=89978449
5 https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwiflK6HssWXAxVLIEQIHQaHA9kQtwJ6BAgUEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DuOkJypqeRmw&usg=AOvVaw1Sj5aeXaGBiTV5P6GFYPEp&opi=89978449
"""