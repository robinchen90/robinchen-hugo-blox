---
title: "Conference & Seminar Presentations"
subtitle: "Interactive Map of Academic Presentations"
date: 2024-01-01T00:00:00
draft: false

summary: "Interactive map showing conference presentations and invited seminars by Dr. Zhengyang Chen across North America and Europe."
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<style>
#conference-map {
    height: 500px;
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin: 20px 0;
}
.conference-legend {
    background: white;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px 0;
}
.legend-item {
    display: flex;
    align-items: center;
    margin: 8px 0;
}
.legend-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 10px;
}
.legend-conference { background-color: #e74c3c; }
.legend-seminar { background-color: #3498db; }
.conference-stats {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin: 20px 0;
}
.stat-box {
    text-align: center;
    padding: 15px 25px;
    background: #f8f9fa;
    border-radius: 8px;
    margin: 5px;
}
.stat-number {
    font-size: 2em;
    font-weight: bold;
    color: #2c3e50;
}
.stat-label {
    color: #4B116F;
    font-size: 0.9em;
}
</style>

<div class="conference-stats">
    <div class="stat-box">
        <div class="stat-number">20+</div>
        <div class="stat-label" style="color:#4B116F !important;">Presentations</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">15+</div>
        <div class="stat-label" style="color:#4B116F !important;">Cities</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">3</div>
        <div class="stat-label" style="color:#4B116F !important;">Countries</div>
    </div>
</div>

<div id="conference-map"></div>

<div class="conference-legend">
    <strong>Legend:</strong>
    <div class="legend-item">
        <span class="legend-dot legend-conference"></span>
        <span>Conference Presentations</span>
    </div>
    <div class="legend-item">
        <span class="legend-dot legend-seminar"></span>
        <span>Invited Seminars</span>
    </div>
</div>

<script>
var map = L.map('conference-map').setView([39.8283, -98.5795], 4);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var conferenceIcon = L.divIcon({
    className: 'custom-div-icon',
    html: "<div style='background-color:#e74c3c;width:12px;height:12px;border-radius:50%;border:2px solid white;box-shadow:0 2px 4px rgba(0,0,0,0.3);'></div>",
    iconSize: [12, 12],
    iconAnchor: [6, 6]
});

var seminarIcon = L.divIcon({
    className: 'custom-div-icon',
    html: "<div style='background-color:#3498db;width:12px;height:12px;border-radius:50%;border:2px solid white;box-shadow:0 2px 4px rgba(0,0,0,0.3);'></div>",
    iconSize: [12, 12],
    iconAnchor: [6, 6]
});

var conferences = [
    // 2025-2026
    {lat: 38.6270, lng: -90.1994, name: "Missouri Valley Economic Association (MVEA)", year: "2025-2026", city: "Missouri", type: "conference"},
    {lat: 27.9506, lng: -82.4572, name: "95th Southern Economic Association (SEA) Annual Meeting", year: "2025", city: "Florida", type: "conference"},
    {lat: 26.1420, lng: -81.7948, name: "65th Southern Finance Association (SFA) Annual Meeting", year: "2025", city: "Florida", type: "conference"},

    // 2024-2025
    {lat: 38.7, lng: -90.3, name: "Missouri Valley Economic Association (MVEA)", year: "2024-2025", city: "Missouri", type: "conference"},
    {lat: 38.55, lng: -90.25, name: "89th Midwest Economic Association (MEA) Annual Meeting", year: "2025", city: "Missouri", type: "conference"},

    // 2023-2024
    {lat: 33.7490, lng: -84.3880, name: "Society of Economic Measurement (SEM)", year: "2024", city: "Georgia", type: "conference"},
    {lat: 29.9511, lng: -90.0715, name: "93rd Southern Economic Association (SEA) Annual Meeting", year: "2023", city: "Louisiana", type: "conference"},

    // 2022-2023 Seminars
    {lat: 42.5349, lng: -92.4453, name: "University of Northern Iowa", year: "2022-2023", city: "Iowa", type: "seminar"},
    {lat: 44.9444, lng: -93.1864, name: "University of St. Thomas", year: "2022-2023", city: "Minnesota", type: "seminar"},
    {lat: 41.2565, lng: -95.9345, name: "University of Nebraska at Omaha", year: "2022-2023", city: "Nebraska", type: "seminar"},
    {lat: 40.6084, lng: -75.4902, name: "Muhlenberg College", year: "2022-2023", city: "Pennsylvania", type: "seminar"},
    {lat: 42.2917, lng: -85.5872, name: "Kalamazoo College", year: "2022-2023", city: "Michigan", type: "seminar"},
    {lat: 36.3134, lng: -82.3535, name: "East Tennessee State University", year: "2022-2023", city: "Tennessee", type: "seminar"},
    {lat: 36.2168, lng: -81.6746, name: "Appalachian State University", year: "2022-2023", city: "North Carolina", type: "seminar"},

    // 2022-2023 Conferences
    {lat: 32.7767, lng: -96.7970, name: "Midwest Macroeconomics Meeting Fall 2022", year: "2022", city: "Texas", type: "conference"},
    {lat: 42.2808, lng: -83.7430, name: "Midwest Econometrics Group (MEG) 2022", year: "2022", city: "Michigan", type: "conference"},

    // 2021-2022
    {lat: 45.5051, lng: -122.6750, name: "Western Economic Association International (WEAI)", year: "2022", city: "Oregon", type: "conference"},
    {lat: 51.0447, lng: -114.0719, name: "Society of Economic Measurement (SEM)", year: "2022", city: "Calgary, Canada", type: "conference"},
    {lat: 43.5978, lng: -84.7675, name: "Central Michigan University", year: "2022", city: "Michigan", type: "seminar"},
    {lat: 44.9778, lng: -93.2650, name: "Midwest Economics Association (MEA)", year: "2022", city: "Minnesota", type: "conference"},

    // Prior to PhD
    {lat: 38.5816, lng: -121.4944, name: "California State University Sacramento", year: "2019", city: "California", type: "seminar"},
    {lat: 41.0814, lng: -81.5190, name: "University of Akron", year: "2019", city: "Ohio", type: "seminar"},
    {lat: 32.9886, lng: -96.7479, name: "UT Dallas - Naveen Jindal School of Management", year: "2019", city: "Texas", type: "seminar"},
    {lat: 50.1109, lng: 8.6821, name: "6th Society for Economic Measurement (SEM)", year: "2019", city: "Frankfurt, Germany", type: "conference"},
    {lat: 30.6280, lng: -96.3344, name: "Texas A&M University - Mays Business School", year: "2018", city: "Texas", type: "seminar"},
    {lat: 49.2827, lng: -123.1207, name: "93rd Western Economic Association International (WEAI)", year: "2018", city: "Vancouver, Canada", type: "conference"}
];

conferences.forEach(function(conf) {
    var icon = conf.type === "conference" ? conferenceIcon : seminarIcon;
    var marker = L.marker([conf.lat, conf.lng], {icon: icon}).addTo(map);
    marker.bindPopup("<strong>" + conf.name + "</strong><br>" + conf.city + "<br><em>" + conf.year + "</em>");
});
</script>

---

## Conference Presentations

### 2025-2026
- **Missouri Valley Economic Association (MVEA)** — Missouri, USA
- **95th Southern Economic Association (SEA) Annual Meeting** — Florida, USA
- **65th Southern Finance Association (SFA) Annual Meeting** — Florida, USA

### 2024-2025
- **Missouri Valley Economic Association (MVEA)** — Missouri, USA
- **89th Midwest Economic Association (MEA) Annual Meeting** — Missouri, USA

### 2023-2024
- **Society of Economic Measurement (SEM)** — Georgia, USA
- **93rd Southern Economic Association (SEA) Annual Meeting** — Louisiana, USA

### 2022-2023
- **Midwest Macroeconomics Meeting Fall 2022** — Texas, USA
- **Midwest Econometrics Group (MEG) 2022** — Michigan, USA

### 2021-2022
- **Western Economic Association International (WEAI)** — Oregon, USA
- **Society of Economic Measurement (SEM)** — Calgary, Canada
- **Midwest Economics Association (MEA)** — Minnesota, USA

### Prior to PhD (2018-2020)
- **6th Society for Economic Measurement (SEM)** — Frankfurt, Germany
- **93rd Western Economic Association International (WEAI)** — Vancouver, Canada

---

## Invited Seminars

- University of Northern Iowa, Iowa
- University of St. Thomas, Minnesota
- University of Nebraska at Omaha, Nebraska
- Muhlenberg College, Pennsylvania
- Kalamazoo College, Michigan
- East Tennessee State University, Tennessee
- Appalachian State University, North Carolina
- Central Michigan University, Michigan
- California State University Sacramento, California
- University of Akron, Ohio
- UT Dallas - Naveen Jindal School of Management, Texas
- Texas A&M University - Mays Business School, Texas

---

*Map shows in-person presentations only. Online conferences during 2020-2021 (COVID-19) not displayed.*
