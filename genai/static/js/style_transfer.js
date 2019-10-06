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

document.querySelector("#style_transfer").addEventListener("click", function (evt) {
    alert('TODO')
});
