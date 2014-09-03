function initialize() {
    
  var PosicionDelacicla = new google.maps.LatLng(5.799423, -75.970884);
  var image = ('img/puntero.png');


  var mapOptions = {
    zoom: 13,
    center: PosicionDelParque,
    mapTypeControl: false,
    scaleControl: false,
     zoomControl: false
     
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelacicla,
      map: map,
      icon: image,
      title: 'ciclo ruta'
  });
  
}
google.maps.event.addDomListener(window, 'load', initialize);


//aqui termina la funcion