const homeButton = document.querySelector("button");

homeButton.onclick = () => {
    window.location.href = "/";
}

document.addEventListener('DOMContentLoaded', () => {
    const dashContainer = document.getElementById("bubble-chart");

    // Add a loading spinner inside the dashContainer
    dashContainer.innerHTML = `
        <div class="loading-spinner"></div>
    `;
    
    fetch('/pages/vis-1/bubble')
        .then(response => response.json())
        .then(data => {
            
        setTimeout(() => {
            dashContainer.innerHTML = data.bubble_graph;
            loadScriptsAndExecuteInline(dashContainer);
        }, 2000);

})});

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

function loadScriptsAndExecuteInline(container) {
    const scriptUrls = [];
    const inlineScripts = [];
    const scripts = container.querySelectorAll('script');
    scripts.forEach(script => {
        if (script.src) {
            scriptUrls.push(script.src);
        } else {
            inlineScripts.push(script.textContent);
        }
        script.remove();
    });

    return loadScripts(scriptUrls)
        .then(() => {
            inlineScripts.forEach(inlineScript => {
                const scriptElement = document.createElement('script');
                scriptElement.textContent = inlineScript;
                document.body.appendChild(scriptElement);
            });
        })
        .catch(error => console.error('Error loading external scripts:', error));
}

