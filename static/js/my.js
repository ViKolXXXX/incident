document.body.onload = function () {
    setTimeout(function () {
        var preloader = document.getElementById('page-preloader');
        if (!preloader.classList.contains('done')) {
            preloader.classList.add('done');
        }

    }, 70);
    active_link_menu();
    check_message();
    message();

};
function message() {
    message_text = $("#message").text();
    message_tags = $("#message").attr("data-tags");
    switch (message_tags) {
        case 'success':  // if (x === 'value1')
            $.notify(message_text, "success");
            break;
        case 'info':
            $.notify(message_text, "info");
            break;
        case 'warning':
            $.notify(message_text, "warn");
            break;
        case 'error':
            $.notify(message_text, "error");
            break;
        default:
            break;
    }
};
// Активная ссылка на пункт менюmy.js
function active_link_menu() {
    name_title = document.title;
    switch (name_title) {
        case 'Журнал':
            $('#journal').addClass('active');
            break;
        case 'Событие':
            $('#event').addClass('active');
            break;
        case 'Оперативная обстановка':
            $('#operationalenv').addClass('active');
            break;
        case 'Лицо':
            $('#face').addClass('active');
            break;
        case 'О программе':
            $('#about').addClass('active');
            break;

    }
}

//Кнопка скрыть показать меню
$("#menu-toggle").click(function (e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
    if ($("#wrapper").hasClass("toggled")) {
        $("#menu-toggle").fadeOut(350, function () {
            $("#menu-toggle").html("<i class=\"fas fa-times\"></i> &nbsp;&nbsp;Скрыть меню").fadeIn(350);
        })
    } else {
        $("#menu-toggle").fadeOut(350, function () {
            $("#menu-toggle").html("<i class=\"fas fa-bars\"></i> &nbsp;&nbsp;Показать меню").fadeIn(350);
        })


    }

});

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


// preloader в процентах
// var
//     images = document.images,
//     images_total_count = images.length,
//     images_loaded_count = 0,
//     perc_display = document.getElementById('load_perc'),
//     preloader = document.getElementById('page-preloader');
//
// for (var i = 0; i < images_total_count; i++) {
//     image_clone = new Image();
//     image_clone.onload = image_loaded;
//     image_clone.onerror = image_loaded;
//     image_clone.src = images[i].src;
// }
// console.log(images_total_count);
// console.log(images_loaded_count);
//
// function image_loaded() {
//     images_loaded_count++;
//     perc_display.innerHTML = (((100 / images_total_count) * images_loaded_count) << 0) + '%';
//
//
//     if (images_loaded_count >= images_total_count) {
//         setTimeout(function () {
//
//             if (!preloader.classList.contains('done')) {
//                 preloader.classList.add('done');
//             }
//
//         }, 100);
//     }
// }

