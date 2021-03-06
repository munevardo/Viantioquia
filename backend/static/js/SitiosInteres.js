function CerrodelaCruz() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.797057, -75.910919);
  var mapOptions = {
    zoom: 16,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'sendero ecologico'
  });
   
document.getElementById('visor').innerHTML="<p><strong>Cerro de la Cruz</strong></p>     <p>ElFunciona como mirador natural y sendero ecológico. Es un sitio de peregrinación en el mes de mayo y en Semana Santa. En el sendero se hallan las estaciones del vía crucis. Desde allí se puede observar la cabecera municipal, además de los farallones del Citará y gran parte del paisaje de los municipios cercanos.>";    
   
}

//aqui termina la funcion

function ElTablazo() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.800964, -75.926840);
  var mapOptions = {
    zoom: 14,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Sendero Ecológico El Tablazo'
  });
   
document.getElementById('visor').innerHTML="<p><strong>Sendero Ecológico El Tablazo<strong></p>     <p>      el sendero ecológico el tablazo, es un sendero en madera y piedra construido por los habitantes de la vereda y que conduce al río Pedral en donde se pueden encontrar algunos balnearios naturales y un espacio apropiado para la diversión familiar.   </p>"   
   
}

//aqui termina la funcion

function MiradorelLlanete() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.792585, -75.875316);
  var mapOptions = {
    zoom: 13,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Alto Mirador el Llanete'
  });
   
document.getElementById('visor').innerHTML="<p><strong>Alto Mirador el Llanete</strong></p>     <p>Mirador natural, de donde se observa la troncal del Suroeste, la cabecera Municipal y los municipios de Betania, Concordia,	el corregimiento de San Gregorio (Ciudad Bolívar), los majestuosos farallones del citará y los chorros de Tapartó. En el sitio existe una escuela, cancha polideportiva y caseta comunal.</p>";    
   
}

//aqui termina la funcion

function MiradornaturalElSilencio() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.800618, -75.886225);
  var mapOptions = {
    zoom: 14,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Sendero Ecológico El Tablazo'
  });
   
document.getElementById('visor').innerHTML="<p><strong> Mirador natural El Silencio  <strong></p>   <p>  Balcón natural para el observatorio de diversas especies de aves tales como el sinsonte (mimus polyglottos), el toche (icterus nigrogularis), entre muchos otros y varias especies de flora silvestre, con cercanía a varias fincas de servicios turísticos, desde allí se puede tener una panorámica de los farallones del Citará, del área urbana del municipio y sus alrededores.  </p>";    
   
}

//aqui termina la funcion

function MiradornaturalMinaVieja() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.766610, -75.911406);
  var mapOptions = {
    zoom: 13,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Mirador natural Mina Vieja'
  });
   
document.getElementById('visor').innerHTML="<p><strong> Mirador natural Mina Vieja <strong></p>   <p>  Balcón natural para el observatorio de diversas especies de aves tales como el sinsonte (mimus polyglottos), el toche (icterus nigrogularis), entre muchos otros y varias especies de flora silvestre, con cercanía a varias fincas de servicios turísticos, desde allí se puede tener una panorámica de los farallones del Citará, del área urbana del municipio y sus alrededores.  </p>";    
   
}

//aqui termina la funcion

function PaisajeCafetero() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.804636, -75.912667);
  var mapOptions = {
    zoom: 14,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Paisaje Cafetero'
  });
   
document.getElementById('visor').innerHTML="<p><strong> hgolnfthmnkfymnflkhn    <strong></p><p>" ;    
   
}

//aqui termina la funcion


function initialize() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.799423, -75.907184);
  var mapOptions = {
    zoom: 18,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'parque Saman!'
  });

    document.getElementById("visor").innerHTML="<p><b>Parque Ambiental los Samanes</b></p> <p>Mirador natural, de donde se observa la troncal del Suroeste, la cabecera Municipal y los municipios de Betania, Concordia, el corregimiento de San Gregorio (Ciudad Bolívar), los majestuosos farallones del citará y los chorros de Tapartó. En el sitio existe una escuela, cancha polideportiva y caseta comunal.</p>";
    ;
    
    
}







google.maps.event.addDomListener(window, 'load', initialize);


//aqui termina la funcion

function QuebradaLasJuntas() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.803606, -75.898753);
  var mapOptions = {
    zoom: 15,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Quebrada las Juntas'
  });
   
document.getElementById('visor').innerHTML="<p><strong> Quebrada las Juntas <strong></p>   <p>  Quebrada con algunas partes de su suelo en roca, lo cual permite la formación de varias piscinas naturales, tales como: la tacita de amor, el charco las brujas entre otros. Es utilizada para pescar, para paseos de olla, caminadas ecológicas, entre otras actividades ecoturísticas. Desemboca en el río San Juan.     </p>";    
   
}

//aqui termina la funcion

function QuebradaLosCaciques() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.796839, -75.901864);
  var mapOptions = {
    zoom: 13,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'Quebrada Los Caciques'
  });
   
document.getElementById('visor').innerHTML="<p><strong> Quebrada Los Caciques <strong></p>   <p>  BQuebrada de agua cristalina, con gran parte de su suelo en roca lo cual provoca la formación de varias piscinas naturales en su recorrido, con una prominente vegetación de especies nativas en sus riveras. Desemboca en el río san Juan.  </p>";    
   
}

//aqui termina la funcion

function senderoecologico() {
    
  var PosicionDelSitio = new google.maps.LatLng(5.801063, -75.911775);
  var mapOptions = {
    zoom: 16,
    center: PosicionDelSitio
  }
  var map = new google.maps.Map(document.getElementById('map-samanes'), mapOptions);

  var marker = new google.maps.Marker({
      position: PosicionDelSitio,
      map: map,
      title: 'sendero ecologico'
  });
   
document.getElementById('visor').innerHTML="<p><strong>Sendero Ecológico El Tablazo</strong></p>     <p>El sendero ecológico el tablazo, es un sendero en madera y piedra construido por los habitantes de la vereda y que conduce al río Pedral en donde se pueden encontrar algunos balnearios naturales y un espacio apropiado para la diversión familiar.</p>";    
   
}

//aqui termina la funcion

