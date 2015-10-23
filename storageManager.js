(function() {

var getStorageManager =  function() {
  if( typeof this.storageManager === "undefined") {
    this.storageManager = new StorageManager();
  }
  return this.storageManager;
};

var StorageManager = function() {

};

StorageManager.prototype = {
 set: function(key, value, expiry) {

 },

 get: function(key) {

 },

 remove: function(key) {

 },

 setProperty: function(key, property, value, expiry) {

 },
};

})();
