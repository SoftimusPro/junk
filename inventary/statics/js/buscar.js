const inputBuscar = document.getElementById('search')
const celdas = document.getElementsByTagName('td')

//buscar
inputBuscar.addEventListener('keyup', e=>{
    let texto = e.target.value
    console.log(texto)
})