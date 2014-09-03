function initialize() {
    
  var PosicionDelParque = new google.maps.LatLng(5.799423, -75.907184);
  var PosicionElTablazo = new google.maps.LatLng(5.800964, -75.926840);
  var PosicionCerrodelaCruz = new google.maps.LatLng(5.797057, -75.910919);
  var PosicionMiradorelLlanete = new google.maps.LatLng(5.792585, -75.875316);
  var PosicionMiradornaturalElSilencio = new google.maps.LatLng(5.800618, -75.886225);
  var PosicionMiradornaturalMinaVieja = new google.maps.LatLng(5.766610, -75.911406);
  var PosicionPaisajeCafetero = new google.maps.LatLng(5.804636, -75.912667);
  var PosicionQuebradaLasJuntas = new google.maps.LatLng(5.803606, -75.898753);
  var PosicionQuebradaLosCaciques = new google.maps.LatLng(5.796839, -75.901864);
  var Posicionsenderoecologico = new google.maps.LatLng(5.801063, -75.911775);
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
      position: PosicionDelParque,
      map: map,
      icon: image,
      title: 'Parque Saman'
  });

  var marker = new google.maps.Marker({
      position: PosicionElTablazo,
      map: map,
      icon: image,
      title: 'El Tablazo'
  });

  var marker = new google.maps.Marker({
      position: PosicionCerrodelaCruz,
      map: map,
      icon: image,
      title:'Cerrode la Cruz'
  });
 
 var marker = new google.maps.Marker({
      position: PosicionMiradorelLlanete,
      map: map,
      icon: image,
      title:'Mirador el Llanete'
  });
    
  var marker = new google.maps.Marker({
      position: PosicionMiradornaturalElSilencio,
      map: map,
      icon: image,
      title:'Mirador Natural El Silencio'
  });

   var marker = new google.maps.Marker({
      position: PosicionMiradornaturalMinaVieja,
      map: map,
      icon: image,
      title:'Mirador natural Mina Vieja'
  });

 var marker = new google.maps.Marker({
      position: PosicionPaisajeCafetero,
      map: map,
      icon: image,
      title:'Paisaje Cafetero'
  });
 
  var marker = new google.maps.Marker({
      position:PosicionQuebradaLasJuntas,
      map: map,
      icon: image,
      title:'Quebrada Las Juntas'
  });

var marker = new google.maps.Marker({
      position:Posicionsenderoecologico,
      map: map,
      icon: image,
      title:'Sendero ecologico'
  });

 
  
}
google.maps.event.addDomListener(window, 'load', initialize);


//aqui termina la funcion