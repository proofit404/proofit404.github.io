import 'highlight.js/styles/zenburn.css'
import hljs from 'highlight.js'

import 'reveal.js/css/reveal.css'
import 'reveal.js/css/theme/league.css'

import 'headjs/dist/1.0.0/head.js'

import './notes.js'

hljs.initHighlightingOnLoad()

Reveal.initialize({
  controls: false,
  progress: false,
  slideNumber: true,
  history: true,
  center: true,
  transition: 'none'
})

window.Reveal = Reveal
