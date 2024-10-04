
fetch("/pistonOrdre.json")
.then(response => response.json)
.then(data => showInfo(data))

function showInfo(data) {
    console.table(data.Eleves)
}


//Selectionner les cases du tableau

//const Line = Array.from(document.querySelectorAll(".LINE"))

//console.log(Line[0].childNodes)

