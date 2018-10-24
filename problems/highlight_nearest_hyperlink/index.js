'use strict';
/**
 * Highlight nearest hyperlink to the mouse cursor.
 */

(() => {
  /**
   * List of hyperlinks in the page.
   */
  let hyperlinks = [];

  /**
   * Time since mousemove event was handled last.
   */
  let lastMousemoveEventHandleTime = 0;

  /**
   * Minimum time between two mousemove event handlings.
   */
  const mousemoveThrottleThreshold = 200;

  /**
   * Currently highlighted hyperlink.
   */
  let highlightedHyperlink;

  /**
   * Class representing an Euclidean point.
   */
  class Point {

    /**
     * Constructor for class Point.
     *
     * @param {number} x x-coordinate of mouse's location.
     * @param {number} y y-coordinate of mouse's location.
     */
    constructor (x, y) {
      this.x = x;
      this.y = y;
    }
  }

  /**
   * Class representing an Euclidean rectangle.
   */
  class Rectangle {

    /**
     * Constructor for class Rectangle.
     *
     * @param {Point} topLeft Top-Left corner of the rectangle.
     * @param {number} height of the rectangle.
     * @param {number} width of the rectangle..
     */
    constructor(topLeft, height, width) {
      this.topLeft = topLeft;
      this.height = height;
      this.width = width;
    }
  }

  /**
   * Set listener for when all page contents are loaded.
   */
  window.addEventListener('load', () => {
    // Identify all hyperlinks in the page.
    for (let anchor of document.getElementsByTagName('a')) {
      hyperlinks.push(anchor);
    }

    // Set listener on mousemove events.
    document.addEventListener('mousemove', mouseMoveHandler);
  });

  /**
   * Function handling mosemove events.
   * @param {!MouseEvent} event - mousemove event object.
   */
  function mouseMoveHandler(event) {
    // Current timestamp.
    let eventTime = new Date().getTime();

    // If current timestamp is after throttling threshold has expired.
    if (eventTime - lastMousemoveEventHandleTime > mousemoveThrottleThreshold) {
      lastMousemoveEventHandleTime = eventTime;

      // Find nearest hyperlink to the mouse cursor.
      let nearestHyperlink = findNearestHyperlink(new Point(event.clientX,
                                                            event.clientY));

      if (nearestHyperlink) {
        // Highlight nearest hyperlink.
        highlightHyperlink(nearestHyperlink);
      }
    }
  }

  /**
   * Function to find nearest hyperlink to the given point.
   * @param {!Point} point Current mouse cursor location.
   *
   * @return {?HTMLAnchorElement} Hyperlink nearest to the mouse cursor.
   */
  function findNearestHyperlink(point) {
    let shortestDistance;
    let nearestHyperlink;

    // Iterate over list of all hyperlinks.
    for (let hyperlink of hyperlinks) {
      // Identify current bounds of the hyperlink.
      let boundingClientRect = hyperlink.getBoundingClientRect();
      let hyperlinkRect = new Rectangle(
          new Point(boundingClientRect.x, boundingClientRect.y),
          boundingClientRect.height,
          boundingClientRect.width);

      // Calculate shortest distance between the point and the rectangle.
      let distance = distanceBetweenRectangleAndPoint(hyperlinkRect, point);

      // If distance is the shortest till now, mark the hyperlink as nearest.
      if (!shortestDistance || distance < shortestDistance) {
        shortestDistance = distance;
        nearestHyperlink = hyperlink;
      }
    }

    return nearestHyperlink;
  }

  /**
   * Function to find distance between a rectangle and a point.
   * The space around the rectangle (section V) is divided into several
   * sections.
   *
   *   I   |   II   | III
   *  -----+--------+-----
   *   IV  |   V    | VI
   *  -----+--------+-----
   *   VII |  VIII  | IX
   *
   * @param {!Rectangle} rectangle Rectangle depicting bounds of a hyperlink.
   * @param {!Point} point Currnt mouse cursor location.
   *
   * @return {number}
   */
  function distanceBetweenRectangleAndPoint(rectangle, point) {
    let distance;

    if (point.x < rectangle.topLeft.x) {  // Sections I, IV or VII
      if (point.y < rectangle.topLeft.y) {  // Section I
        distance = distanceBetweenPoints(point, rectangle.topLeft);
      } else if (point.y > (rectangle.topLeft.y + rectangle.height)) {  // Section VII
        distance = distanceBetweenPoints(
            point, new Point(rectangle.topLeft.x,
                             rectangle.topLeft.y + rectangle.height));
      } else {  // Section IV
        distance = rectangle.topLeft.x - point.x;
      }
    } else if (point.x > (rectangle.topLeft.x + rectangle.width)) { // Sections III, VI or IX
      if (point.y < rectangle.topLeft.y) {  // Section III
        distance = distanceBetweenPoints(
            point, new Point(rectangle.topLeft.x + rectangle.width,
                             rectangle.topLeft.y));
      } else if (
          point.y > (rectangle.topLeft.y + rectangle.height)) {  // Section IX
        distance = distanceBetweenPoints(
            point, new Point(rectangle.topLeft.x + rectangle.width,
                             rectangle.topLeft.y + rectangle.height));
      } else {  // Section VI
        distance = point.x - (rectangle.topLeft.x + rectangle.width);
      }
    } else {  // Sections II, V or VIII
      if (point.y < rectangle.topLeft.y) {  // Section II
        distance = rectangle.topLeft.y - point.y;
      } else if (point.y > (rectangle.topLeft.y + rectangle.height)) {  // Section IX
        distance = point.y - (rectangle.topLeft.y + rectangle.height);
      } else {  // Section VI
        distance = 0;
      }
    }

    return distance;
  }

  /**
   * Function to find distance between two points.
   * @param {!Point} p1 Euclidean point.
   * @param {!Point} p2 Euclidean point.
   *
   * @return {number}
   */
  function distanceBetweenPoints(p1, p2) {
    return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
  }

  /**
   * Function to highlight and unhighlight hyperlinks.
   * @param {!HTMLAnchorElement} hyperlink Hyperlink to highlight.
   */
  function highlightHyperlink(hyperlink) {
    if (highlightedHyperlink) {
      highlightedHyperlink.style.backgroundColor = 'white';
    }

    hyperlink.style.backgroundColor = 'red';
    highlightedHyperlink = hyperlink;
  }
})();
