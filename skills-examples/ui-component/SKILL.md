---
name: ui-component
description: Generates UI components following vanilla JS, accessible HTML, and CSS custom property conventions. Use when creating frontend components.
---
When creating a UI component:

## Technology
- Vanilla JavaScript (ES6+) — no frameworks, no libraries, no CDN links
- No build tools (no webpack, vite, parcel)
- Must work by opening the HTML file directly in a browser

## HTML
- Use semantic HTML5 elements (main, section, article, header, nav, footer)
- All interactive elements must be keyboard-navigable
- Include proper ARIA labels on non-semantic interactive elements
- Use data attributes for JS hooks, not classes

## CSS
- Define all colors and spacing as CSS custom properties on :root
- Use Flexbox or CSS Grid for layout (no floats)
- Mobile-first responsive design with min-width breakpoints
- No inline styles — all styling in a separate .css file

## JavaScript
- Use const/let (never var)
- Event delegation where appropriate
- Separate data from presentation logic
- All sample/mock data defined as a const array at the top of the file

## File Structure
- index.html — markup and structure
- styles.css — all styling, custom properties at :root
- app.js — data, logic, DOM manipulation
