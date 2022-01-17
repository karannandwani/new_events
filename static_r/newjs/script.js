document
    .querySelector("#sidebar-menu > div")
    .addEventListener("click", openSidebar);

document
    .querySelector("#sidebar .sidebar-close")
    .addEventListener("click", closeSidebar);

function openSidebar() {
    document.querySelector("#main").style.width = "80%";
    document.querySelector("#sidebar").style.width = "20%";
    document.getElementById("sidebar-menu").style.display = "none";
}

function closeSidebar() {
    document.querySelector("#main").style.width = "96%";
    document.querySelector("#sidebar").style.width = "0";
    setTimeout(() => {
        document.getElementById("sidebar-menu").style.display = "block";
    }, 500);
}