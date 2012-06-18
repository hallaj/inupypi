function check_update(request_url, update_id) {
    $.ajax({
        url: request_url,
        success: function(data) {
            $('#'+update_id).html(data);
        }
    });
}
