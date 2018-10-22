'use strict';

(() => {
  let lastMousemoveEventHandleTime = 0;
  const mousemoveThrottleThreshold = 200;

  window.addEventListener('load', () => {
    console.log('window loaded');

    document.addEventListener('mousemove', mouseMoveHandler);
  });

  function mouseMoveHandler(event) {
    let eventTime = new Date().getTime();
    if (eventTime - lastMousemoveEventHandleTime > mousemoveThrottleThreshold) {
      console.log('mouse moved to:', event.clientX, event.clientY);
      lastMousemoveEventHandleTime = eventTime;
    }
  }

  class Hyperlink {
    constructor (element) {
      this.ele = element;
    }
  }
})();
