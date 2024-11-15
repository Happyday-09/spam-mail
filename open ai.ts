import { Configuration, OpenAIApi } from "openai";
import * as readlineSync from "readline-sync";

// OpenAI API 설정
const configuration = new Configuration({
    apiKey: 'YOUR_API_KEY', // 자신의 OpenAI API 키를 입력하세요
});
const openai = new OpenAIApi(configuration);

// 사용자와 대화하는 함수
async function chat() {
    console.log("대화 시작! '종료'를 입력하면 대화가 종료됩니다.");
    
    while (true) {
        const userInput = readlineSync.question("당신: ");
        
        if (userInput.toLowerCase() === "종료") {
            console.log("대화를 종료합니다.");
            break;
        }

        try {
            const response = await openai.createChatCompletion({
                model: "gpt-3.5-turbo",
                messages: [{ role: "user", content: userInput }],
            });

            const botReply = response.data.choices[0].message?.content;
            console.log("AI: " + botReply);
        } catch (error) {
            console.error("오류 발생:", error);
        }
    }
}

// 대화 시작
chat();

