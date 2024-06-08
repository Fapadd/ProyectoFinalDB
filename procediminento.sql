CREATE DATABASE Guarderia69;
use Guarderia69;

-- Creación de las Tablas

CREATE TABLE Niño (
    NumeroMatricula INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    FechaNacimiento DATE,
    FechaIngreso DATE,
    FechaBaja DATE
);

CREATE TABLE PersonaAutorizada (
    CI INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Direccion NVARCHAR(100),
    Telefono NVARCHAR(15),
    RelacionConNiño NVARCHAR(100),
    NumeroMatricula INT FOREIGN KEY REFERENCES Niño(NumeroMatricula)
);

CREATE TABLE Pagador (
    CI INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Direccion NVARCHAR(100),
    Telefono NVARCHAR(15),
    NumeroCuentaCorriente NVARCHAR(20)
);

CREATE TABLE Menú (
    NumeroMenú INT PRIMARY KEY
);

CREATE TABLE Plato (
    Nombre NVARCHAR(100) PRIMARY KEY
);

CREATE TABLE Ingrediente (
    Nombre NVARCHAR(100) PRIMARY KEY
);

CREATE TABLE Alergia (
    NumeroMatricula INT,
    Nombre NVARCHAR(100),
    PRIMARY KEY (NumeroMatricula, Nombre),
    FOREIGN KEY (NumeroMatricula) REFERENCES Niño(NumeroMatricula),
    FOREIGN KEY (Nombre) REFERENCES Ingrediente(Nombre)
);

CREATE TABLE ConsumoAlimentos (
    NumeroMatricula INT,
    NumeroMenú INT,
    Fecha DATE,
    NumDias INT,
    FOREIGN KEY (NumeroMatricula) REFERENCES Niño(NumeroMatricula),
    FOREIGN KEY (NumeroMenú) REFERENCES Menú(NumeroMenú)
);

CREATE TABLE ServicioAdicional (
    ID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100),
    Precio DECIMAL(10, 2)
);

CREATE TABLE ConsumoServiciosAdicionales (
    NumeroMatricula INT,
    IDServicio INT,
    Fecha DATE,
    PRIMARY KEY (NumeroMatricula, IDServicio, Fecha),
    FOREIGN KEY (NumeroMatricula) REFERENCES Niño(NumeroMatricula),
    FOREIGN KEY (IDServicio) REFERENCES ServicioAdicional(ID)
);

CREATE TABLE MaterialesInsumosTienda (
    ID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100),
    Cantidad INT
);

CREATE TABLE AtencionEspecialista (
    ID INT PRIMARY KEY IDENTITY,
    NumeroMatricula INT,
    TipoEspecialista NVARCHAR(100),
    Precio DECIMAL(10, 2),
    Fecha DATE,
    FOREIGN KEY (NumeroMatricula) REFERENCES Niño(NumeroMatricula)
);


-- Creación de los Procedimientos Almacenados

-- Procedimiento almacenado para insertar un niño
CREATE PROCEDURE InsertarNiño
    @NumeroMatricula INT,
    @Nombre NVARCHAR(100),
    @FechaNacimiento DATE,
    @FechaIngreso DATE,
    @FechaBaja DATE
AS
BEGIN
    INSERT INTO Niño (NumeroMatricula, Nombre, FechaNacimiento, FechaIngreso, FechaBaja)
    VALUES (@NumeroMatricula, @Nombre, @FechaNacimiento, @FechaIngreso, @FechaBaja);
END;

-- Procedimiento almacenado para consultar todos los niños
CREATE PROCEDURE ConsultarNiños
AS
BEGIN
    SELECT * FROM Niño;
END;

-- Procedimiento almacenado para insertar una persona autorizada
CREATE PROCEDURE InsertarPersonaAutorizada
    @CI INT,
    @Nombre NVARCHAR(100),
    @Direccion NVARCHAR(100),
    @Telefono NVARCHAR(15),
    @RelacionConNiño NVARCHAR(100),
    @NumeroMatricula INT
AS
BEGIN
    INSERT INTO PersonaAutorizada (CI, Nombre, Direccion, Telefono, RelacionConNiño, NumeroMatricula)
    VALUES (@CI, @Nombre, @Direccion, @Telefono, @RelacionConNiño, @NumeroMatricula);
END;

-- Procedimiento almacenado para consultar todas las personas autorizadas
CREATE PROCEDURE ConsultarPersonasAutorizadas
AS
BEGIN
    SELECT * FROM PersonaAutorizada;
END;

-- Procedimiento almacenado para insertar un pagador
CREATE PROCEDURE InsertarPagador
    @CI INT,
    @Nombre NVARCHAR(100),
    @Direccion NVARCHAR(100),
    @Telefono NVARCHAR(15),
    @NumeroCuentaCorriente NVARCHAR(20)
AS
BEGIN
    INSERT INTO Pagador (CI, Nombre, Direccion, Telefono, NumeroCuentaCorriente)
    VALUES (@CI, @Nombre, @Direccion, @Telefono, @NumeroCuentaCorriente);
END;

-- Procedimiento almacenado para consultar todos los pagadores
CREATE PROCEDURE ConsultarPagadores
AS
BEGIN
    SELECT * FROM Pagador;
END;

-- Procedimiento almacenado para insertar un menú
CREATE PROCEDURE InsertarMenú
    @NumeroMenú INT
AS
BEGIN
    INSERT INTO Menú (NumeroMenú)
    VALUES (@NumeroMenú);
END;

-- Procedimiento almacenado para consultar todos los menús
CREATE PROCEDURE ConsultarMenús
AS
BEGIN
    SELECT * FROM Menú;
END;

-- Procedimiento almacenado para insertar un plato
CREATE PROCEDURE InsertarPlato
    @Nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO Plato (Nombre)
    VALUES (@Nombre);
END;

-- Procedimiento almacenado para consultar todos los platos
CREATE PROCEDURE ConsultarPlatos
AS
BEGIN
    SELECT * FROM Plato;
END;

-- Procedimiento almacenado para insertar un ingrediente
CREATE PROCEDURE InsertarIngrediente
    @Nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO Ingrediente (Nombre)
    VALUES (@Nombre);
END;

-- Procedimiento almacenado para consultar todos los ingredientes
CREATE PROCEDURE ConsultarIngredientes
AS
BEGIN
    SELECT * FROM Ingrediente;
END;

-- Procedimiento almacenado para insertar una alergia
CREATE PROCEDURE InsertarAlergia
    @NumeroMatricula INT,
    @Nombre NVARCHAR(100)
AS
BEGIN
    INSERT INTO Alergia (NumeroMatricula, Nombre)
    VALUES (@NumeroMatricula, @Nombre);
END;

-- Procedimiento almacenado para consultar todas las alergias
CREATE PROCEDURE ConsultarAlergias
AS
BEGIN
    SELECT * FROM Alergia;
END;

-- Procedimiento almacenado para insertar un consumo de alimentos
CREATE PROCEDURE InsertarConsumoAlimentos
    @NumeroMatricula INT,
    @NumeroMenú INT,
    @Fecha DATE,
    @NumDias INT
AS
BEGIN
    INSERT INTO ConsumoAlimentos (NumeroMatricula, NumeroMenú, Fecha, NumDias)
    VALUES (@NumeroMatricula, @NumeroMenú, @Fecha, @NumDias);
END;

-- Procedimiento almacenado para consultar todos los consumos de alimentos
CREATE PROCEDURE ConsultarConsumoAlimentos
AS
BEGIN
    SELECT * FROM ConsumoAlimentos;
END;

-- Procedimiento almacenado para insertar un servicio adicional
CREATE PROCEDURE InsertarServicioAdicional
    @Nombre NVARCHAR(100),
    @Precio DECIMAL(10, 2)
AS
BEGIN
    INSERT INTO ServicioAdicional (Nombre, Precio)
    VALUES (@Nombre, @Precio);
END;

-- Procedimiento almacenado para consultar todos los servicios adicionales
CREATE PROCEDURE ConsultarServiciosAdicionales
AS
BEGIN
    SELECT * FROM ServicioAdicional;
END;

-- Procedimiento almacenado para insertar un consumo de servicio adicional
CREATE PROCEDURE InsertarConsumoServicioAdicional
    @NumeroMatricula INT,
    @IDServicio INT,
    @Fecha DATE
AS
BEGIN
    INSERT INTO ConsumoServiciosAdicionales (NumeroMatricula, IDServicio, Fecha)
    VALUES (@NumeroMatricula, @IDServicio, @Fecha);
END;

-- Procedimiento almacenado para consultar todos los consumos de servicios adicionales
CREATE PROCEDURE ConsultarConsumoServiciosAdicionales
AS
BEGIN
    SELECT * FROM ConsumoServiciosAdicionales;
END;

-- Procedimiento almacenado para insertar un material o insumo en la tienda
CREATE PROCEDURE InsertarMaterialInsumoTienda
    @Nombre NVARCHAR(100),
    @Cantidad INT
AS
BEGIN
    INSERT INTO MaterialesInsumosTienda (Nombre, Cantidad)
    VALUES (@Nombre, @Cantidad);
END;

-- Procedimiento almacenado para consultar todos los materiales e insumos en la tienda
CREATE PROCEDURE ConsultarMaterialesInsumosTienda
AS
BEGIN
    SELECT * FROM MaterialesInsumosTienda;
END;

-- Procedimiento almacenado para insertar una atención de especialista
CREATE PROCEDURE InsertarAtencionEspecialista
    @NumeroMatricula INT,
    @TipoEspecialista NVARCHAR(100),
    @Precio DECIMAL(10, 2),
    @Fecha DATE
AS
BEGIN
    INSERT INTO AtencionEspecialista (NumeroMatricula, TipoEspecialista, Precio, Fecha)
    VALUES (@NumeroMatricula, @TipoEspecialista, @Precio, @Fecha);
END;

-- Procedimiento almacenado para consultar todas las atenciones de especialistas
CREATE PROCEDURE ConsultarAtencionEspecialista
AS
BEGIN
    SELECT * FROM AtencionEspecialista;
END;

