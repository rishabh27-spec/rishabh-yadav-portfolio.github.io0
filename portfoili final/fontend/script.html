document.querySelectorAll(".card3d").forEach(card => {
  card.addEventListener("mousemove", e => {
    const x = (window.innerWidth / 2 - e.pageX) / 20;
    const y = (window.innerHeight / 2 - e.pageY) / 20;
    card.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
  });

  card.addEventListener("mouseleave", () => {
    card.style.transform = "rotateY(0) rotateX(0)";
  });
});

// Add form submission handling
document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.querySelector("input[type='text']").value;
  const email = document.querySelector("input[type='email']").value;
  const message = document.querySelector("textarea").value;

  const res = await fetch("http://localhost:5000/contact", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, message })
  });

  const data = await res.json();
  alert(data.msg);
});
