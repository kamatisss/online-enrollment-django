function toggleMenu() {
    document.getElementById("menu").classList.toggle("show");
}

const avatarBtn = document.getElementById("avatarBtn");
const avatarDropdown = document.getElementById("avatarDropdown");

if (avatarBtn) {
    avatarBtn.addEventListener("click", () => {
        avatarDropdown.style.display =
            avatarDropdown.style.display === "block" ? "none" : "block";
    });
}


// hide dropdown when clicking outside
document.addEventListener("click", (e) => {
    if (!avatarBtn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.style.display = "none";
    }
});

