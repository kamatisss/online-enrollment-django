function toggleMore(id) {
    const info = document.getElementById("more-info-" + id);
    const btn = event.target;

    if (info.style.display === "block") {
        info.style.display = "none";
        btn.textContent = "View More";
    } else {
        info.style.display = "block";
        btn.textContent = "View Less";
    }
}
