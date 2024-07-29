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
          // 새로운 창을 열어 결과를 표시
          const resultWindow = window.open('','_blank');
          resultWindow.document.write('<h1>결과</h1><p>${spamStatus}</p>');
        },
        error: function() {
          const resultWindow = window.open('', '_blank');
          resultWindow.document.write('<h1>오류</h1><p>오류가 발생했습니다.')
        }
      });
    });
  });
  