function r_d(id){
    fetch('http://'+window.location.host+'/documents/downloads/'+id, {
   headers: {
      'Accept': 'application/json',
   }
})
   .then(response => response.json())
   .then(text => document.getElementById('nd').innerText = "Downloads: "+ text.d)
}