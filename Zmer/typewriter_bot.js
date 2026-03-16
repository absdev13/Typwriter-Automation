(function autoType() {
    console.log("🚀 Auto-Typer gestartet...");

    function sim(char) {
        const c = char.charCodeAt(0);
        const e = { key: char, keyCode: c, which: c, bubbles: true };

        document.dispatchEvent(new KeyboardEvent('keydown', e));
        document.dispatchEvent(new KeyboardEvent('keypress', e));
        
        const inp = document.getElementById('input_area') || document.activeElement;
        if (inp && inp.value !== undefined) {
            inp.value += char;
            inp.dispatchEvent(new Event('input', { bubbles: true }));
        }
        document.dispatchEvent(new KeyboardEvent('keyup', e));
    }

    function typeNext() {
        const box = document.getElementById('text_todo_1');
        if (!box || !box.textContent) return console.log("✅ Fertig!");

        const char = box.textContent.charAt(0).replace(/\u00a0/g, " ");
        let speed = Math.floor(Math.random() * 120 + 180); // 180-300ms
        
        if (Math.random() < 0.008) { // 0.8% mistakes (4 in 500)
            sim(String.fromCharCode(97 + Math.floor(Math.random() * 26)));
            setTimeout(() => { sim(char); step(char, speed); }, Math.random() * 150 + 250);
        } else {
            sim(char);
            step(char, speed);
        }
    }

    function step(char, speed) {
        if (/^[.,!?]$/.test(char)) speed += Math.random() * 200 + 150;
        setTimeout(typeNext, speed);
    }
    
    typeNext();
})();
