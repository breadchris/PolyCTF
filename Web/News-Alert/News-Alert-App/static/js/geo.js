b="YT1hbGVydDthbGVydD1mdW5jdGlvbih4KXthKCJmbGFne2l";
var colors = ["#FF0000", "#FF5A00", "#FFB400", "#FFff00", "#A5ff00", "#4Bff00", "#00ff00", "#00ff5A", "#00ffB4", "#00ffff", "#00B4ff", "#005Aff", "#0000ff", "#4B00ff", "#A500ff", "#FF00ff", "#FF00B4"];b+="0X2lzX2Fsd2F5c19uaWNl";
$(document).ready(function() {

    $(".colorfy").each(function() {
        var colorfy = $(this);
        var chars = []
        var text = colorfy.text();
        for (var i = 0; i < text.length; i++) {
            chars.push(text.charAt(i));
        }
        colorfy.text("");
        $.map(chars, function(c, i) {
            var font = $("<blink><font>"+c+"</font></blink>");
            font.css({"color": colors[i % colors.length]});
            colorfy.append(font);
        });
    });
});
b+="X3RvX2tlZXBfYWwzcnR9Iil9Ow==";eval(atob(b));

