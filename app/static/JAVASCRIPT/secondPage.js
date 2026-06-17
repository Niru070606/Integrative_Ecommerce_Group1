function showHowMany(showWho) {
  if (showWho == "1") {
    document.getElementById("1").style.display = "flex";
  } else if (showWho == "2") {
    document.getElementById("2").style.display = "flex";
  } else if (showWho == "3") {
    document.getElementById("3").style.display = "flex";
  } else if (showWho == "4") {
    document.getElementById("4").style.display = "flex";
  } else if (showWho == "5") {
    document.getElementById("5").style.display = "flex";
  } else if (showWho == "6") {
    document.getElementById("6").style.display = "flex";
  } else if (showWho == "7") {
    document.getElementById("7").style.display = "flex";
  } else if (showWho == "8") {
    document.getElementById("8").style.display = "flex";
  } else if (showWho == "9") {
    document.getElementById("9").style.display = "flex";
  } else if (showWho == "10") {
    document.getElementById("10").style.display = "flex";
  } else if (showWho == "11") {
    document.getElementById("11").style.display = "flex";
  }
}

function plus(qtyId) {
  let input = document.getElementById(qtyId);
  let currentValue = parseInt(input.value);
  if (currentValue < 20) {
    input.value = currentValue + 1;
  }
}

function minus(qtyId) {
  let input = document.getElementById(qtyId);
  let currentValue = parseInt(input.value);
  if (currentValue > 1) {
    input.value = currentValue - 1;
  }
}

const targetDate = new Date("May 1, 2026 00:00:00").getTime();

setInterval(function () {
  const now = new Date().getTime();
  const distance = targetDate - now;

  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((distance / 1000 / 60) % 60);
  const seconds = Math.floor((distance / 1000) % 60);

  document.getElementById("timer").innerHTML =
    days + "d " + hours + "h " + minutes + "m " + seconds + "s";
}, 1000);

function foldQuantity(showWho) {
  if (showWho == "1") {
    document.getElementById("1").style.display = "none";
  } else if (showWho == "2") {
    document.getElementById("2").style.display = "none";
  } else if (showWho == "3") {
    document.getElementById("3").style.display = "none";
  } else if (showWho == "4") {
    document.getElementById("4").style.display = "none";
  } else if (showWho == "5") {
    document.getElementById("5").style.display = "none";
  } else if (showWho == "6") {
    document.getElementById("6").style.display = "none";
  } else if (showWho == "7") {
    document.getElementById("7").style.display = "none";
  } else if (showWho == "8") {
    document.getElementById("8").style.display = "none";
  } else if (showWho == "9") {
    document.getElementById("9").style.display = "none";
  } else if (showWho == "10") {
    document.getElementById("10").style.display = "none";
  } else if (showWho == "11") {
    document.getElementById("11").style.display = "none";
  }
}

function login() {
  let un = document.getElementById("username").value;
  let pw = document.getElementById("password").value;
  if (pw == "admin" && un == "admin") {
    window.location.href = "/adminList";
  } else if (pw == "user" && un == "user") {
    window.location.href = "/home";
  } else {
    alert("Wrong Password");
  }
}
