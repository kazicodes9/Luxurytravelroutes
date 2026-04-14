// SIDEBAR (you can keep or remove if not using)
function toggleMenu() {
    let sidebar = document.getElementById("sidebar");
    sidebar.style.left = (sidebar.style.left === "0px") ? "-250px" : "0px";
}

function toggleDropdown() {
    let d = document.getElementById("dropdown");
    d.style.display = (d.style.display === "block") ? "none" : "block";
}

// SLIDER FIXED
let slides = document.querySelectorAll(".slide");
let index = 0;

function showSlides() {
    // remove active from all
    slides.forEach(slide => slide.classList.remove("active"));

    // next slide
    index++;
    if (index > slides.length) {
        index = 1;
    }

    // add active to current
    slides[index - 1].classList.add("active");

    setTimeout(showSlides, 3000);
}

// start slider
showSlides();