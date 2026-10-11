create database Minicore_Comisiones

use Minicore_Comisiones

create table vendedores(
	id int auto_increment Primary key,
    nombre varchar(100) NOt null,
    apellido varchar(100) Not null,
    correo varchar(120) not null unique,
    fecha_registro datetime default current_timestamp
)

create table ventas(
	id int auto_increment primary key,
    vendedor_id int not null,
    descripcion varchar(200) not null,
    monto decimal(10,2) not null,
    fecha_venta datetime default current_timestamp,
    constraint fk_venta_vendedor
	foreign key (vendedor_id) references vendedores(id)
)

create table reglas(
	id int auto_increment primary key,
    monto_minimo decimal(10,2) not null unique,
    porcentaje_comision decimal(5,2) not null
)


create table comisiones (
	id int auto_increment primary key,
    venta_id int not null unique,
    porcentaje_aplicado decimal(5,2) not null,
    monto_comision decimal(10,2) not null,
    estado enum('pendiente', 'pagada') not null default 'pendiente',
    constraint fk_comision_venta
		foreign key (venta_id) references ventas(id)
)

INSERT INTO reglas (id, monto_minimo, porcentaje_comision) VALUES
    (1, 1000, 0.15),
    (2, 800, 0.10),
    (3, 600, 0.06),
    (4, 500, 0.08);
    
INSERT INTO vendedores (id, nombre, apellido, correo) VALUES
    (1, 'Carlos', 'Carvajal', 'carlos@example.com'),
    (2, 'Ana', 'Torres', 'ana@example.com'),
    (3, 'Luis', 'Fernández', 'luis@example.com'),
    (4, 'María', 'López', 'maria@example.com'),
    (5, 'Jorge', 'Ramírez', 'jorge@example.com');
    

INSERT INTO ventas (id, vendedor_id, descripcion, monto) VALUES
    (1,  1, 'Licencia software empresarial', 1200.00),
    (2,  1, 'Consultoría mensual',             850.00),
    (3,  2, 'Paquete de soporte',              650.00),
    (4,  2, 'Renovación anual',                520.00),
    (5,  1, 'Capacitación al equipo',         1000.00),
    (6,  2, 'Venta minorista',                 300.00),
    (7,  3, 'Implementación ERP',             1500.00),
    (8,  3, 'Servicio de mantenimiento',       780.00),
    (9,  4, 'Venta de hardware',               950.00),
    (10, 4, 'Capacitación básica',             500.00),
    (11, 5, 'Paquete premium',                2000.00),
    (12, 5, 'Soporte técnico',                 600.00),
    (13, 3, 'Venta pequeña',                   450.00),
    (14, 4, 'Consultoría express',             700.00),
    (15, 5, 'Licencia básica',                 800.00);

INSERT INTO comisiones (id, venta_id, porcentaje_aplicado, monto_comision, estado) VALUES
    (1,  1, 0.15, 180.00, 'pagada'),
    (2,  2, 0.10,  85.00, 'pendiente'),
    (3,  3, 0.06,  39.00, 'pendiente'),
    (4,  4, 0.08,  41.60, 'pagada'),
    (5,  5, 0.15, 150.00, 'pendiente'),
    (6,  7, 0.15, 225.00, 'pendiente'),
    (7,  8, 0.06,  46.80, 'pagada'),
    (8,  9, 0.10,  95.00, 'pendiente'),
    (9,  10, 0.08,  40.00, 'pagada'),
    (10, 11, 0.15, 300.00, 'pendiente'),
    (11, 12, 0.06,  36.00, 'pendiente'),
    (12, 14, 0.06,  42.00, 'pagada'),
    (13, 15, 0.10,  80.00, 'pendiente');
    

