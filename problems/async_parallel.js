'use strict';

(function() {

  const async = {
    parallel: (tasks, callback) => {
      const response = [];
      let finished = 0;

      for (let i = 0, len = tasks.length; i < len; i++) {
        tasks[i]((err, result) => {
          console.log(result);
          finished++;
          response[i] = result;
          if (finished === tasks.length) {
            return callback(response);
          }
        });
      }
    }
  };

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

  async.parallel(tasks, (result) => {
    console.log(result);
  });
})();
