'use strict';

(function() {

	class Async {

    parallel(tasks, callback) {
      const response = [];
      let finished = 0;

      const interval = setInterval(() => {
        if (finished === tasks.length) {
          clearInterval(interval);
          return callback(response);
        }
      }, 200);

      for (let i = 0, len = tasks.length; i < len; i++) {
        tasks[i]((err, result) => {
          console.log(result);
          finished++;
          response[i] = result;
        });
      }
    }
  }

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

  const async = new Async();
  async.parallel(tasks, (result) => {
    console.log(result);
  });
})();
