# AppPanPan - Sistema de Gestión para Panadería

## Introducción

**Propósito y Objetivos**

El propósito de **AppPanPan** es ofrecer una plataforma web eficiente e intuitiva para la gestión integral de una panadería. Este sistema busca optimizar tanto la experiencia del cliente como los procesos operativos internos, permitiendo gestionar pedidos, inventarios y la producción de manera ágil y eficaz.

### Objetivos específicos:
1. **Automatizar el sistema de pedidos**: Facilitar que los clientes realicen pedidos en línea de manera rápida y sencilla.
2. **Gestión de inventarios**: Monitorear y gestionar el stock de productos en tiempo real, con alertas para evitar faltantes.
3. **Mejorar la comunicación interna**: Optimizar la comunicación entre empleados y clientes a través de notificaciones y el seguimiento de pedidos.
4. **Optimizar procesos internos**: Automatizar la facturación y los procesos de producción, reduciendo el trabajo manual y el margen de error.
5. **Análisis de ventas**: Ofrecer reportes detallados sobre las ventas, ayudando a la toma de decisiones estratégicas.

---

## Contexto del Problema

Las panaderías enfrentan diversos desafíos operativos que afectan tanto su eficiencia como rentabilidad. La gestión manual de pedidos, inventarios y la falta de herramientas para el análisis de ventas dificultan la toma de decisiones informadas que optimicen sus operaciones. Además, la competencia está aumentando, lo que hace aún más necesario contar con una solución tecnológica que permita ofrecer un mejor servicio al cliente y agilizar los procesos internos.

Las panaderías tradicionales dependen de sistemas manuales que requieren tiempo y son propensos a errores, lo que impacta negativamente en la calidad del servicio y la eficiencia de las operaciones. En muchos casos, el manejo manual del inventario aumenta el riesgo de desabastecimiento o desperdicio de ingredientes.

De acuerdo con la **Sociedad Internacional de Panadería**, hasta un 20% de las panaderías pequeñas y medianas pierden rentabilidad debido a la gestión ineficiente de su inventario.

Por otro lado, las panaderías que no tienen un sistema de pedidos en línea limitan su alcance, perdiendo la oportunidad de atraer a clientes que prefieren realizar compras cómodamente desde sus dispositivos móviles. La digitalización en este sector es clave para mantenerse competitivo en un mercado cada vez más enfocado en la tecnología.

---

## Análisis de Requerimientos

### Requerimientos Funcionales

1. **Gestión de usuarios**: El sistema debe permitir crear, editar y eliminar usuarios con roles específicos (clientes, empleados, administradores).
2. **Sistema de pedidos**: Los clientes deben poder realizar pedidos en línea, seleccionar productos, añadir al carrito y proceder al pago.
3. **Gestión de inventarios**: El sistema debe permitir seguir el estado del inventario en tiempo real, con alertas de bajo stock y opciones para añadir o editar productos.
4. **Generación de facturas**: El sistema debe generar facturas automáticas después de completar un pedido, incluyendo los detalles del pedido y los impuestos.
5. **Notificaciones**: Los usuarios deben recibir notificaciones sobre el estado de sus pedidos (confirmación, envío, entrega).
6. **Reportes de ventas**: El sistema debe generar informes de ventas diarias, semanales y mensuales.
7. **Administración de recetas**: El sistema debe permitir registrar y gestionar las recetas de los productos, detallando los ingredientes y cantidades necesarias.

### Requerimientos No Funcionales

1. **Seguridad**: Implementar un sistema de autenticación seguro y encriptación de datos sensibles.
2. **Usabilidad**: La interfaz debe ser intuitiva, fácil de usar y responsive.
3. **Escalabilidad**: El sistema debe ser escalable para soportar un aumento en la carga de usuarios y funcionalidades.
4. **Disponibilidad**: El sistema debe estar disponible 24/7 con tiempos de inactividad mínimos para mantenimiento.
5. **Compatibilidad**: Compatible con los principales navegadores web y dispositivos móviles.

### Requerimientos Técnicos

1. **Framework**: La aplicación será desarrollada usando **Django**, un framework de Python adecuado para la creación de aplicaciones web seguras y escalables.
2. **Base de datos**: Se utilizará **SQLite** para el desarrollo inicial, con la posibilidad de migrar a **PostgreSQL** o **MySQL** en el futuro.
3. **Frontend**: Se utilizarán tecnologías web como **HTML**, **CSS** y **JavaScript** para el desarrollo de la interfaz de usuario.
4. **APIs**: El sistema debe integrarse con plataformas de pago como **PayPal** o **Stripe**.
5. **Testing**: Implementar pruebas unitarias y de integración para asegurar la funcionalidad del sistema.

---



## MODELO RELACIONAL
![ModeloRelacional(Django)](https://github.com/user-attachments/assets/d9db8b85-996a-4a24-9b68-204a71fa35eb)
![ModeloRelacional](https://github.com/user-attachments/assets/38e2afe2-de81-469a-ae9a-4a4797cdd26e)


## DESARROLLO DE PROYECTO
![Inicio-Paginaprincipal](https://github.com/user-attachments/assets/702db12e-d728-4fb5-9e80-b61c5c0d2709)
![Catalogo](https://github.com/user-attachments/assets/0e5ca4ba-5be8-4ce9-a3a8-4afd2869016e)
![Contacto](https://github.com/user-attachments/assets/c6b31361-40f5-425e-82da-d76ce7324c35)













