$(document).ready(function(){
	$('#mapa')
		.wrap('<span style="display:inline-block"></span>')
		.css('display', 'block')
		.parent()
		.zoom({
			magnify: 1,
		});
});