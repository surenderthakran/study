'use strict';

(() => {
  window.addEventListener('load', () => {
    console.log('window loaded');

    document.addEventListener('mousemove', throttleMouseMoveEvents(200, mouseMoveHandler));
  });

  function throttleMouseMoveEvents(delay, handler) {
    let lastCalled;
    return handler;
  }

  function mouseMoveHandler(event) {
    console.log('mouse moved to:', event.clientX, event.clientY);
  }

  class Hyperlink {
    constructor (element) {
      this.ele = element;
    }
  }
})();
