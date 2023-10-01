const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

function drawGame(gameState) {
    // Implement the code to draw the game on the canvas using the gameState
    // You'll need to translate your Python code to JavaScript here
    // ...

    // Use setTimeout or requestAnimationFrame to periodically call drawGame
    setTimeout(() => {
        fetch('/get_game_state')
            .then(response => response.json())
            .then(data => {
                drawGame(data);
            });
    }, 100);
}

// Start the game by fetching the initial game state
fetch('/get_game_state')
    .then(response => response.json())
    .then(data => {
        drawGame(data);
    });
