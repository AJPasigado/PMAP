function openModal(mode, id) {
    if (mode == 1){
        document.getElementById("modalcontent").innerHTML = 
        " <img class='img-modal' src='/uploads/grayscale/"+id+".png' data-dismiss='modal'>";
    } else {
        document.getElementById("modalcontent").innerHTML = 
        " <img class='img-modal' src='/uploads/colored/"+id+".png' data-dismiss='modal'>";
    }
    $('#exampleModal').modal();    
}

document.getElementById("generate_btn").addEventListener("click", redirect);

function redirect() {
    document.getElementById("generate_btn").innerHTML = "Painting ...";
    window.location.replace("/");
}