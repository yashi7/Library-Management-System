google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
    drawPieChart();
    drawLineChart();
}

function drawPieChart() {
    var data = google.visualization.arrayToDataTable([
        ['Category', 'Number of Books'],
        ['Fiction',  30],
        ['Non-Fiction',  20],
        ['Literature', 15],
        ['Others', 25]
        // Add more categories and data as needed
    ]);

    var options = {
        title: 'Book Categories Distribution',
        is3D: true,
        backgroundColor: 'transparent', // Make the background of the chart transparent
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

function drawLineChart() {
    var data = google.visualization.arrayToDataTable([
        ['Year', 'ISSUED', 'RETURNED'],
        ['2013',  1000,      400],
        ['2014',  1170,      460],
        ['2015',  660,       1120],
        ['2016',  1030,      540],
        ['2017',  1370,      750],
        ['2018',  2000,      200],
        ['2019',  1500,      173],
        ['2020',  1130,      550],
        ['2021',  2150,      750],  
        ['2022',  2260,      1563],
        ['2023',  2330,      650],
    ]);

    var options = {
        title: 'Library Performance',
        curveType: 'function',
        legend: { position: 'bottom' },
        backgroundColor: 'transparent', // Make the background of the chart transparent
    };

    var chart = new google.visualization.LineChart(document.getElementById('line_chart_div'));

    chart.draw(data, options);
}
