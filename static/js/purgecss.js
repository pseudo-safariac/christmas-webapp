// Import the PurgeCSS package
const PurgeCSS = require('purgecss');

// Create a new PurgeCSS instance with the specified options
const purgecss = new PurgeCSS({
  // An array of file patterns for the HTML files to analyze
  content: ['templates/**/*.html'],
  // An array of file patterns for the CSS files to optimize
  css: ['static/css/styles.css'],
  // A file path for the generated CSS file
  output: 'static/css/purged.css',
  // An array of CSS selectors to keep in the CSS file
  safelist: ['.dont-purge']
});

// Run PurgeCSS and save the optimized CSS to a file
purgecss.purge((purgedCss) => {
  const fs = require('fs');
  fs.writeFileSync('static/css/purged.css', purgedCss.join(''));
});
