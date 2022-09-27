const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))


function signupfunc(){
  var signup=document.getElementById("signup");
  var signin=document.getElementById("signin");
  var login_slider= document.getElementById("login-signup-separtor");

  // if(signin.style.display=="block"){
  // signup.style.display="none";

  // }
  signup.style.display="block";
  signin.style.display="none";
}
function signinfunc(){
  var signup=document.getElementById("signup");
  var signin=document.getElementById("signin");
  var login_slider= document.getElementById("login-signup-separtor");
  signup.style.display="none";
  signin.style.display="block";
}