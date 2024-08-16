function checkspam() {
    const emailContent = document.getElementById('address-input').value; // value 가져오기
    $.ajax({
        url: '/predict',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ message: emailContent }),
        success: function(response) {
            const spamStatus = response.spam ? '스팸 메일입니다.' : '정상 메일입니다.';
            document.getElementById('result').innerText = spamStatus; // 결과 표시
        },
        error: function() {
            document.getElementById('result').innerText = '오류가 발생했습니다.'; // 오류 메시지
        }
    });
}
