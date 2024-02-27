// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
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
// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["AAAAAA", "AAAAAAAAAA", "AAAAAAAAA", "AAAAAAAA", "AAAAAAA", "AAAAAAAA"],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [4215, 5312, 6251, 7841, 9821, 14984],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 15000,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
