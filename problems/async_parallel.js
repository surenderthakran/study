'use strict';

(function() {
	class Async {
    parallel(tasks, callback) {
      const response = [];
      callback(response);
    }
  }

	function asyncTask(name, cb) {
	  setTimeout(() => {
	    cb(null, 'task ' + name + ' done!');
	  }, Math.random() * 1000);
	}

  const tasks = [];

  const async = new Async();
  async.parallel(tasks, (result) => {
    console.log(result);
  })
})();
