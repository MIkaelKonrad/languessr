var Languages = {
    "Germanic": ["English","Swedish","German","Dutch","Danish","Yiddish"],
    "Romance": ["Spanish","Italian","French"],
    "Slavic": ["Russian","Polish","Czech","Serbo-Croatian"],
    "Other": ["Basque","Georgian"]
    }
window.onload = function(){
    var lang = document.getElementById('lang');
    var fam = document.getElementById('fam');
    for (var x in Languages) {
        fam.options[fam.options.length] = new Option(x, x);
        }
    fam.onchange = function(){
        lang.length=1;
        var z = Languages[this.value];
        for (var i = 0; i < z.length; i++) {
            lang.options[lang.options.length] = new Option(z[i], z[i]);
            }
        }
}