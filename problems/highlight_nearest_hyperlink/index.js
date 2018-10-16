'use strict';

(() => {
  window.addEventListener('load', () => {
    console.log('window loaded');

    document.addEventListener('mousemove', (event) => {
      console.log('mouse moved to:', event.clientX, event.clientY);
    });
  });

  class Hyperlink {
    constructor (element) {
      this.ele = element;
    }
  }
})();
