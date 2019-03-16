var dataWhole = $.getJSON("/external_data/bloomberg-DF1-Generic-1st-Coffee-Robusta-10-Tonne-random-sentiment.json", function( data ){
    console.log(data);
    // chart definition
    var chart = am4core.create("chartdiv", am4charts.XYChart);
    chart.data = data;

    var title = chart.titles.create();
    title.text = "DU1 Generic 1st Coffee Robusta (10 Tonne)";
    title.fontSize = 40;
    title.fontFamily = "Helvetica Neue"
    title.marginBottom = 30;
    title.align = "center"

    // Axis set up
    chart.dateFormatter.inputDateFormat = "yyyy-MM-dd";
    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.title.text = "Date";
    dateAxis.dataFields.category = "date";

    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.renderer.minWidth = 35;
    valueAxis.title.text = "Date";

    // Line series set up
    var sentimentSeries = chart.series.push(new am4charts.LineSeries());
    sentimentSeries.name = "Sentiment";
    sentimentSeries.dataFields.valueY = "sentiment";
    sentimentSeries.dataFields.dateX = "date";
    sentimentSeries.bullets.push(new am4charts.CircleBullet());
    sentimentSeries.minBulletDistance = 15;
    sentimentSeries.strokeWidth = 2;
    // tooltip
    sentimentSeries.tooltipText = "{sentiment}";
    // Drop-shaped tooltips
    sentimentSeries.tooltip.background.cornerRadius = 20;
    sentimentSeries.tooltip.background.strokeOpacity = 0;
    sentimentSeries.tooltip.pointerOrientation = "vertical";
    sentimentSeries.tooltip.label.minWidth = 40;
    sentimentSeries.tooltip.label.minHeight = 40;
    sentimentSeries.tooltip.label.textAlign = "middle";
    sentimentSeries.tooltip.label.textValign = "middle";

    var open_interest_series = chart.series.push(new am4charts.LineSeries());
    open_interest_series.name = "Open Interest";
    open_interest_series.dataFields.valueY = "open_interest";
    open_interest_series.dataFields.dateX = "date";
    open_interest_series.bullets.push(new am4charts.CircleBullet());
    open_interest_series.minBulletDistance = 15;
    open_interest_series.strokeWidth = 2;
    // tooltip
    open_interest_series.tooltipText = "{open_interest}";
    // Drop-shaped tooltips
    open_interest_series.tooltip.background.cornerRadius = 20;
    open_interest_series.tooltip.background.strokeOpacity = 0;
    open_interest_series.tooltip.pointerOrientation = "vertical";
    open_interest_series.tooltip.label.minWidth = 40;
    open_interest_series.tooltip.label.minHeight = 40;
    open_interest_series.tooltip.label.textAlign = "middle";
    open_interest_series.tooltip.label.textValign = "middle";

    var sma_series = chart.series.push(new am4charts.LineSeries());
    sma_series.name = "SMA (15)";
    sma_series.dataFields.valueY = "simple_15_day_moving_avg";
    sma_series.dataFields.dateX = "date";
    sma_series.bullets.push(new am4charts.CircleBullet());
    sma_series.minBulletDistance = 15;
    sma_series.strokeWidth = 2;
    // tooltip
    sma_series.tooltipText = "{simple_15_day_moving_avg}";
    // Drop-shaped tooltips
    sma_series.tooltip.background.cornerRadius = 20;
    sma_series.tooltip.background.strokeOpacity = 0;
    sma_series.tooltip.pointerOrientation = "vertical";
    sma_series.tooltip.label.minWidth = 40;
    sma_series.tooltip.label.minHeight = 40;
    sma_series.tooltip.label.textAlign = "middle";
    sma_series.tooltip.label.textValign = "middle";

    var last_price_series = chart.series.push(new am4charts.LineSeries());
    last_price_series.name = "Last Price (USD)";
    last_price_series.dataFields.valueY = "last_price_USD";
    last_price_series.dataFields.dateX = "date";
    last_price_series.bullets.push(new am4charts.CircleBullet());
    last_price_series.minBulletDistance = 15;
    last_price_series.strokeWidth = 2;

    // tooltip
    last_price_series.tooltipText = "{last_price_USD}";
    // Drop-shaped tooltips
    last_price_series.tooltip.background.cornerRadius = 20;
    last_price_series.tooltip.background.strokeOpacity = 0;
    last_price_series.tooltip.pointerOrientation = "vertical";
    last_price_series.tooltip.label.minWidth = 40;
    last_price_series.tooltip.label.minHeight = 40;
    last_price_series.tooltip.label.textAlign = "middle";
    last_price_series.tooltip.label.textValign = "middle";

    // Make a panning cursor
    chart.cursor = new am4charts.XYCursor();

    // // scrollbar
    // var scrollbarX = new am4charts.XYChartScrollbar();
    // scrollbarX.series.push(open_interest_series);
    // scrollbarX.series.push(sma_series);
    // scrollbarX.series.push(last_price_series);
    // chart.scrollbarX.parent = chart.bottomAxesContainer;

    // LEGEND
    chart.legend = new am4charts.Legend();
    chart.legend.useDefaultMarker = true;
    var marker = chart.legend.markers.template.children.getIndex(0);
    marker.cornerRadius(12, 12, 12, 12);
    marker.strokeWidth = 2;
    marker.strokeOpacity = 1;
    marker.stroke = am4core.color("#ccc");


});
