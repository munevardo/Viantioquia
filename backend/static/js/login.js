window.fbAsyncInit = function(){
	FB.init({
		appId: '489145764524341',
		xfbml: true,
		version: 'v2.0'
	});
};


(function(d, s, id){
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) {return;}
	js = d.createElement(s); js.id = id;
	js.src = "http://connect.facebook.net/es_CO/sdk.js";
	js.src = "http://connect.facebook.net/es_CO/sdk/debug.js";
	fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
