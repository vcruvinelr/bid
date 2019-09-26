function verificouDiario(id){
  console.log(id);
  token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  $.ajax({
    type: 'POST',
    url: '/diarios/verificou-diario/' + id + '/',
    data: {
        csrfmiddlewaretoken: token
    },
    success: function(result){
        console.log(result);
        $("#diarios").text(result.diarios);
        $("#mensagem").text(result.mensagem);
    }

  });
}

function desmarcarDiario(id){
  console.log(id);
  token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  $.ajax({
    type: 'POST',
    url: '/diarios/desmarcou-diario/' + id + '/',
    data: {
        csrfmiddlewaretoken: token
    },
    success: function(result){
        console.log(result);
        $("#diarios01").text(result.diarios01);
        $("#mensagem01").text(result.mensagem01);
    }

  });
}
