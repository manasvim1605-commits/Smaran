
// CAREGIVER REGISTRATION
const caregiverRegisterForm =
    document.getElementById("caregiverRegisterForm");

if (caregiverRegisterForm) {

    caregiverRegisterForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const data = {
            name: document.getElementById("name").value,
            phone: document.getElementById("phone").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };

        await sendFormData("/api/caregiver/register", data, "/caregiver-login");
    });
}


// CAREGIVER LOGIN
const caregiverLoginForm =
    document.getElementById("caregiverLoginForm");

if (caregiverLoginForm) {

    caregiverLoginForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const data = {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };

        await sendFormData("/api/caregiver/login", data);
    });
}


// PLAYER REGISTRATION
const playerRegisterForm =
    document.getElementById("playerRegisterForm");

if (playerRegisterForm) {

    playerRegisterForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const data = {
            name: document.getElementById("name").value,
            phone: document.getElementById("phone").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
            caregiver_email: document.getElementById("caregiver_email").value
        };

        await sendFormData("/api/player/register", data, "/player-login");
    });
}


// PLAYER LOGIN
const playerLoginForm =
    document.getElementById("playerLoginForm");

if (playerLoginForm) {

    playerLoginForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const data = {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };

        await sendFormData("/api/player/login", data);
    });
}


// COMMON FUNCTION
async function sendFormData(url, data, successRedirect = null) {

    try {

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            credentials: "same-origin",
            body: JSON.stringify(data)
        });

        const result = await response.json();

        alert(result.message);

        if (response.ok) {

            if (successRedirect) {
                window.location.href = successRedirect;
            }

            else if (result.redirect) {
                window.location.href = result.redirect;
            }
        }

    }

    catch (error) {

        alert("Unable to connect to SMARAN server.");
        console.error(error);

    }
}


// LOGOUT
async function logoutUser() {

    try {

        const response = await fetch("/api/logout", {
            method: "POST",
            credentials: "same-origin"
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.message);
            window.location.href = "/";
        }

    }

    catch (error) {
        alert("Logout failed. Please try again.");
        console.error(error);
    }
}
