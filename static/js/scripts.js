/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 
teste = document.getElementById("id_cpforcnpj");
pessoa = document.getElementById("type_pessoa");

teste.addEventListener("keypress", () => {
    let inputlength = teste.value.length
    $('#id_cpforcnpj').mask('000.000.000-00', {reverse: true});

    if (pessoa.value == "PESSOA FÍSICA") {
        $('#id_cpforcnpj').mask('000.000.000-00', {reverse: true});
    } else
        $('#id_cpforcnpj').mask('00.000.000/0000-00', {reverse: true});    
})

function rendereriza_total_area(url){
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json()
    }).then(function(data){
        document.getElementById('teste_area').innerHTML = data.total
    })
}
    


window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
   
}

)





