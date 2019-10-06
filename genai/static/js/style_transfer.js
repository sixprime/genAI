function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#user_picture')
                .attr('src', e.target.result)
                .width(400)
                .height(300);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function base64ToBlob(base64, mime) 
{
    mime = mime || '';
    var sliceSize = 1024;
    var byteChars = atob(base64);
    var byteArrays = [];

    for (var offset = 0, len = byteChars.length; offset < len; offset += sliceSize) {
        var slice = byteChars.slice(offset, offset + sliceSize);

        var byteNumbers = new Array(slice.length);
        for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }

        var byteArray = new Uint8Array(byteNumbers);

        byteArrays.push(byteArray);
    }

    return new Blob(byteArrays, {type: mime});
}

var startStyleTransferTask = function () {
    var image = $('#user_picture').attr('src');
    if (image == 'static/img/image_preview.jpg') {
        $('#result').text('Please choose an image first!');
        return
    }

    var base64ImageContent = image.replace(/^data:image\/jpeg;base64,/, "");
    var blob = base64ToBlob(base64ImageContent, 'image/jpeg');
    var formData = new FormData();
    alert(blob)
    formData.append('picture', blob);

    $.ajax({
        url: '/style_transfer',
        type: 'POST',
        cache: false,
        contentType: false,
        processData: false,
        data: formData
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
