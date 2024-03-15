document.addEventListener("DOMContentLoaded", function() {
    // Mock player data
    var players = [
        { name: "Player 1" },
        { name: "Player 2" },
        { name: "Player 3" },
        // Add more players as needed
    ];

    // Function to render players
    function renderPlayers() {
        var playersHTML = "";
        players.forEach(function(player) {
            playersHTML += "<div class='player'>" + player.name + "</div>";
        });
        document.getElementById("players").innerHTML = playersHTML;
    }

    // Initial render
    renderPlayers();

    // Example: Adding a new player
    function addPlayer(name) {
        players.push({ name: name });
        renderPlayers();
    }

    // Example: Remove a player
    function removePlayer(index) {
        players.splice(index, 1);
        renderPlayers();
    }

    // Example: Adding a player manually (for testing)
    addPlayer("Player 4");

    // Example: Removing a player manually (for testing)
    setTimeout(function() {
        removePlayer(0);
    }, 5000);
});