form = document.querySelector('#form_add')

total_area =Number(document.querySelector('#id_total_area_hectares').value)
total_arable = Number(document.querySelector('#id_arable_area_hectares').value)
total_vegetation = Number(document.querySelector('#id_vegetation_area_hectares').value)
sum = total_arable + total_vegetation


$("#id_total_area_hectares").keyup(function() {
    total_area =Number(document.querySelector('#id_total_area_hectares').value)
    total_arable = Number(document.querySelector('#id_arable_area_hectares').value)
    total_vegetation = Number(document.querySelector('#id_vegetation_area_hectares').value)
    sum = total_arable + total_vegetation
    console.log(total_area);
    
  
  });

  $("#id_vegetation_area_hectares").keyup(function() {
    total_vegetation = Number(document.querySelector('#id_vegetation_area_hectares').value)
    sum = total_arable + total_vegetation
    
    
  });

  $("#id_arable_area_hectares").keyup(function() {
    total_arable = Number(document.querySelector('#id_arable_area_hectares').value)
    sum = total_arable + total_vegetation
    
  });

  form.addEventListener("submit", (event) =>{
    event.preventDefault();
    if (total_area < sum) {
        alert("ERRO! CAMPO ÁREA TOTAL MENOR DO QUE A SOMA ENTRE A ÁREA AGRCULTÁVEL E A ÁREA DE VEGETAÇÃO ");
    } else {
       form.submit();
       console.log("ok")
    }
})


