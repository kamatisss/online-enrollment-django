
(function() {
const alerts = document.querySelectorAll('.alert');
alerts.forEach(a => {
    // show animation class
    requestAnimationFrame(() => a.classList.add('alert-show'));

    // close button
    const btn = a.querySelector('.alert-close');
    btn && btn.addEventListener('click', () => {
    a.classList.add('alert-hide');
    setTimeout(() => a.remove(), 260);
    });

    // optional: auto-dismiss non-error messages after 5s
    const tags = a.className;
    if (!/error|danger/.test(tags)) {
    setTimeout(() => {
        if (document.body.contains(a)) {
        a.classList.add('alert-hide');
        setTimeout(() => a.remove(), 260);
        }
    }, 5000);
    }
});
})();

