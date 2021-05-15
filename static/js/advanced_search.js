$(document).ready(function() {
    var max_fields      = 4;
    var wrapper         = $(".container1");
    var add_button      = $(".add_form_field");

    var x = 1;
    $(add_button).click(function(e){
        e.preventDefault();
        if(x < max_fields){
            x++;
            $(wrapper).append('<div class="col"><input type="text" name="mytext[]"/><a href="#" class="delete">-</a></div>'); //add input box
        }
  else
  {
  alert('Key Words limit is 4')
  }
    });

    $(wrapper).on("click",".delete", function(e){
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});

$(document).ready(function() {
    var max_fields      = 4;
    var wrapper         = $(".container2");
    var add_button      = $(".add_form_field2");

    var x = 1;
    $(add_button).click(function(e){
        e.preventDefault();
        if(x < max_fields){
            x++;
            $(wrapper).append('<div class="col"><input type="text" name="mytext[]"/><a href="#" class="delete">-</a></div>'); //add input box
        }
  else
  {
  alert('Feature Artists limit is 4')
  }
    });

    $(wrapper).on("click",".delete", function(e){
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});