function showEmail() {
    document.getElementById("emailField").style.display = "block";
    document.getElementById("phoneField").style.display = "none";

    document.getElementById("email").required = true;
    document.getElementById("phone").required = false;
}

function showPhone() {
    document.getElementById("phoneField").style.display = "block";
    document.getElementById("emailField").style.display = "none";

    document.getElementById("phone").required = true;
    document.getElementById("email").required = false;
}

function caregiverLogin() {

    let name = document.querySelector('input[placeholder="Enter your name"]').value;
    let password = document.querySelector('input[type="password"]').value;

    if (name == "") {
        alert("Please enter your name.");
        return;
    }

    let selectedRole = document.querySelector('input[name="loginType"]:checked');

    if (selectedRole == null) {
        alert("Please select Email or Phone Number.");
        return;
    }

    if (selectedRole.value == "email") {

        let email = document.getElementById("email").value;

        if (email == "") {
            alert("Please enter your email.");
            return;
        }
    }

    if (selectedRole.value == "phone") {

        let phone = document.getElementById("phone").value;

        if (phone == "") {
            alert("Please enter your phone number.");
            return;
        }
    }

    if (password == "") {
        alert("Please enter your password.");
        return;
    }

    alert("Caregiver logged in successfully!");
}