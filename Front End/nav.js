function continueLogin() {

    let selectedRole = document.querySelector('input[name="role"]:checked');

    if (selectedRole == null) {
        alert("Please select an option");
        return;
    }

    if (selectedRole.value == "caregiver") {
        window.location.href = "Caregiver_log_in.html";
    }

    if (selectedRole.value == "player") {
        window.location.href = "Player_log_in.html";
    }
}