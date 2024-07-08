const { defineConfig } = require("cypress");

module.exports = defineConfig({
  component: {
    devServer: {
      framework: "angular",
      bundler: "webpack",
    },
    specPattern: "**/*.cy.ts",
  },
  e2e: {
    setupNodeEvents(on, config) {
      // Implementar los eventos del nodo aquí si es necesario
    },
    supportFile: false, // Desactiva el archivo de soporte si no es necesario
    baseUrl: 'http://localhost:8100', // Configura la URL base
  },
  
});