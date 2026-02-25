# Guest Feedback Dashboard

## Build & Test
- Language: HTML, CSS, JavaScript (vanilla ES6+)
- Run: Open index.html in a browser (no server needed)
- Test: Open in browser, verify all filters work, check console for errors

## Conventions
- No external dependencies — no CDN links, no npm packages, no build tools
- Must work by opening index.html directly from the filesystem
- Use semantic HTML5 elements (main, section, article, header, footer)
- Accessible: all interactive elements keyboard-navigable, proper ARIA labels
- CSS custom properties (variables) for colors and spacing
- All sample data embedded directly in JavaScript
- Mobile-responsive layout using CSS Grid or Flexbox

## File Structure
- index.html — single entry point, all markup
- styles.css — all styles, custom properties at :root
- app.js — data, logic, DOM manipulation

## Don't
- Don't use any framework or library (no React, Vue, jQuery, etc.)
- Don't make network requests or fetch external resources
- Don't use build tools (no webpack, vite, parcel)
- Don't use hardcoded absolute paths
