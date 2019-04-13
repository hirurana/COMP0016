
	function getNews() {
		//
		$.getJSON("/external_data/dailycoffeenews_with_sentiment.json", function(json) {
			$('#jsonTable').css("visibility", "visible").css("border", "1px solid green");
			$('#jsonTable').append("<tbody>");
			for (var counter = 0; counter < json.length; counter++) {
				$('#jsonTable').append("<tr><td>" + json[counter].title + "</td></tr>");
			}
			$('#jsonTable').append("</tbody>");
			$('th').css("border", "1px solid green");
		});
	}
