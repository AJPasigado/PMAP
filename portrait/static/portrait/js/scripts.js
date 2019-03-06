function openModal(mode, id) {
    if (mode == 1){
        document.getElementById("modalcontent").innerHTML = 
        " <img class='img-modal' src='/uploads/grayscale/"+id+".png' data-dismiss='modal'>";
    } else {
        document.getElementById("modalcontent").innerHTML = 
        " <img class='img-modal' src='/uploads/colored/"+id+".png' data-dismiss='modal'>";
    }
    $('#exampleModal').modal()
    
  }