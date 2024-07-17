async function checkSpam(){
    const addressInput = document.getElementById('address-Input').value;
    const resultElement = document.getElementById('result');

    try {
        // model load
        const model  = await tf.loadLayerModel('');

        //주소 전처리
        const addressTensor = tf.tensor([addressInput]);

        //spam check
        const prediction = await model.predict(addressTensor);
        const isSpam = prediction.dataSync()[0] > 0.5;

        //result
        resultElement.textContent = isSpam
        ? 'The address is considered spam'
        : 'The address is not considered spam';
    }
    catch (error){
        console.error('Error', error);
        resultElement.textContent = 'Error!! please checking address'
    }
}