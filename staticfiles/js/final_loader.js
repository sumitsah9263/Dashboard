window.setTimeout(function(){

  document.getElementById("loader-text").innerHTML="Calculating..."

}, 5000);

window.setTimeout(function(){

  document.getElementById("loader-text").innerHTML="Generating Report<br>Please wait..."

}, 15000);

window.setTimeout(function(){
  window.location.href="/final"
  document.getElementById("loader-text").innerHTML="Almost done"

}, 20000);


