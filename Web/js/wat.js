if (window.addEventListener) {
    var kkeys = [], konami = "38,38,40,40,37,39,37,39,66,65";
	var triggered = false;
    window.addEventListener("keydown", function(e){
        kkeys.push( e.keyCode );
        if ( kkeys.toString().indexOf( konami ) >= 0 ) {
		    if ( triggered == false ) {
				triggered = true;
				kkeys.length = 0;
				soundManager.stopAll();
				$("body").append("<div><video class='centre' id='stormvind' autoplay controls loop width='window.innerWidth' height='window.innerHeight'><source src='stormvind.webm' type='video/webm'></video></div>");
				var video = document.getElementById("stormvind");
			} else if (triggered == true) {
				triggered = false;
				$("#stormvind").remove();
				soundManager.play('omfgdogs');
			}
		}
        while (kkeys.length >= konami.split(',').length) {
            kkeys.shift();
        }
    }, true);
}
