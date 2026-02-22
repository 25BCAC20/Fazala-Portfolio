// SPA Navigation
function showSection(id) {
    document.querySelectorAll(".section").forEach(sec => 
        sec.classList.remove("active")
    );
    document.getElementById(id).classList.add("active");
}

// Contact Form Submission
document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const feedback = document.getElementById("contactFeedback");

    fetch("/contact", {   // ✅ FIXED HERE
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            message: document.getElementById("message").value
        })
    })
    .then(res => res.json())
    .then(data => {
        feedback.style.display = "block";
        feedback.style.color = "green";
        feedback.textContent = "Message saved to database successfully!";
        document.getElementById("contactForm").reset();
    })
    .catch(err => {
        feedback.style.display = "block";
        feedback.style.color = "red";
        feedback.textContent = "Error saving message!";
        console.error(err);
    });
});