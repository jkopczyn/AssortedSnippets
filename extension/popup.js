//Array.prototype.forEach.call(
//  document.scripts, 
//  function(script) {console.log(script);}
//);
//
//element.getAttribute("src")
//element.hasAttribute("async")
(function(){

//  var WalkMeExtensionData = document.WalkMeExtensionData = {
//    "host": undefined,
//    "userID": undefined,
//    "env": undefined,
//    "https": undefined,
//    "async": undefined,
//    "found": undefined,
//  }
  var host, userID, env, https, async
  var found = false;
  var breaker = false;
  var d = document;

  document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.getSelected(null, function(tab) {
      var doc = document;
      Array.prototype.forEach.call(
        doc.scripts,
        function(script) { 
          if(!breaker && script.hasAttribute("src")) { 
            fragments = script.getAttribute("src").split('/');
            hostSplit = fragments.length > 2 ? fragments[2].split(".") : [];
            if(hostSplit[1]+"."+hostSplit[2] === "walkme.com") {
              found = true;
              host = fragments[2];
              console.log(fragments[3]+" should be 'users'");
              userID = fragments[4];
              if (fragments.length === 7) {
                env = fragments[5];
                scriptname = fragments[6];
              } else {
                env = 'production';
                scriptname = fragments[7];
              }
              script_parts = scriptname.split("_");
              if (script_parts[0] === "walkme" && script_parts[1].length >= 32 && 
                  script_parts[1].slice(-3) !== ".js" && 
                    script_parts[2].slice(-3) === ".js") {
                https = true;
              } else {
                https = false;
              }
              async = script.hasAttribute("async");
            }
          }
        }
      );

      var details = d.getElementById("details");
      if(found) {
        d.getElementById("title").insertAdjacentHTML(
          "beforeend", 
          " - WalkMeEnabled"
        );
        details.innerHTML = "Details:<br />"+
          "User Id - "+userID+"<br />"+
          "Env - "+env+"<br />"+
          "Is Https - "+https+"<br />"+
          "Host - "+host+"<br />"+
          "async - "+async+""
      }
    });
  });
})();
