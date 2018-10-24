'use strict';

/**
 * Implement an async.parallel function that calls an array of asynchronous
 * functions and returns all of their results in a single callback.
 */

(function() {

  const async = {};
  /**
   * Calls an array of asynchronous functions in parallel and returns their
   * results in a single callback.
   *
   * @param {!Array.<!Function>} tasks Array of asynchronous functions.
   * @param {!Function} callback Callback function.
   */
  async.parallel = (tasks, callback) => {
    const response = [];
    let finished = 0;

    // Iterate over all the asynchronous functions.
    for (let i = 0, len = tasks.length; i < len; i++) {
      // Call each function with a callback.
      tasks[i]((err, result) => {
        console.log(result);

        // Add current function's result to the response array at its
        // corresponding index in the tasks array.
        response[i] = result;

        // Increment count of finished functions by 1.
        finished++;

        // If the current function was the last function to finish.
        if (finished === tasks.length) {
          // Return by passing the response array to the async.parallel's
          // callback.
          return callback(response);
        }
      });
    }
  };

  // Create array of asynchronous functions.
  const tasks = [
    function(cb) {
      setTimeout(() => {
        cb(null, 1);
      }, Math.random() * 1000);
    },
    function(cb) {
      setTimeout(() => {
        cb(null, 2);
      }, Math.random() * 1000);
    },
    function(cb) {
      setTimeout(() => {
        cb(null, 3);
      }, Math.random() * 1000);
    },
    function(cb) {
      setTimeout(() => {
        cb(null, 4);
      }, Math.random() * 1000);
    },
  ];

  // Call async.parallel with the array of asynchronous functions and a
  // callback.
  async.parallel(tasks, (result) => {
    console.log(result);
  });
})();
