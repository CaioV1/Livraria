function abrirModal(){

    const modal = document.getElementById("modal_visualizar");

    modal.style.display = "block";

}

function fecharModal(){

    const modal = document.getElementById("modal_visualizar");

    modal.style.display = "none";

}

window.onclick = function(event){

    if(event.target == document.getElementById("modal_visualizar")){

        fecharModal();

    }

}
