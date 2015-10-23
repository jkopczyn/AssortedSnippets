(function() {

var getStorageManager =  function() {
  if( typeof this.storageManager === "undefined") {
    this.storageManager = new StorageManager();
  }
  return this.storageManager;
};

var StorageManager = function() {
  this.localStorage = localStorage;
  this.time = new Date();
};

StorageManager.prototype = {
 set: function(key, value, expiry) {
   var expireTime = this.time.getTime() + expiry;
   this.localStorage.setItem(key, 
                      JSON.stringify({"value": value, "expire": expireTime}));
 },

 get: function(key) {
   var now = this.time.getTime();
   var obj = JSON.parse(this.localStorage.getItem(key));
   if(typeof obj === "undefined") {
     return undefined;
   } else if (obj["expire"] < now) {
     this.localStorage.remove(key);
     return undefined;
   } else {
     return obj["value"];
   }
 },

 remove: function(key) {

 },

 setProperty: function(key, property, value, expiry) {

 },
};


getStorageManager();
})();
