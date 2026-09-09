// 1. Photo Preview Logic
document.getElementById('photo').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById('imagePreview');
            img.src = e.target.result;
            img.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});

// 2. High Accuracy GPS Logic
document.getElementById('getGpsBtn').addEventListener('click', () => {
    const status = document.getElementById('locationStatus');
    status.innerText = "Fetching location...";

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                status.innerText = `GPS Location Captured: ${lat.toFixed(5)}, ${lng.toFixed(5)}`;
                status.setAttribute('data-lat', lat);
                status.setAttribute('data-lng', lng);
            },
            (error) => {
                status.innerText = "Error getting GPS. Please turn on Location/GPS access.";
            },
            { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
        );
    } else {
        status.innerText = "Geolocation is not supported by your browser.";
    }
});

// 3. Form Submit Logic (Street Name, Area Name, Subject & GPS)
document.getElementById('complaintForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const street = document.getElementById('streetName').value;
    const area = document.getElementById('areaName').value;
    const subject = document.getElementById('subject').value;
    const description = document.getElementById('description').value;

    alert(`Complaint Registered Successfully!\n\nLocation: ${street}, ${area}\nSubject: ${subject}`);
});