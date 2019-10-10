function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#user_picture')
                .attr('src', e.target.result)
                .width(640)
                .height(480);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

var startStyleTransferTask = function () {
    var image = $('#user_picture').attr('src');
    if (image == 'static/img/image_preview.jpg') {
        $('#result').text('Please choose an image first!');
        return
    }

    var image = image.replace(/^data:image\/jpeg;base64,/, "");

    $.ajax({
        url: '/style_transfer',
        type: 'POST',
        cache: false,
        processData: false,
        contentType: 'application/json',
        data: image
    })
    .done(function(data) {
        $('#result').text('Task started! Check back in a few minutes!');
    })
    .fail(function() {
        $('#result').text('Wait... Something went wrong...');
    });
};

document.querySelector("#style_transfer").addEventListener("click", function (evt) {
    startStyleTransferTask();
});
