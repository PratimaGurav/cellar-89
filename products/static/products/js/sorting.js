/**
 * sorting.js: Javascript file for sorting the results on the products page. 
 */

/*jshint esversion: 6 */
/*globals $:false */


// Script for Back to top button -->
$('.btt-link').click(function(e) {
    window.scrollTo(0,0);
});

//Script for sorting products
$('#sort-selector, #sort-selector-brand').change(function() {
    let selector = $(this);
    let currentUrl = new URL(window.location);

    let selectedVal = selector.val();
    if(selectedVal != "reset"){
        let sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});