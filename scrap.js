// Import ZIP library
var script = document.createElement("script");
script.src = "https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js";
script.onload = function () {
    console.log("JSZip cargado exitosamente");
    scrapImages();
};
document.head.appendChild(script);

// Constants
const MONTHS = {
  January: "01", February: "02", March: "03",
  April: "04", May: "05", June: "06",
  July: "07", August: "08", September: "09",
  October: "10", November: "11", December: "12",
};

const DATE_LIMIT = "2023_12_30";

const MAIN_ELEMENT_SELECTOR = "#__next > div > main > div > div.grid.lg\\:gap-y-8.gap-y-4.lg\\:mt-8.mt-4 > div.relative"
const DATE_ELEMENT_SELECTOR = "div.absolute p span.text-4xl"
const YEAR_ELEMENT_SELECTOR = "div.absolute p span.text-3xl"
const IMAGES_SELECTOR = "img[src^='blob:']";

function scrapImages() {
  const zip = new JSZip();
  const elements = [...document.querySelectorAll(MAIN_ELEMENT_SELECTOR)];
  processElements(zip, elements);
}

function formatDate(dateString) {
  const parts = dateString.split(" ");

  const year = parts[2];
  const month = MONTHS[parts[0]];
  const day = parts[1].padStart(2, "0");

  return `${year}_${month}_${day}`;
}

function addImageToZip(zip, url, filename) {
  return fetch(url)
      .then((response) => response.blob())
      .then((blob) => zip.file(filename, blob));
}

async function processElements(zip, elements) {
  let lastDate = null;
  let lastDateCount = 0;

  for (const div of elements) {
      const dateElement = div.querySelector(DATE_ELEMENT_SELECTOR);
      const yearElement = div.querySelector(YEAR_ELEMENT_SELECTOR);

      if (dateElement && yearElement) {
          const dateText = `${dateElement.textContent} ${yearElement.textContent}`;
          const formattedDate = formatDate(dateText);

          if (formattedDate === DATE_LIMIT) {
              console.log(`Se alcanzó la fecha límite (${DATE_LIMIT})`);
              break;
          }

          console.log(`Procesando fecha: ${formattedDate}`);

          // Obtener las imágenes
          const imgs = div.querySelectorAll(IMAGES_SELECTOR);

          if (imgs.length >= 2) {
              const backImg = imgs[0].src;
              const frontImg = imgs[1].src;

              // Verificar si la fecha es la misma que la anterior
              if (formattedDate === lastDate) {
                  lastDateCount++;
              } else {
                  lastDateCount = 0;
              }

              const backImgFilename = `${formattedDate}_back_${lastDateCount}.png`;
              const frontImgFilename = `${formattedDate}_front_${lastDateCount}.png`;

              // Agregar imágenes al ZIP
              await addImageToZip(zip, backImg, backImgFilename);
              await addImageToZip(zip, frontImg, frontImgFilename);

              lastDate = formattedDate;
          } else {
              console.warn(`No se encontraron suficientes imágenes para la fecha: ${formattedDate}`);
          }
      } else {
          console.warn("No se encontró la fecha en el elemento");
      }
  }

  zip.generateAsync({ type: "blob" }).then((content) => {
      const link = document.createElement("a");
      link.href = URL.createObjectURL(content);
      link.download = "images.zip";
      link.click();
  });
}