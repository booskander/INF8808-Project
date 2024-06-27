const homeButton = document.querySelector("button");

homeButton.onclick = () => {
    window.location.href = "/";
}

document.addEventListener('DOMContentLoaded', () => {
    fetch('/pages/vis-2/field?team=Italy&opposite_team=England')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const dashContainer = document.getElementById("field-chart");
            dashContainer.innerHTML = data.field_graph;
            loadScriptsAndExecuteInline(dashContainer);
        })
        .catch(error => console.error('Error fetching field chart:', error));
    populateDropdowns();
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

    loadScripts(scriptUrls)
        .then(() => {
            inlineScripts.forEach(inlineScript => {
                const scriptElement = document.createElement('script');
                scriptElement.textContent = inlineScript;
                document.body.appendChild(scriptElement);
            });
        })
        .catch(error => console.error('Error loading external scripts:', error));
}

function populateDropdowns() {
    const countryDropdown = document.getElementById('country-dropdown');
    const teamDropdown = document.getElementById('team-dropdown');
    const showFormationButton = document.getElementById('show-formation-button');

    fetch('/data/team')
        .then(response => response.json())
        .then(teams => {
            teams.forEach(team => {
                const option = document.createElement('option');
                option.value = team;
                option.textContent = team;
                countryDropdown.appendChild(option);
            });
            countryDropdown.disabled = false;
        })
        .catch(error => console.error('Error fetching countries:', error));

    countryDropdown.addEventListener('change', () => {
        const selectedCountry = countryDropdown.value;
        fetch(`/data/teams/${selectedCountry}`)
            .then(response => response.json())
            .then(teams => {
                teamDropdown.innerHTML = '';
                teams.forEach(team => {
                    const option = document.createElement('option');
                    option.value = team;
                    option.textContent = team;
                    teamDropdown.appendChild(option);
                });
                teamDropdown.disabled = false;
                checkDropdowns();
            })
            .catch(error => console.error('Error fetching teams:', error));
    });

    teamDropdown.addEventListener('change', checkDropdowns);

    function checkDropdowns() {
        if (countryDropdown.value && teamDropdown.value) {
            showFormationButton.style.display = 'block';
        } else {
            showFormationButton.style.display = 'none';
        }
    }

    showFormationButton.addEventListener('click', () => {
        const selectedCountry = countryDropdown.value;
        const selectedTeam = teamDropdown.value;
        fetch(`/pages/vis-2/field?team=${selectedCountry}&opposite_team=${selectedTeam}`)
            .then(response => response.json())
            .then(data => {
                const dashContainer = document.getElementById("field-chart");
                console.log(data);
                dashContainer.innerHTML = data.field_graph;
                loadScriptsAndExecuteInline(dashContainer);
            })
            .catch(error => console.error('Error generating field chart:', error));
    });
}
