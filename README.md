# Proyecto de Servicio de Reparación de Ropa

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Django que permite gestionar un servicio de reparación de ropa. La aplicación incluye funcionalidades básicas de CRUD (Crear, Leer, Actualizar y Eliminar) para las reparaciones, así como gestión de usuarios, perfil y autenticación.

## Características

- **CRUD de Reparaciones**: Permite añadir, editar, visualizar y eliminar reparaciones.
- **Gestión de Usuarios**: Incluye funcionalidades para el registro, inicio de sesión y perfil de usuario.
- **Panel de Administración**: Utiliza el panel de administración de Django para gestionar los datos.
- **Plantillas**: Utiliza herencia de plantillas para mantener la consistencia del diseño.

## Información del Alumno

- **Nombre Completo**: [Danitza Requena Espinoza]
- **Comisión**: [Coderhouse 57830]
- **LinkedIn**: [https://www.linkedin.com/in/danitza-requena-espinoza-070619211/]

## Instalación y Configuración

1. **Clonar el Repositorio**:

   git clone [https://github.com/Danitzalinda/Coderhouse-57830-DanitzaRequenaE.git]
   cd . project

2. **Configurar entorno virtual**:   
python -m venv .venv
source env/bin/activate  # En Windows: env\Scripts\activate

3. **Aplicar Migraciones**:
python manage.py makemigrations
python manage.py migrate

4. **Crear un Superusuario**:
python manage.py createsuperuser
Iniciar el Servidor: servicios
password: 123
python manage.py runserver
Visita http://127.0.0.1:8000/ para acceder a la aplicación.

## Aplicaciones Utilizadas
Django: Framework web utilizado para desarrollar la aplicación.

## Mejoras Futuras
Funcionalidad de Búsqueda: Implementar una función de búsqueda para encontrar reparaciones fácilmente.
Mejoras en el Diseño: Mejorar el diseño y la experiencia del usuario utilizando frameworks avanzados como Bootstrap
Sistema de Notificaciones: Implementar un sistema de notificaciones para alertar a los usuarios sobre el estado de sus reparaciones.
Funcionalidades Avanzadas para el Perfil de Usuario: Permitir a los usuarios actualizar sus fotos de perfil directamente desde la 