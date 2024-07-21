$(document).ready(function() {
    $('#check-button').on('click', function() {
      const email = $('#address-input').val();
  
      $.ajax({
        url: '/predict',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ message: email }),
        success: function(response) {
          const spamStatus = response.spam ? '스팸 메일입니다.' : '정상 메일입니다.';
          $('#result').text(spamStatus);
        },
        error: function() {
          $('#result').text('오류가 발생했습니다.');
        }
      });
    });
  });
  