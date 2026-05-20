const name = document.getElementById("name");
const desc = document.getElementById("desc");
const price = document.getElementById("price");
const image = document.getElementById("image");
const category = document.getElementById("category");
const rating = document.getElementById("rating");

const darkMode = document.getElementById("darkMode");
const priceRange = document.getElementById("priceRange");
const priceVal = document.getElementById("priceVal");

let manageMode = false;
let selectedCategory = "all";

let adminPassword = localStorage.getItem("adminPass") || "1234";

let foods = JSON.parse(localStorage.getItem("foods")) || [
  {
    id: 1,
    name: "Margherita",
    desc: "Klasična pizza",
    price: 8,
    category: "pizza",
    rating: 4,
    image:
      "https://images.unsplash.com/photo-1604382355076-af4b0eb60143"
  },
  {
    id: 2,
    name: "Burger",
    desc: "Sočen burger",
    price: 7,
    category: "burger",
    rating: 5,
    image:
      "https://images.unsplash.com/photo-1550547660-d9450f859349"
  },
  {
    id: 3,
    name: "Coca Cola",
    desc: "Osvežilna pijača",
    price: 3,
    category: "pijača",
    rating: 3,
    image:
      "https://images.unsplash.com/photo-1581636625402-29b2a704ef13"
  },
  {
    id: 5,
    name: "Pomfri",
    desc: "Pomfri, topel, slan",
    price: 5,
    category: "ocvrto",
    rating: 4,
    image:
      "https://images.24ur.com/media/images/953x459/Aug2024/426df81d32ef074c5d60_63275834.jpg?v=f468&fop=fp:0.47:0.54"
  },
  {
    id: 6,
    name: "Špageti po bolonjsko",
    desc: "Špageti po bolonjsko z baziliko",
    price: 10,
    category: "testenine",
    rating: 5,
    image:
      "https://images.24ur.com/media/images/1024x576/Mar2011/60643049.jpg?v=ba85"
  }
];

let cart = JSON.parse(localStorage.getItem("cart")) || [];

/* =========================
   LOCAL STORAGE
========================= */

function saveFoods() {
  localStorage.setItem("foods", JSON.stringify(foods));
}

function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

/* =========================
   TOAST
========================= */

function showToast(text) {
  const toast = document.createElement("div");

  toast.className = "toast";

  toast.innerText = text;

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.remove();
  }, 2500);
}

/* =========================
   ADMIN
========================= */

function enterManageMode() {
  const pass = prompt("Vnesi geslo:");

  if (pass === null) return;

  if (pass === adminPassword) {
    manageMode = true;

    document.getElementById("addBtn").style.display =
      "inline-block";

    document.getElementById("manageToggleBtn").style.display =
      "inline-block";

    document.getElementById("adminSettings").style.display =
      "block";

    renderMenu();

    showToast("Urejanje je vklopljeno 🔓");
  } else {
    showToast("Napačno geslo ❌");
  }
}

function toggleManageMode() {
  manageMode = false;

  document.getElementById("addBtn").style.display = "none";

  document.getElementById("manageToggleBtn").style.display =
    "none";

  document.getElementById("adminSettings").style.display =
    "none";

  renderMenu();

  showToast("Urejanje je izklopljeno");
}

function changePassword() {
  const newPass = document
    .getElementById("newAdminPass")
    .value.trim();

  if (!newPass) {
    showToast("Vnesi novo geslo");
    return;
  }

  adminPassword = newPass;

  localStorage.setItem("adminPass", adminPassword);

  document.getElementById("newAdminPass").value = "";

  showToast("Geslo shranjeno ✅");
}

/* =========================
   PANELS
========================= */

function toggleAddPanel() {
  document
    .getElementById("addPanel")
    .classList.toggle("open");
}

function toggleCartPanel() {
  document
    .getElementById("cartPanel")
    .classList.toggle("open");
}

function toggleSettingsPanel() {
  document
    .getElementById("settingsPanel")
    .classList.toggle("open");
}

/* =========================
   STARS
========================= */

function stars(r) {
  return "⭐".repeat(r) + "☆".repeat(5 - r);
}

/* =========================
   CATEGORY
========================= */

function setCategory(event, cat) {
  event.preventDefault();

  selectedCategory = cat;

  document
    .querySelectorAll(".menu-nav a")
    .forEach((a) => {
      a.classList.remove("active");
    });

  event.target.classList.add("active");

  renderMenu();
}

/* =========================
   ADD FOOD
========================= */

function addFood() {
  const n = name.value.trim();

  const d = desc.value.trim();

  const p = parseFloat(price.value);

  const r = parseInt(rating.value) || 3;

  if (!n || isNaN(p) || p <= 0) {
    showToast("Napaka pri vnosu");
    return;
  }

  foods.push({
    id: Date.now(),
    name: n,
    desc: d,
    price: p,
    category: category.value,
    image:
      image.value ||
      "https://via.placeholder.com/300x200",
    rating: r
  });

  saveFoods();

  console.log(foods);
  renderMenu();

  toggleAddPanel();

  name.value = "";
  desc.value = "";
  price.value = "";
  image.value = "";

  showToast("Jed dodana 🍔");
}

/* =========================
   EDIT / DELETE
========================= */

function editFood(id) {
  let f = foods.find((x) => x.id === id);

  name.value = f.name;
  desc.value = f.desc;
  price.value = f.price;
  image.value = f.image;
  category.value = f.category;
  rating.value = f.rating;

  foods = foods.filter((x) => x.id !== id);

  saveFoods();

  renderMenu();

  toggleAddPanel();

  showToast("Urejanje jedi");
}

function deleteFood(id) {
  foods = foods.filter((f) => f.id !== id);

  saveFoods();

  renderMenu();

  showToast("Jed izbrisana 🗑️");
}

/* =========================
   RENDER MENU
========================= */

function renderMenu() {
  const menu = document.getElementById("menu");

  menu.innerHTML = "";

  const search = document
    .getElementById("search")
    .value.toLowerCase();

  const cat = selectedCategory;

  const maxPrice = Number(priceRange.value);

  priceVal.innerText = maxPrice;

  foods
    .filter(
      (f) =>
        f.name.toLowerCase().includes(search) &&
        (cat === "all" || f.category === cat) &&
        f.price <= maxPrice
    )
    .forEach((food) => {
      const div = document.createElement("div");

      div.className = "card";

      div.innerHTML = `
        <img loading="lazy" src="${food.image}">

        <div class="card-body">

          <h3>${food.name}</h3>

          <p class="desc">${food.desc || ""}</p>

          <p>${stars(food.rating)}</p>

          <p><strong>${food.price} €</strong></p>

          <div class="btn-row">

            <button class="add"
              onclick="addToCart(${food.id})">
              Dodaj
            </button>

            ${
              manageMode
                ? `
                <button class="edit-btn"
                  onclick="editFood(${food.id})">
                  Uredi
                </button>

                <button class="remove-btn"
                  onclick="deleteFood(${food.id})">
                  Izbriši
                </button>
              `
                : ""
            }

          </div>

        </div>
      `;

      menu.appendChild(div);
    });
}

/* =========================
   CART
========================= */

function addToCart(id) {
  let item = cart.find((x) => x.id === id);

  if (item) {
    item.qty++;
  } else {
    cart.push({
      id,
      qty: 1
    });
  }

  saveCart();

  renderCart();

  updateCartCount();

  showToast("Dodano v košarico 🛒");
}

function removeFromCart(id) {
  cart = cart.filter((x) => x.id !== id);

  renderCart();

  updateCartCount();

  saveCart();
}

/* ===== PLUS ===== */

function increaseQty(id) {
  let item = cart.find((x) => x.id === id);

  if (item) {
    item.qty++;
  }

  saveCart();

  renderCart();

  updateCartCount();
}

/* ===== MINUS ===== */

function decreaseQty(id) {
  let item = cart.find((x) => x.id === id);

  if (!item) return;

  item.qty--;

  if (item.qty <= 0) {
    cart = cart.filter((x) => x.id !== id);
  }

  saveCart();

  renderCart();

  updateCartCount();
}

function renderCart() {
  const c = document.getElementById("cart");

  c.innerHTML = "";

  let total = 0;

  cart.forEach((i) => {
    let f = foods.find((x) => x.id === i.id);

    if (!f) return;

    total += f.price * i.qty;

    const div = document.createElement("div");

    div.innerHTML = `
      <span>
        ${f.name} x${i.qty}
        =
        ${(f.price * i.qty).toFixed(2)} €
      </span>

      <div style="display:flex; gap:5px;">

        <button onclick="increaseQty(${i.id})">
          +
        </button>

        <button class="remove"
          onclick="removeFromCart(${i.id})">
          ❌
        </button>

        <button onclick="decreaseQty(${i.id})">
          -
        </button>

      </div>
    `;

    c.appendChild(div);
  });

  document.getElementById("total").innerText =
    "Skupaj: " + total.toFixed(2) + " €";

  saveCart();
}

function updateCartCount() {
  let count = 0;

  cart.forEach((i) => {
    count += i.qty;
  });

  document.getElementById("cartCount").innerText =
    count;
}

/* =========================
   ORDER
========================= */

function order() {
  if (cart.length === 0) {
    showToast("Košarica je prazna");
    return;
  }

  showToast("Naročilo poslano 🍔");

  cart = [];

  renderCart();

  updateCartCount();

  saveCart();
}

/* =========================
   DARK MODE
========================= */

darkMode.addEventListener("change", () => {
  document.body.classList.toggle("dark");

  localStorage.setItem(
    "darkMode",
    document.body.classList.contains("dark")
  );
});

if (localStorage.getItem("darkMode") === "true") {
  document.body.classList.add("dark");

  darkMode.checked = true;
}

/* =========================
   EXPORT / IMPORT JSON
========================= */

function exportJSON() {
  const blob = new Blob(
    [JSON.stringify(foods, null, 2)],
    {
      type: "application/json"
    }
  );

  const a = document.createElement("a");

  a.href = URL.createObjectURL(blob);

  a.download = "restavracija.json";

  a.click();

  showToast("JSON izvožen");
}

function importJSON(e) {
  const file = e.target.files[0];

  if (!file) return;

  const reader = new FileReader();

  reader.onload = function (ev) {
    try {
      foods = JSON.parse(ev.target.result);

      saveFoods();

      renderMenu();

      showToast("JSON uvožen ✅");
    } catch (err) {
      showToast("Napaka pri JSON");
    }
  };

  reader.readAsText(file);
}

/* =========================
   EVENTS
========================= */

priceRange.addEventListener("input", renderMenu);

document
  .getElementById("search")
  .addEventListener("input", renderMenu);

/* =========================
   INIT
========================= */

renderMenu();

renderCart();

updateCartCount();