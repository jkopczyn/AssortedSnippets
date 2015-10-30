var inherits = function(SubClass, SuperClass) {
  function Surrogate() {
    this.constructor = SubClass;
  }
  Surrogate.prototype = SuperClass.prototype;
  SubClass.prototype = new Surrogate();
};

var Calculator = function() {};

Calculator.prototype = {
  add: function(a, b) {
    return a + b;
  },
  subtract: function(a,b) {
    return a - b;
  },
  multiply: function(a,b) {
    return a * b;
  },
  divide: function(a,b) {
    if (b === 0) {
      return NaN;
    }
    return a / b;
  },
}


var ScientificCalculator = function() {

};

inherits(ScientificCalculator, Calculator);

ScientificCalculator.prototype.sin = function(angle) {
  return Math.sin(angle);
};

ScientificCalculator.prototype.cos = function(angle) {
  return Math.cos(angle);
};

ScientificCalculator.prototype.tan = function(angle) {
  return Math.tan(angle);
};

ScientificCalculator.prototype.log = function(n) {
  return Math.log(n);
};


var withExponents = function() {
  this.pow = function(base, exponent) {
    var accum = 1;
    for(var i = 0; i < exponent; i++) {
      accum = accum * base;
    }
    return accum;
  };

  this.multiplyExp = function(logForm1, logForm2) {
    return this.pow.apply(this,logForm1) * this.pow.apply(this, logForm2);
  }

  this.divideExp = function(logForm1, logForm2) {
    return this.pow.apply(this,logForm1) / this.pow.apply(this, logForm2);
  }
}

var delay = function(time, object, method, args) {
  //var onResolve = object[method].apply(object, args);
  var promise = new Promise(function(resolve, reject){
    setTimeout(function() {
      if(object[method]) {
        resolve(object[method].apply(object, args));
      } else {
        reject(new Error("method "+method+" not found"));
      }
    }, time);
  });
  return promise;
};
