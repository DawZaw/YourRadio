function onBlur() {
    setTimeout(() => {
        document.getElementById('results').classList.add('d-none');
    }, 150);
}

function onFocus() {
    document.getElementById('results').classList.remove('d-none');
}