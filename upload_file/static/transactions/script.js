let BASE_URL = "http://127.0.0.1:8000";

const body = document.querySelector("body");
const tbody = document.querySelector("tbody");
const tfoter = document.querySelector(".total");

const createTable = async () => {
  const response = await fetch(`${BASE_URL}/api/transactions/`);
  const transactionsData = await response.json();
  const data = transactionsData.data;

  for (let x = 0; x < data.length; x++) {
    const tr = document.createElement("tr");
    const keys = Object.keys(data[x]);
    const values = Object.values(data[x]);

    for (let y = 1; y < keys.length; y++) {
      const td = document.createElement("td");
      td.innerText = values[y];

      tr.appendChild(td);
    }

    tbody.appendChild(tr);
  }
};
createTable();

const backgroundBubbles = () => {
  const container = document.createElement("div");
  const content = document.createElement("div");
  container.classList.add("container");
  content.classList.add("bubbles");

  for (let x = 1; x <= 45; x++) {
    const span = document.createElement("span");
    span.style.setProperty("--i", Math.floor(Math.random() * 45)) + 1;
    content.appendChild(span);
  }
  container.appendChild(content);
  body.appendChild(container);
};
backgroundBubbles();