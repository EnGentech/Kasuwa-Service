document.addEventListener("DOMContentLoaded", function () {
    // Retrieve product information elements
    const addToCartButton = document.getElementById("add-to-cart-button");
    const productNameElement = document.getElementById("prod_name");
    const productDescriptionElement = document.getElementById("prod_des");
    const productPriceElement = document.getElementById("prod_price");
    const productStockElement = document.getElementById("prod_stock");
    const productTypeElement = document.getElementById("prod_type");
    // const productIdElement = document.getElementById("product_id");
    // const productCategoryElement = document.getElementById("product_category_id");
    // const productUserElement = document.getElementById("product_user_id");
    const productImageElement = document.getElementById("prod_image");

    // Check if all the necessary elements exist on the page
    if (addToCartButton && productNameElement && productDescriptionElement && productPriceElement && productStockElement && productTypeElement && productImageElement) {
        // Extract the product information
        addToCartButton.addEventListener("click", function() {
        const productID = addToCartButton.getAttribute("data-product-id");
        const productName = productNameElement.textContent.trim();
        const productType = productTypeElement.textContent.trim();
        const productDescription = productDescriptionElement.textContent.trim();
        const productStock = productStockElement.textContent.trim();
        const productPrice = productPriceElement.textContent.trim();
        const productImage = productImageElement.textContent.trim();

        // Create a dictionary (object) with the product data
        productData = {
            name: productName,
            type: productType,
            description: productDescription,
            stock: productStock,
            price: productPrice,
            id: productID,
            image: productImage
        };
         // Convert the product data to JSON format
         const productDataJSON = JSON.stringify(productData);

         console.log(productDataJSON)
         // Encode the product data as a query parameter
         const encodedProductData = encodeURIComponent(productDataJSON);

         // Construct the URL for the cart page and include the encoded product data as a query parameter
         const cartURL = `/cart?product_id=${encodedProductData}`;

         // Redirect the user to the shopping cart page
         window.location.href = cartURL;
    });
}

});
