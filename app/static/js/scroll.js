var content = document.querySelector('#content');


var loadMore = function() {
        $.ajax({
        type: "GET",
        url:"/load_more_books",
        data: "{}",
        dataType: "text",
        success: function( data ) {
            content.innerHTML += data;
        }
        });

}

window.addEventListener('scroll', function() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        loadMore();
    }
})