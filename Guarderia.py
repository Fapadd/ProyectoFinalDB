import pyodbc

def connect_to_db():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=Guarderia69;'
        'UID=sa;'
        'PWD=<YourStrong@Passw0rd>;'
        'TrustServerCertificate=yes'
    )
    return conn

def insertar_niño():
    numero_matricula = input("Ingrese el número de matrícula: ")
    nombre = input("Ingrese el nombre del niño: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
    fecha_baja = input("Ingrese la fecha de baja (deje en blanco si no aplica): ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarNiño ?, ?, ?, ?, ?;
    """
    cursor.execute(query, (numero_matricula, nombre, fecha_nacimiento, fecha_ingreso, fecha_baja))
    conn.commit()
    conn.close()
    print("Niño registrado exitosamente.")

def consultar_niños():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarNiños;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("Listado de Niños:")
    for row in rows:
        print(row)
    conn.close()

def insertar_persona_autorizada():
    ci = input("Ingrese el número de cédula de identidad: ")
    nombre = input("Ingrese el nombre de la persona autorizada: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el número de teléfono: ")
    relacion = input("Ingrese la relación con el niño: ")
    matricula = input("Ingrese el número de matrícula del niño asociado: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarPersonaAutorizada ?, ?, ?, ?, ?, ?;
    """
    cursor.execute(query, (ci, nombre, direccion, telefono, relacion, matricula))
    conn.commit()
    conn.close()
    print("Persona autorizada registrada exitosamente.")

def consultar_personas_autorizadas():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarPersonasAutorizadas;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Personas Autorizadas:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar pagadores, menús, platos, ingredientes, alergias, consumo de alimentos,
# servicios adicionales, consumo de servicios adicionales, materiales e insumos de tienda, y atención de especialistas.

def insertar_pagador():
    ci = input("Ingrese el número de cédula de identidad: ")
    nombre = input("Ingrese el nombre del pagador: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el número de teléfono: ")
    cuenta_corriente = input("Ingrese el número de cuenta corriente: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarPagador ?, ?, ?, ?, ?;
    """
    cursor.execute(query, (ci, nombre, direccion, telefono, cuenta_corriente))
    conn.commit()
    conn.close()
    print("Pagador registrado exitosamente.")

def consultar_pagadores():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarPagadores;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Pagadores:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar menús

def insertar_menu():
    numero_menu = input("Ingrese el número de menú: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarMenú ?;
    """
    cursor.execute(query, (numero_menu,))
    conn.commit()
    conn.close()
    print("Menú registrado exitosamente.")

def consultar_menus():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarMenús;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Menús:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar platos

def insertar_plato():
    nombre_plato = input("Ingrese el nombre del plato: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarPlato ?;
    """
    cursor.execute(query, (nombre_plato,))
    conn.commit()
    conn.close()
    print("Plato registrado exitosamente.")

def consultar_platos():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarPlatos;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Platos:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar ingredientes

def insertar_ingrediente():
    nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarIngrediente ?;
    """
    cursor.execute(query, (nombre_ingrediente,))
    conn.commit()
    conn.close()
    print("Ingrediente registrado exitosamente.")

def consultar_ingredientes():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarIngredientes;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Ingredientes:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar alergias

def insertar_alergia():
    numero_matricula = input("Ingrese el número de matrícula del niño: ")
    nombre_ingrediente = input("Ingrese el nombre del ingrediente alergénico: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarAlergia ?, ?;
    """
    cursor.execute(query, (numero_matricula, nombre_ingrediente))
    conn.commit()
    conn.close()
    print("Alergia registrada exitosamente.")

def consultar_alergias():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarAlergias;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Alergias:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar consumo de alimentos

def insertar_consumo_alimentos():
    numero_matricula = input("Ingrese el número de matrícula del niño: ")
    numero_menu = input("Ingrese el número de menú: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    num_dias = input("Ingrese el número de días: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarConsumoAlimentos ?, ?, ?, ?;
    """
    cursor.execute(query, (numero_matricula, numero_menu, fecha, num_dias))
    conn.commit()
    conn.close()
    print("Consumo de alimentos registrado exitosamente.")

def consultar_consumo_alimentos():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarConsumoAlimentos;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Consumo de Alimentos:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar servicios adicionales

def insertar_servicio_adicional():
    nombre_servicio = input("Ingrese el nombre del servicio adicional: ")
    precio = input("Ingrese el precio del servicio adicional: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarServicioAdicional ?, ?;
    """
    cursor.execute(query, (nombre_servicio, precio))
    conn.commit()
    conn.close()
    print("Servicio adicional registrado exitosamente.")

def consultar_servicios_adicionales():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarServiciosAdicionales;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Servicios Adicionales:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar consumo de servicios adicionales

def insertar_consumo_servicios_adicionales():
    numero_matricula = input("Ingrese el número de matrícula del niño: ")
    id_servicio = input("Ingrese el ID del servicio adicional: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarConsumoServicioAdicional ?, ?, ?;
    """
    cursor.execute(query, (numero_matricula, id_servicio, fecha))
    conn.commit()
    conn.close()
    print("Consumo de servicio adicional registrado exitosamente.")

def consultar_consumo_servicios_adicionales():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarConsumoServiciosAdicionales;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Consumo de Servicios Adicionales:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar materiales e insumos de tienda

def insertar_material_insumo_tienda():
    nombre = input("Ingrese el nombre del material o insumo: ")
    cantidad = input("Ingrese la cantidad: ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarMaterialInsumoTienda ?, ?;
    """
    cursor.execute(query, (nombre, cantidad))
    conn.commit()
    conn.close()
    print("Material o insumo registrado exitosamente.")

def consultar_materiales_insumos_tienda():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarMaterialesInsumosTienda;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Materiales e Insumos de Tienda:")
    for row in rows:
        print(row)
    conn.close()

# Define funciones para insertar y consultar atención de especialistas

def insertar_atencion_especialista():
    numero_matricula = input("Ingrese el número de matrícula del niño: ")
    tipo_especialista = input("Ingrese el tipo de especialista: ")
    precio = input("Ingrese el precio de la atención: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC InsertarAtencionEspecialista ?, ?, ?, ?;
    """
    cursor.execute(query, (numero_matricula, tipo_especialista, precio, fecha))
    conn.commit()
    conn.close()
    print("Atención de especialista registrada exitosamente.")

def consultar_atencion_especialista():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    EXEC ConsultarAtencionEspecialista;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Listado de Atención de Especialistas:")
    for row in rows:
        print(row)
    conn.close()

# Define función para el menú principal

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar niño")
        print("2. Consultar lista de niños")
        print("3. Registrar persona autorizada")
        print("4. Consultar lista de personas autorizadas")
        print("5. Registrar pagador")
        print("6. Consultar lista de pagadores")
        print("7. Registrar menú")
        print("8. Consultar lista de menús")
        print("9. Registrar plato")
        print("10. Consultar lista de platos")
        print("11. Registrar ingrediente")
        print("12. Consultar lista de ingredientes")
        print("13. Registrar alergia")
        print("14. Consultar lista de alergias")
        print("15. Registrar consumo de alimentos")
        print("16. Consultar lista de consumo de alimentos")
        print("17. Registrar servicio adicional")
        print("18. Consultar lista de servicios adicionales")
        print("19. Registrar consumo de servicio adicional")
        print("20. Consultar lista de consumo de servicios adicionales")
        print("21. Registrar material o insumo de tienda")
        print("22. Consultar lista de materiales e insumos de tienda")
        print("23. Registrar atención de especialista")
        print("24. Consultar lista de atención de especialistas")
        print("25. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            insertar_niño()
        elif opcion == '2':
            consultar_niños()
        elif opcion == '3':
            insertar_persona_autorizada()
        elif opcion == '4':
            consultar_personas_autorizadas()
        elif opcion == '5':
            insertar_pagador()
        elif opcion == '6':
            consultar_pagadores()
        elif opcion == '7':
            insertar_menu()
        elif opcion == '8':
            consultar_menus()
        elif opcion == '9':
            insertar_plato()
        elif opcion == '10':
            consultar_platos()
        elif opcion == '11':
            insertar_ingrediente()
        elif opcion == '12':
            consultar_ingredientes()
        elif opcion == '13':
            insertar_alergia()
        elif opcion == '14':
            consultar_alergias()
        elif opcion == '15':
            insertar_consumo_alimentos()
        elif opcion == '16':
            consultar_consumo_alimentos()
        elif opcion == '17':
            insertar_servicio_adicional()
        elif opcion == '18':
            consultar_servicios_adicionales()
        elif opcion == '19':
            insertar_consumo_servicios_adicionales()
        elif opcion == '20':
            consultar_consumo_servicios_adicionales()
        elif opcion == '21':
            insertar_material_insumo_tienda()
        elif opcion == '22':
            consultar_materiales_insumos_tienda()
        elif opcion == '23':
            insertar_atencion_especialista()
        elif opcion == '24':
            consultar_atencion_especialista()
        elif opcion == '25':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()

