function onBlur() {
    setTimeout(() => {
        document.getElementById('results').classList.add('d-none');
    }, 150);
}

function onFocus() {
    document.getElementById('results').classList.remove('d-none');
}

function countText() {
    let text = document.getElementById('comment-text').value;
    document.getElementById('current').innerText = text.length;
}

$("comment-text").keypress(function (e) {
    if(e.which === 13 && !e.shiftKey) {
        e.preventDefault();
    
        $(this).closest("form").submit();
    }
});