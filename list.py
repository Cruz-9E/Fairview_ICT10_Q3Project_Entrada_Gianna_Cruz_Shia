from pyscript import document

# List of all players
players = [
    "Jairo Agudo",
    "Naser Al Hazmi", 
    "Mikko Alaiza",
    "Matthew Banaag",
    "Emille Barcelona",
    "Cyrene Brion",
    "Miguel Buo",
    "Lian Castro",
    "Shia Cruz",
    "KC Del Prado",
    "Gianna Entrada",
    "Gavin Francisco",
    "Adrian Gavina",
    "Xylee Goyenechea",
    "Sofia Guevarra",
    "Alexander Janayan",
    "Jabez Libutan",
    "Arabella Lubo",
    "Luisa Manuel",
    "Janine Mariposque",
    "Rycob Pagtalunan",
    "Lucas Reyes",
    "Fateh Singh",
    "Tyronne Subaan",
    "Audrey Tan",
    "Alexandra Vargas",
    "James Zaldivar"
]

def show_players(e):
    # Get the container where the player list will be displayed
    container = document.getElementById("players-container")
    
    # Create HTML for the player list
    html = '<div class="players-list">'
    # Loop through each name in the player list
    for name in players:
        # For each player, create a card div with their name inside
        html += f'<div class="player-card"><p>{name}</p></div>'
    html += '</div>'
    
    # Insert the generated HTML into the page
    container.innerHTML = html