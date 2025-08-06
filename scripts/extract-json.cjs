const fs = require('fs');

const input = 'public/direct-messages.js';
const output = 'public/direct-messages.json';

let content = fs.readFileSync(input, 'utf8');
content = content.replace(/^window\.YTD\.direct_messages\.part0\s*=\s*/, '');
fs.writeFileSync(output, content);

console.log('Saved cleaned JSON to:', output);
