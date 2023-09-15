// const productsEl = document.querySelector(".productData");

// function renderProduct(){
//     productData.forEach( (product) => {
//         productsEl.innerHTML += `
//             <div class="product-info-left">
//                         <div class="image-viewer">
//                                     <img id="prod_image" src="{{ product.image_source }}" alt="{{ product.name }}" style="max-width: 100%; max-height: 300px;">
//                         </div>
//                     </div>
//                     <div class="product-info-right">
//                         <div class="product-title_container">
//                             <h1 class="product-title" id="prod_name"> {{ product.name }}</h1>
//                         </div>
//                         <div class="comet-divider comet-divider_small"></div>
//                         <div class="price-banner">
//                             <div class="price-wrapper">
//                                 <div class="price-header">

//                                     <div class="counter-display">
//                                         <div class="saving">
//                                             <span>Spend & Save</span>
//                                         </div>
//                                         <div class="counter">

//                                             <div class="timer">
//                                                 <span>Start:</span>
//                                                 <span class="hour">16</span>
//                                                 <span class="split">:</span>
//                                                 <span class="minute">28</span>
//                                                 <span class="split">:</span>
//                                                 <span class="seconds">40</span>
//                                             </div>
//                                         </div>
//                                     </div>
//                                 </div>
//                                 <div class="price-body">
//                                     <div class="price-text">
//                                         <span>NGN2,295.36 off orders NGN19,128.02+ & NGN6,120....</span>
//                                     </div>
//                                 </div>
//                             </div>
//                         </div>
//                         <div class="main-price">
//                             <span class="common currency">
//                                 NGN
//                             </span>
//                             <span id="prod_price" class="common round-figure">
//                                 {{ product.price }}
//                             </span>
//                             <span class="common float-amount">
//                                 .9
//                             </span>
//                         </div>

//                     </div>
//                 </div>
//                 <div></div>
//                 <div class="comet-divider comet-divider_small"></div>
//                 <section class="description">
//                     <div class="description-title">
//                         <h1 class="title">Description</h1>
//                     </div>

//                     <div id="prod_des" class="product-description">
//                         {{ product.description }}
//                     </div>
//                 </section>
//                 <div class="comet-divider comet-divider_small"></div>
//                 <section class="specification">
//                     <div class="title-wrap">
//                         <div class="title-text">
//                             <h1 class="specification-header">
//                                 Specifications
//                             </h1>
//                         </div>
//                     </div>
//                     <ul class="specification-list">
//                         <li class="specification-line">
//                             <div class="specification-prop">
//                                 <div class="specification-title">
//                                     <span>Power Type</span>
//                                 </div>
//                                 <div class="specification-desc">
//                                     <span id="prod_type" >{{ product.type }}</span>
//                                 </div>
//                             </div>
//                             <div class="specification-prop">
//                                 <div class="specification-title">
//                                     <span>Power Type</span>
//                                 </div>
//                                 <div class="specification-desc">
//                                     <span>{{ product.type }}</span>
//                                 </div>
//                             </div>
//         `
//     });
// }
// renderProduct();

