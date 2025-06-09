const speakEL = document.getElementById('speak');
const textEL = document.getElementById('text');
speakEL.addEventListener('click', speakText);
function speakText() {
    const text = textEL.textContent;
    alert(text);
    // stop any speaking in progress
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);

}
