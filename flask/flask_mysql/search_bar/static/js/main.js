$(document).ready(function(){
  $('#username').keyup(function(){
 
    var data = $('#regForm').serialize()
    $.ajax({
      method: 'POST',
      url: '/username',
      data: data
    })
    .done(function(res){
      $('#usernameMsg').html(res)
      event.preventDefault()
    })
    return false
  })

  $('#name').keyup(function(){
 
    var data = $('#ser').serialize()
    $.ajax({
      method: 'GET',
      url: '/usersearch',
      data: data
    })
    .done(function(res){
      $('#output').html(res)
      event.preventDefault()
    })
    return false
  })

})
