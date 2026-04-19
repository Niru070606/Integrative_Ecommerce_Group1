function showHowMany(showWho) {
  if (showWho == "p1") {
    document.getElementById("howMany1").style.display = "flex";
  } else if (showWho == "p2") {
    document.getElementById("howMany2").style.display = "flex";
  } else if (showWho == "p3") {
    document.getElementById("howMany3").style.display = "flex";
  } else if (showWho == "p4") {
    document.getElementById("howMany4").style.display = "flex";
  } else if (showWho == "p5") {
    document.getElementById("howMany5").style.display = "flex";
  } else if (showWho == "p6") {
    document.getElementById("howMany6").style.display = "flex";
  } else if (showWho == "p7") {
    document.getElementById("howMany7").style.display = "flex";
  } else if (showWho == "p8") {
    document.getElementById("howMany8").style.display = "flex";
  } else if (showWho == "p9") {
    document.getElementById("howMany9").style.display = "flex";
  } else if (showWho == "p10") {
    document.getElementById("howMany10").style.display = "flex";
  } else if (showWho == "p11") {
    document.getElementById("howMany11").style.display = "flex";
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
