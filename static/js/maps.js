function initMap() {
    const netpark = { lat: 54.6708, lng: -1.4514 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: netpark,
    });
    const marker = new google.maps.Marker({
        position: netpark,
        map: map,
    });
}