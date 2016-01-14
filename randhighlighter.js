(function(){
    // loadScript lets us load jQuery without violating Gmail's Content Security Policy
    function loadScript(url, callback) {
        var req = new XMLHttpRequest();
        req.open("GET", url, true);
        req.onreadystatechange = function () {
            if (req.readyState != 4 || req.status != 200) { return; }

            // Taken from jquery source.  Ensures code is evaluated in global scope
            var script = document.createElement( "script" );
            script.text = req.responseText;
            document.head.appendChild(script).parentNode.removeChild(script);

            if(callback) { callback(); }
        };
        req.send();
    }

    function choose_an_email(){
        var messages = jQuery(".xW.xY:visible").parent();
        var chosenIndexes = [];
        for(var i = 0; i < 3 || i >= messages.length ;) {
                var candidate = Math.floor(Math.random()*messages.length);
                if (chosenIndexes.indexOf(candidate) == -1) {
                        i+= 1;
                        chosenIndexes.push(candidate);
                }
        };
        chosenIndexes.forEach(function(chosenIndex) {
                var el = jQuery(messages[chosenIndex]);
                el.css("background-color","#3a8bf7");
                el.find(".yW,,.y6,.xW.xY").css("color", "#fff").css("font-weight", "bold");
                el.find(".y2").css("color", "#d4e1ff").css("font-weight","normal");        
        })
    }

    if (document.location.toString().indexOf("mail.google.com") == -1){
        alert("Click on this bookmarklet when you are viewing your Gmail Inbox.");
    }
    else if (typeof jQuery == "undefined"){
        loadScript('https://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js');

        function wait_for_jquery()
        {
            if (typeof jQuery == "undefined")
            {
                setTimeout(wait_for_jquery, 500);
            }
            else
            {
                choose_an_email();
            }
        }

        wait_for_jquery();
    }
    else{
        choose_an_email();
    }
})();

