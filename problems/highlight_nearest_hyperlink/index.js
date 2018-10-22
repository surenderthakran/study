'use strict';

(() => {
  let hyperlinks = [];

  let lastMousemoveEventHandleTime = 0;
  const mousemoveThrottleThreshold = 200;

  let highlightedHyperlink;

  class Point {
    constructor (x, y) {
      this.x = x;
      this.y = y;
    }
  }

  class Rectangle {
    constructor(topLeft, height, width) {
      this.topLeft = topLeft;
      this.height = height;
      this.width = width;
    }
  }

  window.addEventListener('load', () => {
    scanPageHyperlinks();

    document.addEventListener('mousemove', mouseMoveHandler);
  });

  function scanPageHyperlinks() {
    for (let anchor of document.getElementsByTagName('a')) {
      hyperlinks.push(anchor);
    }
  }

  function mouseMoveHandler(event) {
    let eventTime = new Date().getTime();
    if (eventTime - lastMousemoveEventHandleTime > mousemoveThrottleThreshold) {
      lastMousemoveEventHandleTime = eventTime;

      let nearestHyperlink = findNearestHyperlink(new Point(event.clientX,
                                                            event.clientY));

      highlightHyperlink(nearestHyperlink);
    }
  }

  function findNearestHyperlink(point) {
    let shortestDistance;
    let nearestHyperlink;

    for (let hyperlink of hyperlinks) {
      let boundingClientRect = hyperlink.getBoundingClientRect();
      let hyperlinkRect = new Rectangle(
          new Point(boundingClientRect.x, boundingClientRect.y),
          boundingClientRect.height,
          boundingClientRect.width);

      let distance = distanceBetweenRectangleAndPoint(hyperlinkRect, point);
      if (!shortestDistance || distance < shortestDistance) {
        shortestDistance = distance;
        nearestHyperlink = hyperlink;
      }
    }

    return nearestHyperlink;
  }

  /**
   *   I   |   II   | III
   *  -----+--------+-----
   *   IV  |   V    | VI
   *  -----+--------+-----
   *   VII |  VIII  | IX
   */
  function distanceBetweenRectangleAndPoint(rectangle, point) {
    let distance;
    if (point.x < rectangle.topLeft.x) {  // Quadrants I, IV or VII
      if (point.y < rectangle.topLeft.y) {  // Quadrant I
        distance = distanceBetweenPoints(point, rectangle.topLeft);
      } else if (point.y > (rectangle.topLeft.y + rectangle.height)) {  // Quadrant VII
        distance = distanceBetweenPoints(point, new Point(rectangle.topLeft.x, rectangle.topLeft.y + rectangle.height));
      } else {  // Quadrant IV
        distance = rectangle.topLeft.x - point.x;
      }
    } else if (point.x > (rectangle.topLeft.x + rectangle.width)) { // Quadrants III, VI or IX
      if (point.y < rectangle.topLeft.y) {  // Quadrant III
        distance = distanceBetweenPoints(point, new Point(rectangle.topLeft.x + rectangle.width, rectangle.topLeft.y));
      } else if (point.y > (rectangle.topLeft.y + rectangle.height)) {  // Quadrant IX
        distance = distanceBetweenPoints(point, new Point(rectangle.topLeft.x + rectangle.width, rectangle.topLeft.y + rectangle.height));
      } else {  // Quadrant VI
        distance = point.x - (rectangle.topLeft.x + rectangle.width);
      }
    } else {  // Quadrants II, V or VIII
      if (point.y < rectangle.topLeft.y) {  // Quadrant II
        distance = rectangle.topLeft.y - point.y;
      } else if (point.y > (rectangle.topLeft.y + rectangle.height)) {  // Quadrant IX
        distance = point.y - (rectangle.topLeft.y + rectangle.height);
      } else {  // Quadrant VI
        distance = 0;
      }
    }

    return distance;
  }

  function distanceBetweenPoints(p1, p2) {
    return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
  }

  function highlightHyperlink(hyperlink) {
    if (highlightedHyperlink) {
      highlightedHyperlink.style.backgroundColor = 'white';
    }

    hyperlink.style.backgroundColor = 'red';
    highlightedHyperlink = hyperlink;
  }
})();
