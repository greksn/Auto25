function myMap() {
	var mapProp = {
		center: new google.maps.LatLng(58.378248, 26.714834),
		zoom: 17,
	};
	var mapDiv = document.getElementById("googleMap");
	var map = new google.maps.Map(mapDiv, mapProp);
	var marker = new google.maps.Marker({
		position: {
			lat: 58.378248,
			lng: 26.714834
		},
		map: map,
		title: 'Asume siin!'
	});
}
function hideMap() {
    var x = document.getElementById("googleMap");
    var peidaNupp = document.getElementById('peidaNupp');
    if (x.style.display === "none") {
        x.style.display = "block";
        peidaNupp.innerHTML = 'Peida kaart';
    } else {
        x.style.display = "none";
        peidaNupp.innerHTML = 'Kuva kaart';
    }
}