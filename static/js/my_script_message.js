// Активная ссылка на пункт менюmy.js
window.onload = function () {
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