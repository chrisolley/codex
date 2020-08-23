$(function() {
    $("#autocomplete").autocomplete({
        source:function(request, response) {
            $.getJSON("/autocomplete", {
                q: request.term, // in flask, "q" will be the argument to look for using request.args
            }, function(data) {
                response(data.matching_results);
            });
        },
        minLength: 2,
        select: function(event, ui) {
            console.log(ui.item);
            this.value = ui.item.label;
            $('#hidden').val('book/' + ui.item.value)
                        .trigger('change');

            return false;
        }
    });
})

$('#hidden').change(function() {
    window.location.href = $('#hidden').val();
});