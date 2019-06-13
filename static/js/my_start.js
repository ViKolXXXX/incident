document.body.onload = function () {


    check_message();


};

function check_message() {
    mes = $("#message").text();
    if (mes == "1") {
        $('#accessdenied-modal').modal('show').on("shown", function () {
            window.setTimeout(function () {
                $("#accessdenied-modal").modal("hide");
            }, 5000);
        });
    }
}
