<script src="amcharts/plugins/dataloader/dataloader.min.js" type="text/javascript"></script>
var chart = AmCharts.makeChart("chartdiv", {
    "type": "stock",
    ...
    "dataSets": [{
      "title": "MSFT",
        "fieldMappings": [{
          "fromField": "Open",
          "toField": "open"
        }, {
          "fromField": "High",
          "toField": "high"
        }, {
          "fromField": "Low",
          "toField": "low"
        }, {
          "fromField": "Close",
          "toField": "close"
        }, {
          "fromField": "Volume",
          "toField": "volume"
        }],
        "compared": false,
        "categoryField": "Date",
        "dataLoader": {
          "url": "AAPL.json",
          "format": "json",
          "showCurtain": true,
          "showErrors": true,
          "async": true,
          "reverse": true,
          "useColumnNames": true
        }
      }
    }]
  });