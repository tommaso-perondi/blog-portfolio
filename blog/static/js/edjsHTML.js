!function(e,t){"object"==typeof exports&&"undefined"!=typeof module?module.exports=t():"function"==typeof define&&define.amd?define(t):(e="undefined"!=typeof globalThis?globalThis:e||self).edjsHTML=t()}(this,(function(){"use strict";var e={delimiter:function(){return"<br/>"},header:function(e){var t=e.data;return"<h"+t.level+">"+t.text+"</h"+t.level+">"},paragraph:function(e){return"<p>"+e.data.text+"</p>"},list:function(e){var t=e.data,n="unordered"===t.style?"ul":"ol",r="";return t.items&&(r=t.items.map((function(e){return"<li>"+e+"</li>"})).reduce((function(e,t){return e+t}),"")),"<"+n+">"+r+"</"+n+">"},image:function(e){var t=e.data,n=t.caption?t.caption:"Image";return'<img src="'+(t.file?t.file.url:"")+'" alt="'+n+'" />'},quote:function(e){var t=e.data;return"<blockquote>"+t.text+"</blockquote> - "+t.caption},code:function(e){return"<pre><code>"+e.data.code+"</code></pre>"}};function t(e){return new Error('[31m The Parser function of type "'+e+'" is not defined. \n\n  Define your custom parser functions as: [34mhttps://github.com/pavittarx/editorjs-html#extend-for-custom-blocks [0m')}return function(n){return void 0===n&&(n={}),Object.assign(e,n),{parse:function(n){return n.blocks.map((function(n){return e[n.type]?e[n.type](n):t(n.type)}))},parseBlock:function(n){return e[n.type]?e[n.type](n):t(n.type)}}}}));
