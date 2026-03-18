// Search history
let searchHistory = JSON.parse(localStorage.getItem('searchHistory')) || [];

// When page loads
window.onload = function() {
    showHistory();

    // If Flask sent data
    if (typeof flaskMovie !== 'undefined') {
        
        // If error — movie not found
        if (flaskError === true) {
            showError(flaskMovie);
        } 
        // If recommendations found
        else if (flaskRecs && flaskRecs.length > 0) {
            showResults(flaskMovie, flaskRecs);
        }
    }
};

// Show results page with movie cards
function showResults(movie, recs) {
    // Save to search history
    if (!searchHistory.includes(movie)) {
        searchHistory.unshift(movie);
        if (searchHistory.length > 5) searchHistory.pop();
        localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
    }

    // Switch pages
    document.getElementById('page-search').style.display = 'none';
    document.getElementById('page-results').style.display = 'block';

    // Set movie name
    document.getElementById('searched-movie').textContent = movie;

    // Build movie cards
    const grid = document.getElementById('cards-grid');
    grid.innerHTML = '';

    recs.forEach(function(title, index) {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <div class="card-icon">🎬</div>
            <div class="card-number">#${index + 1}</div>
            <div class="card-title">${title}</div>
            <div class="card-click-hint">Click for details →</div>
        `;
        card.style.cursor = 'pointer';
        card.onclick = function() {
            window.location.href = '/movie/' + encodeURIComponent(title);
        };
        grid.appendChild(card);
    });
}

// Show error when movie not found
function showError(movie) {
    // Switch pages
    document.getElementById('page-search').style.display = 'none';
    document.getElementById('page-results').style.display = 'block';

    // Set movie name
    document.getElementById('searched-movie').textContent = movie;

    // Show error card
    const grid = document.getElementById('cards-grid');
    grid.innerHTML = `
        <div style="
            grid-column: 1/-1;
            text-align: center;
            padding: 60px 20px;
        ">
            <div style="font-size: 4rem; margin-bottom: 20px;">😕</div>
            <h3 style="color: #e50914; font-size: 1.5rem; margin-bottom: 12px;">
                Movie Not Found!
            </h3>
            <p style="color: #888; font-size: 1rem;">
                We couldn't find "<strong style="color:white">${movie}</strong>" in our database.
            </p>
            <p style="color: #555; font-size: 0.9rem; margin-top: 8px;">
                Please check the spelling or try another movie name.
            </p>
            <button onclick="goBack()" style="
                margin-top: 30px;
                background: #e50914;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 8px;
                font-size: 1rem;
                cursor: pointer;
            ">← Try Again</button>
        </div>
    `;
}

// Go back to search page
function goBack() {
    document.getElementById('page-results').style.display = 'none';
    document.getElementById('page-search').style.display = 'block';
    showHistory();
}

// Show search history tags
function showHistory() {
    searchHistory = JSON.parse(localStorage.getItem('searchHistory')) || [];

    const section = document.getElementById('history-section');
    const tagsContainer = document.getElementById('history-tags');

    if (searchHistory.length === 0) {
        section.style.display = 'none';
        return;
    }

    section.style.display = 'block';
    tagsContainer.innerHTML = '';

    searchHistory.forEach(function(movie) {
        const tag = document.createElement('div');
        tag.className = 'history-tag';
        tag.textContent = movie;
        tag.onclick = function() {
            document.getElementById('movie-input').value = movie;
            document.getElementById('search-form').submit();
        };
        tagsContainer.appendChild(tag);
    });
}