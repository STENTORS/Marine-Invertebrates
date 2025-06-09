document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.label').forEach(label => {
    const button = label.querySelector('button');
    if (button) {
      button.addEventListener('click', (e) => {
        e.stopPropagation();
        // Collect all text content inside the label (excluding the button image)
        let text = '';
        // Add h1 text (excluding the button)
        const h1 = label.querySelector('h1');
        if (h1) {
          // Remove button from h1 text
          const h1Clone = h1.cloneNode(true);
          const btn = h1Clone.querySelector('button');
          if (btn) btn.remove();
          text += h1Clone.textContent.trim() + '. ';
        }
        // Add all <p> text
        label.querySelectorAll('p').forEach(p => {
          text += p.textContent.trim() + ' ';
        });
        // Stop any speaking in progress
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text.trim());
        window.speechSynthesis.speak(utterance);
      });
    }
  });
});