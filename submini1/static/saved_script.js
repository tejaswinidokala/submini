
window.onload = function () {
    const titles = JSON.parse(localStorage.getItem("titles")) || [];
    const contents = JSON.parse(localStorage.getItem("notes")) || [];

    const main = document.getElementById("main-saved");

    for (let i = 0; i < titles.length; i++) {
        const noteDiv = document.createElement("div");
        noteDiv.className = "note";
        noteDiv.innerHTML = `
            <h3 class="saved-title">${titles[i]}</h3>
            <p class="saved-content">${contents[i]}</p>
        `;
        main.appendChild(noteDiv);
    }
};
