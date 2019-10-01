function openSlideMenu() {
    document.getElementById('menu').style.width = '50vw';
    document.getElementById('navigation-bar').style.marginLeft = '50vw';
    document.getElementById('menu-toggle').style.display = 'none';
}

function closeSlideMenu() {
    document.getElementById('menu').style.width = '0';
    document.getElementById('navigation-bar').style.marginLeft = '0';
    document.getElementById('menu-toggle').style.display = 'block';
}