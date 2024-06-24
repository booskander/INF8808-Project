const homeButton = document.querySelector("button");

homeButton.onclick = () => {
    window.location.href = "/"
}

document.addEventListener('DOMContentLoaded', () => {
    fetch('/pages/vis-1/bubble')
        .then(response => response.json())
        .then(data => {
            const dashContainer = document.getElementsByClassName("bubble-chart")[0];
            dashContainer.appendChild(data.bubble_graph);
        })
        .catch(error => console.error('Error fetching bubble chart:', error));
});