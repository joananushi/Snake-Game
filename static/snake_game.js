const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

function drawGame(gameState) {

    setTimeout(() => {
        fetch('/get_game_state')
            .then(response => response.json())
            .then(data => {
                drawGame(data);
            });
    }, 100);
}

fetch('/get_game_state')
    .then(response => response.json())
    .then(data => {
        drawGame(data);
    });
