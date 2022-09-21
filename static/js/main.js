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

// product change script
var productimage=document.getElementById('product-page-image')
            var productchange= document.getElementsByClassName("choti-images")
            productchange[0].onclick=function(){
                productimage.src=productchange[0].src
            }
            productchange[1].onclick=function(){
                productimage.src=productchange[1].src
            }
            productchange[2].onclick=function(){
                productimage.src=productchange[2].src
            }
            productchange[3].onclick=function(){
                productimage.src=productchange[3].src
            }