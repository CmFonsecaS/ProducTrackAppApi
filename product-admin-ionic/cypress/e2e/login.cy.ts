// cypress/integration/login.spec.js
describe('Login Test', () => {
  beforeEach(() => {
    // Limpiar cookies y caché antes de cada prueba
    cy.clearCookies();
    cy.clearLocalStorage();
    cy.window().then((win) => {
      win.caches.keys().then((cacheNames) => {
        cacheNames.forEach((cacheName) => {
          win.caches.delete(cacheName);
        });
      });
    });

    // Cargar los datos del usuario desde el archivo de datos estáticos
    cy.fixture('testData').then((data) => {
      // Crear un alias para los datos del usuario
      cy.wrap(data).as('userData');
    });
  });

  it('should log in successfully', function() {
    // Visitar la página de inicio de sesión
    cy.visit('http://localhost:8100/auth'); // Usar la URL base configurada en cypress.config.js

    // Esperar a que el elemento que contiene 'Login' esté visible
    cy.get('strong').contains('Login').should('be.visible');

    // Utilizar document.querySelector para obtener el campo de correo electrónico por su ID
    cy.window().then((win) => {
      const emailInput = win.document.querySelector('#ion-input-0');
      cy.wrap(emailInput).click().type(this['userData'].user.email); // Acceder correctamente a userData usando ['userData']
    });

    // Utilizar document.querySelector para obtener el campo de contraseña por su ID
    cy.window().then((win) => {
      const passwordInput = win.document.querySelector('#ion-input-1');
      cy.wrap(passwordInput).click().type(this['userData'].user.password); // Acceder correctamente a userData usando ['userData']
    });

    // Hacer clic en el botón de inicio de sesión
    cy.contains('Ingresar').click();

    // Esperar a que se complete la redirección y verificar la URL
    cy.url().should('include', '/home');

    // Cerrar la página al finalizar la prueba
    cy.then(() => {
      cy.window().then((win) => {
        win.close(); // Cierra la ventana actual
      });
      cy.log('Prueba finalizada exitosamente.');
    });

    // Esperar un breve tiempo antes de finalizar completamente la prueba
    cy.wait(60000); // Puedes ajustar el tiempo según sea necesario
  });
});
