from pyscript import document

# Team names and their corresponding logo images
teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

logos = {
    "Blue Bears": "bears.png",
    "Red Bulldogs": "bulldogs.png",
    "Yellow Tigers": "tigers.png",
    "Green Hornets": "hornets.png",
}

def sign_up(e):
    reg = document.querySelector('input[name="registration"]:checked')
    clearance = document.querySelector('input[name="clearance"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value
    
    output = document.getElementById("output")
    
    # Check registration and clearance status. If the value is not "yes", the user is not eligible.
    if not reg or reg.value != "yes":
        output.innerHTML = "Please register online."
    elif not clearance or clearance.value != "yes":
        output.innerHTML = "Please get medical clearance."
    elif not grade or grade == "":
        output.innerHTML = "Please select your grade."
    elif not section or section == "":
        output.innerHTML = "Please select your section."
    # Check if the grade and section are valid, and not the placeholder.
    
    # If both registration and clearance are met, randomize the team based on grade and section.
    else:
        section_values = {"emerald": 3, "ruby": 1, "sapphire": 0, "topaz": 2, "jade": 4}
        team_index = (int(grade) + section_values[section]) % 4
        team = teams[team_index]
        logo = logos.get(team)
        # Compose result HTML; use a container so layout can be adjusted by CSS
        message = f"<div class=\"result\"><strong>Congratulations! Your team: {team}</strong>"
        if logo:
            message += f"<img src=\"{logo}\" alt=\"{team} logo\" class=\"team-logo\">"
        message += "</div>"
        output.innerHTML = message
    # For example, 10-Emerald would be 10+3 = 13 % 4 = 1
    # This would result into 1-Emerald being placed into Red Bulldogs (as Red Bulldogs is index 1).