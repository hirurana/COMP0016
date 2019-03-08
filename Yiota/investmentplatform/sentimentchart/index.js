am4core.useTheme(am4themes_animated);

var dataWhole = $.getJSON("/external_data/bloomberg-DF1-Generic-1st-Coffee-Robusta-10-Tonne-random-sentiment.json", function( data ){
    console.log(data);
    // chart definition
    var chart = am4core.create("chartdiv", am4charts.XYChart);
    chart.paddingRight = 50;
    chart.paddingLeft =450;

    chart.data = data;

    var title = chart.titles.create();
    title.text = "Sentiment Analysis";
    title.fontSize = 40;
    title.fontFamily = "Helvetica Neue"
    title.marginBottom = 30;
    title.align = "center"

    // Axis set up
    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.grid.template.location = 0;
    dateAxis.tooltip.disabled = false;
    dateAxis.dataFields.category = "Date";

    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.tooltip.disabled = true;
    valueAxis.renderer.minWidth = 35;

    // Line series set up
    var sentimentSeries = chart.series.push(new am4charts.LineSeries());
    sentimentSeries.name = "Sentiment";
    sentimentSeries.dataFields.dateX = "date";
    sentimentSeries.dataFields.valueY = "value";
    sentimentSeries.tooltipText = "{valueY}";
    sentimentSeries.tooltip.pointerOrientation = "vertical";
    sentimentSeries.tooltip.background.fillOpacity = 0.5;

    var openInterestSeries = chart.series.push(new am4charts.LineSeries());
    openInterestSeries.name = "Open Interest";
    openInterestSeries.dataFields.valueY = "Exports";
    openInterestSeries.dataFields.categoryX = "year";
    openInterestSeries.bullets.push(new am4charts.CircleBullet());
    openInterestSeries.minBulletDistance = 15;

    chart.cursor = new am4charts.XYCursor();
    chart.cursor.snapToSeries = sentimentSeries;
    chart.cursor.xAxis = dateAxis;

    var scrollbarX = new am4charts.XYChartScrollbar();
    scrollbarX.series.push(sentimentSeries);
    chart.scrollbarX = scrollbarX;
});
