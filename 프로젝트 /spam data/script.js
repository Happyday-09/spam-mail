function checkspam() {
    const emailContent = document.getElementById('address-input').value; // 이메일 입력 가져오기
    $.ajax({
        url: '/predict', // 서버 요청
        type: 'POST', // 요청 타입
        contentType: 'application/json', // 데이터 타입 설정
        data: JSON.stringify({ message: emailContent }), // 데이터 전송
        success: function(response) {
            let spamStatus = response.spam ? "스팸 메일입니다." : "정상 메일입니다.";
            document.getElementById('result').innerText = spamStatus; // 결과 표시
            document.getElementById('result').style.color = "black";
        },
        error: function() {
            document.getElementById('result').innerText = "오류가 발생했습니다."; // 오류 메시지
            document.getElementById('result').style.color = "red";
        }
    });
}