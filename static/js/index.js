fetch('/bags')
  .then(response => response.json())
  .then(data => {
    // داده‌ها را در اینجا پردازش کنید و روی صفحه نمایش دهید
    displayBags(data);
  })
  .catch(error => console.error(error));

function displayBags(bags) {
  const bagsContainer = document.getElementById('bags-container');

  bags.forEach(bag => {
    const bagElement = document.createElement('div');
    bagElement.classList.add('bag');

    const brandElement = document.createElement('h3');
    brandElement.textContent = bag.bag_name;

    const numberElement = document.createElement('p');
    numberElement.textContent = `تعداد کیف ها: ${bag.bag_number}`;

    const priceElement = document.createElement('p');
    priceElement.textContent = `قیمت کیف: ${bag.bag_price} ریال`;

    const typeElement = document.createElement('p');
    typeElement.textContent = `نوع کیف: ${getTypeName(bag.Type)}`;

    bagElement.appendChild(brandElement);
    bagElement.appendChild(numberElement);
    bagElement.appendChild(priceElement);
    bagElement.appendChild(typeElement);

    bagsContainer.appendChild(bagElement);
  });
}

function getTypeName(typeId) {
  const typeNames = ['کیف مدرسه', 'کیف باشگاه', 'کیف پول', 'گیف مسافرتی'];
  return typeNames[typeId - 1];
}