
function rendenriza_total_area(url){
    fetch(url, {
        method: 'get',  
    }).then(function(result){
        return result.json()

    }).then(function(data){
        document.getElementById('area_total').innerHTML = data.total
    })
}

function rendenriza_total_arable_area(url){
    fetch(url, {
        method: 'get',  
    }).then(function(result){
        return result.json()

    }).then(function(data){
        document.getElementById('area_arable_total').innerHTML = data.total
    })
}

function rendenriza_total_vegetation_area(url){
    fetch(url, {
        method: 'get',  
    }).then(function(result){
        return result.json()

    }).then(function(data){
        document.getElementById('area_vegetation_total').innerHTML = data.total
    })
}

function rendenriza_total_prod(url){
    fetch(url, {
        method: 'get',  
    }).then(function(result){
        return result.json()

    }).then(function(data){
        document.getElementById('prod_total').innerHTML = data.total
    })
}

function gera_cor(qtd=1) {
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;

        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2} )`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1} )`)
    }

    return [bg_color, border_color]
}


function renderiza_state_dash(url) {

    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('state_pie').getContext('2d');
        var cores_states = gera_cor(qtd=26)
        const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Estados',
                data: data.data,
                backgroundColor: ['#232020', '#887880', '#88A096', '#BBAB8B', '#E8C547', '#97D2FB', '#2A7F62','#9DFFF9','#006989', '#A30000', '#623CEA', '#45B69C', '#F26419', '#E2FDFF', '#514663' ],
                borderColor: ['#232020', '#887880', '#88A096', '#BBAB8B', '#E8C547', '#97D2FB', '#2A7F62','#9DFFF9','#006989', '#A30000', '#623CEA', '#45B69C', '#F26419', '#E2FDFF', '#514663' ],
                borderWidth: 1
            }]
            
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
}

    })

       
    
    });

    }


    function renderiza_areas_ag_vg_dash(url) {

        fetch(url, {
            method: 'get',
        }).then(function(result) {
            return result.json()
        }).then(function(data){
            const ctx = document.getElementById('ag_ac_pie').getContext('2d');
            var cores_states = gera_cor(qtd=26)
            const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Área Agricultável', 'Área de Vegetação'],
                datasets: [{
                    label: 'TESTE',
                    data: [data.total_agric,data.total_veget],
                    backgroundColor: ['#E1CE7A', '#254441'],
                    borderColor: ['#E1CE7A', '#254441'],
                    borderWidth: 1
                }]
                
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
    }
    
        })
    
           
        
        });
    
        }
    
    
        function renderiza_culturas(url) {

            fetch(url, {
                method: 'get',
            }).then(function(result) {
                return result.json()
            }).then(function(data){
                const ctx = document.getElementById('culture_bars').getContext('2d');
                var cores_states = gera_cor(qtd=26)
                const myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Culturas de Plantil',
                        data: data.data,
                        backgroundColor: ['#2A7F62','#9DFFF9','#006989', '#A30000', '#623CEA', '#45B69C', '#F26419', '#E2FDFF', '#514663', '#A30000', '#623CEA', '#45B69C', '#F26419', '#E2FDFF', '#514663' ],
                        borderColor: ['#2A7F62','#9DFFF9','#006989', '#A30000', '#623CEA', '#45B69C', '#F26419', '#E2FDFF', '#514663', '#A30000', '#623CEA', '#45B69C', '#F26419', '#E2FDFF', '#514663' ],
                        borderWidth: 1
                    }]
                    
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
        }
        
            })
        
               
            
            });
        
            }