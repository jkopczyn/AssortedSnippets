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
   this.time = new Date();
   var expireTime = this.time.getTime() + expiry;
   var obj = {"value": value, "expire": expireTime}
   this.localStorage.setItem(key, JSON.stringify(obj));
   return obj;
 },

 get: function(key) {
   this.time = new Date();
   var now = this.time.getTime();
   var obj = JSON.parse(this.localStorage.getItem(key));
   if(typeof obj === "undefined" || obj === null) {
     return undefined;
   } else if (obj["expire"] < now) {
     this.remove(key);
     return undefined;
   } else {
     return obj["value"];
   }
 },

 remove: function(key) {
   this.time = new Date();
   this.localStorage.removeItem(key);
 },

 setProperty: function(key, property, value, expiry) {
   this.time = new Date();
   var now = this.time.getTime();
   var obj = JSON.parse(this.localStorage.getItem(key));
   if(typeof obj === "undefined" || obj === null) {
     obj = { "value": {}, "expire":  now + expiry };
   } else if( typeof obj === "object" && typeof obj["value"] === "object") {
     obj["expire"] = now + expiry;
   } else {
     throw "Asssigning property to non-object value"
   }
   obj["value"][property] = value;
   this.localStorage.setItem(key, JSON.stringify(obj));
   return obj;
 },
};


getStorageManager();
})();
