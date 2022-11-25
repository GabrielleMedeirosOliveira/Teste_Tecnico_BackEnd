const body = document.querySelector("body");

const inputFile = document.getElementById("uploadFile");
const btn = document.getElementById("btn");

inputFile.addEventListener("change", (e) => {
  archiveName = e.target.value.replace("C:\\fakepath\\", "");

  const span = document.getElementById("fileName");
  span.innerText = archiveName !== "" ? archiveName : "Nenhum arquivo escolhido";

  if (archiveName !== "") {
    btn.removeAttribute("disabled");
    btn.classList.add("hover");
    btn.style.cursor = "pointer";
  } else {
    btn.setAttribute("disabled", true);
    btn.classList.remove("hover");
    btn.style.cursor = "not-allowed";
  }
});