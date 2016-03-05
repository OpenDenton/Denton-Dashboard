function violations (data) { 
    $('#demo').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Total Code Violations'
        },
        xAxis: {
            categories: ['Date']
        },
        yAxis: {
            title: {
                text: 'Code Violations'
            }
        },
        series: [{
            name: 'Jane',
            data: [1, 5, 4]
        }, {
            name: 'John',
            data: [5, 7, 3]
        }]
    });
});

$(document).ready(function() {
 $.ajax({
    url: 'https://sheetsu.com/apis/v1.0/41293eb6/?fields=Year,Month,TotalViolations',
    type: 'GET',
    async: true,
    dataType: "json",
    success: function (data) {
        violations(data);
    }
  });
 });