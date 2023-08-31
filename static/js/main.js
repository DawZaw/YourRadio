function onBlur() {
    setTimeout(() => {
        document.getElementById('results').classList.add('d-none');
    }, 100);
}

function onFocus() {
    document.getElementById('results').classList.remove('d-none');
}