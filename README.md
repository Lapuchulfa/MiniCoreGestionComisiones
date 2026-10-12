# MiniCoreGestionComisiones
<p>
Permite a una empresa llevar el control de sus vendedores, registrar las ventas que realizan y calcular automáticamente la comisión que les corresponde. La comisión depende de reglas por tramos: mientras mayor es el monto de una venta, mayor es el porcentaje que gana el vendedor.

El proyecto está construido con el patrón **MVC (Modelo, Vista, Controlador)**, usando Flask en el backend y MySQL como base de datos en la nube.</p>
<h2>Demo en linea</h2>
<p>https://minicore-gestion-comisiones.onrender.com/</p>

<h2>Ejecución en vivo</h2>
https://youtu.be/H2s5zdZjHpI

<h2>Funcionalidades</h2>
<p>- Vendedores: listar, crear y editar vendedores.
- Ventas: registrar ventas. Al guardarlas, el sistema busca la regla aplicable y genera la comisión automáticamente.
- Gestión de Comisiones: reporte por rango de fechas que suma las ventas de cada vendedor y calcula su comisión total.
- Comisiones: listado con filtros (todas, pendientes, pagadas) y opción para marcar una comisión como pagada.
- Reglas: consulta de los tramos de comisión vigentes.</p>

<h2>Capturas</h2>

<h3> Vendedores</h3>
<img width="1689" height="628" alt="image" src="https://github.com/user-attachments/assets/29f653c1-6f22-4740-8a34-75310e06ad1c" />

<h3>Ventas</h3>
<img width="1732" height="1000" alt="image" src="https://github.com/user-attachments/assets/eda7782d-a354-46f2-8942-154d3c7f6fc1" />


<h3>Gestión de comisiones</h3>
<img width="1732" height="372" alt="image" src="https://github.com/user-attachments/assets/6e3f7395-3f76-4b71-8ba5-40b869872f2b" />

<img width="1676" height="507" alt="image" src="https://github.com/user-attachments/assets/2e7621ef-e50f-412a-bf56-8acfb3db8cda" />

<h3>Comisiones</h3>
<img width="1633" height="1019" alt="image" src="https://github.com/user-attachments/assets/75bc27c3-4804-41cd-8c22-6b2383780344" />

<h3>Reglas</h3>
<img width="1688" height="490" alt="image" src="https://github.com/user-attachments/assets/8b363da9-8b59-41ca-b243-a18a2bd74989" />

## Tecnologías utilizadas

- **Python** + **Flask**: servidor web y rutas (Blueprints)
- **MySQL**: base de datos relacional, alojada en **Aiven**
- **Jinja2**: plantillas HTML dinámicas
- **Bootstrap 5**: diseño visual responsivo
- **python-dotenv**: manejo de variables de entorno
- **Gunicorn**: servidor para el despliegue

## Autor
| [<img src="https://github.com/Lapuchulfa.png" width=115><br><sub><Tu nombre></sub>](https://github.com/Lapuchulfa) |
| :---: |

Trabajo Academico CRUD y Login — Ingeniería Web, Semestre 7, UDLA.
