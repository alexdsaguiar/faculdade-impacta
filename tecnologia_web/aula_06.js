var cursos = ["ADS", "Arquitetura", "Inglês"];
var notas = [
    [9,9.5,10],
    [10,8,7.5],
    [10,10,9.5]
];

console.log(cursos)
console.log("Cursos de: " + cursos)
console.log(notas)


for (var i = 0; i < cursos.length; i++) {
    console.log("Curso: " + cursos[i]);
    var media = 0;
    for (var j = 0; j < notas[i].length; j++) {
        media = media + notas[i][j];
    }
    media = media / 3;
    if (media >=6) {
        console.log("Aprovado!");
    } else {
        console.log("Reprovado!")
    }
}