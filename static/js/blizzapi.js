$(document).ready(function () {


$.getJSON(
"https://eu.api.battle.net/wow/guild/Twisting%20Nether/Undivine?fields=members&locale=en_GB&apikey=e5prqn7xpeweekdvx4jzebzfdpcu6gkq",
function(json) {
var out = ""
var i
for(i = 0; i < json.members.length; i++) {
    out += json.members[i].character.name + " " + json.members[i].character.level + "<br>" +
    '<img src="http://render-api-eu.worldofwarcraft.com/static-render/eu/' + json.members[i].character.thumbnail + '">' + "<br>"
}

document.getElementById("roster").innerHTML = out
;});


//END OF JS
});