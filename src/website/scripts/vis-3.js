const homeButton = document.querySelector("button");

homeButton.onclick = () => {
    window.location.href = "/"
}


document.addEventListener('DOMContentLoaded', () => {
    fetch('/pages/vis-3/tournament')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const dashContainer = document.getElementById("tournament-chart");
            dashContainer.innerHTML = data.tournament_graph;

            // Extract script URLs and inline scripts
            const scriptUrls = [];
            const inlineScripts = [];
            const scripts = dashContainer.querySelectorAll('script');
            scripts.forEach(script => {
                if (script.src) {
                    scriptUrls.push(script.src);
                } else {
                    inlineScripts.push(script.textContent);
                }
                script.remove(); // Remove the script element after extracting the content
            });

            // Load external scripts
            loadScripts(scriptUrls)
                .then(() => {
                    // Execute inline scripts after external scripts are loaded
                    inlineScripts.forEach(inlineScript => {
                        const scriptElement = document.createElement('script');
                        scriptElement.textContent = inlineScript;
                        document.body.appendChild(scriptElement);
                    });
                })
                .catch(error => console.error('Error loading external scripts:', error));
        })
        .catch(error => console.error('Error fetching bubble chart:', error));
});

function loadScripts(urls) {
    return Promise.all(
        urls.map(url => {
            return new Promise((resolve, reject) => {
                const script = document.createElement('script');
                script.src = url;
                script.onload = resolve;
                script.onerror = reject;
                document.head.appendChild(script);
            });
        })
    );
}
