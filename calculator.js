
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
