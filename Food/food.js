function createChild(parentNode, tag, className) {
  child = document.createElement(tag);
  child.className = className;
  parentNode.appendChild(child);
  return child;
}

function appendText(parentNode, text) {
  parentNode.appendChild(document.createTextNode(text));
}

function addBooth(boothData, dst) {
  div = createChild(dst, 'div');

  h2 = createChild(div, 'h2');
  appendText(h2, boothData.name);

  table = createChild(dst, 'table');
  for (var i = 0; i < boothData.items.length; i++) {
    tr = createChild(table, 'tr');

    tdStars = createChild(tr, 'td', 'stars-uneaten');
    appendText(tdStars, '\u2606\u2606\u2605');

    tdDesc = createChild(tr, 'td', 'desc');
    appendText(tdDesc, boothData.items[i].desc);

    tdNotes = createChild(tr, 'td', 'notes');
    if (boothData.items[i].veg) {
      appendText(tdNotes, 'V');
    }
    if (boothData.items[i].ddp) {
      appendText(tdNotes, 'D');
    }
    if (boothData.items[i].stein) {
      appendText(tdNotes, 'S');
    }
  }
}

for (var i = 0; i < food.length; i++) {
  addBooth(food[i], document.getElementById('food'));
}


