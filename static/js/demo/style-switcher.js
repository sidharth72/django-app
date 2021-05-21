


//Password strength check//
$(document).ready(function() { 
  $('#password-reg').keyup(function(){ 
    $('#result').html(checkStrength($('#password-reg').val())); 
    function checkStrength(password){ 
      var strength = 0; 
      if (password.length < 6) { 
        $('#result').removeClass(); 
        $('#result').addClass('short');
        $("#result").css("color","tomato");
        $('#password-reg').css('border-color','tomato');  
        return 'Too short' 
      }if (password.length > 7){ 
        strength += 1
      } 
      if (String(password).match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)){ 
        strength += 1;
      }
      if (String(password).match(/([a-zA-Z])/) && String(password).match(/([0-9])/)){
        strength += 1
      }  
      if (String(password).match(/([!,%,&,@,#,$,^,*,?,_,~])/)){
        strength += 1
      }

      if (String(password).match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,",%,&,@,#,$,^,*,?,_,~])/)){ 
        strength += 1;
      }
      if (strength < 2 ) { 
        $('#result').removeClass();
        $('#result').text('Password is too weak! add symbols , letters and numbers')
        $("#result").css("color","tomato");
        $('#password-reg').css('border-color','tomato'); 
        return 'Password is weak! add symbols , letters and numbers' 
      } else if (strength == 2 ) { 
        $('#result').removeClass() 
        $('#result').text('good')
        $("#result").css("color","orange");
        $('#password-reg').css('border-color','orange');  
        return 'Good' 
      } else{ 
        $('#result').removeClass() 
        $('#result').text('strong') 
        $("#result").css("color","mediumseagreen");
        $('#password-reg').css('border-color','mediumseagreen'); 
        return 'Strong!' 
      }

    } 
  });
  
});


/*Username validation */



  

$(document).ready(function(){

  $('#username-reg').keyup(function(){

    $("#username-reg").submit();


    var name = $("#username-reg").val();
    var patt = /\s/g;
    var res = name.match(patt);

    if(res){

      $('#username-val').text("Username " + "'" +name+ "'" + " not available")
      $("#username-val").css('color','tomato');
      $('#username-val').fadeIn()
      $("#username-reg").css('border-color','tomato')

    }
    else{

      $('#username-val').text("Available")
      $("#username-val").css('color','mediumseagreen')
      $("#username-reg").css('border-color','mediumseagreen')
      

    } 
  })
})


function onClick(){

  var i = document.getElementById('likes_id').value
  $.ajax({
    
      url:'/ajax/likes/',
      data:{'i':i},
      dataType:'json',
      success:function(data){
        document.getElementById('like').innerHTML = data.i

      }
    })
}

$(document).ready(function(){
  $('#sub-btn').click(function(){
    if($('#username-reg').val() && $('#firstname-reg').val() && $('#lastname-reg').val()){   
      $('#sub-btn').text("submitting...")
    }

  });

});

$(document).ready(function(){
  $('.btn-info').click(function(){

      alert('Your comment is awaiting moderation')
      
      

    
  })
})