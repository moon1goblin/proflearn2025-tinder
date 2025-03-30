document.querySelector("h1").textContent = "Привет мир!";

const regButton = document.querySelector(".create-account");

function registrationClicked() {
  console.log("clicked");
  const regDialog = document.querySelector("#account-dialog");
  regDialog.showModal();
}

regButton.addEventListener("click", registrationClicked);

async function getProfiles() {
  const response = await fetch("https://api.profcomff.com/rating/lecturer");
  console.log(response);

  const data = await response.json();

  console.log(data.lecturers);

  data.lecturers.forEach(renderProfileCard);
}

function renderProfileCard(profile) {
  const card = document.createElement("div");
  card.className = "profile";
  card.dataset.id = profile.id;
  card.innerHTML = `
      <h3>${profile.first_name} ${profile.last_name}</h3>
    `;
  card.addEventListener("click", () => openProfile(profile.id));
  document.body.appendChild(card);
}

getProfiles();
