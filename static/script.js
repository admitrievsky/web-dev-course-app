document.addEventListener('DOMContentLoaded', onload);

function onload() {
  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.onclick = () => {
      const productName = button.dataset.productName;
      console.log(`Adding ${productName} to cart`);
    };
  });
}
