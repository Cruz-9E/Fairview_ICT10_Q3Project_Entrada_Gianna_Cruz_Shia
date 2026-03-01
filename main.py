from pyscript import document

# Code for password visibility toggle, just a extra feature I added
def toggle_pass(event):
    pass_field = document.getElementById("pass")
    icon = document.getElementById("eyeIcon")
    
    if pass_field.type == "password":
        pass_field.type = "text"
        icon.classList.remove("fa-eye")
        icon.classList.add("fa-eye-slash")
    else:
        pass_field.type = "password"
        icon.classList.remove("fa-eye-slash")
        icon.classList.add("fa-eye")

def create_account(event):
    username = document.getElementById("user").value
    password = document.getElementById("pass").value
    output = document.getElementById("output")
    
    username_length = len(username)
    password_length = len(password)
    
    # Check if username is valid
    if username_length < 7:
        user_left = 7 - username_length # Show how many characters are left to reach 7
        output.innerHTML = f'<p style="color: red;">Username needs {user_left} more character/s</p>'
        return
    
    # Check if password is valid
    if password_length < 10:
        pass_left = 10 - password_length # Show how many characters are left to reach 10
        output.innerHTML = f'<p style="color: red;">Password needs {pass_left} more character/s</p>'
        return
    
    # Check if password has letter and number using the any() function
    has_letter = any(char.isalpha() for char in password) # If there is at least one letter, this will be True
    has_number = any(char.isdigit() for char in password) # If there is atleast one number, this will be True
    
    if not has_letter or not has_number:
        output.innerHTML = '<p style="color: red;">Password must include at least one letter and one number</p>'
        return
    
    # If everything is valid, show success message
    output.innerHTML = '<p style="color: green;">Account created successfully!</p>'