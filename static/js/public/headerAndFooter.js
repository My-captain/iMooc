$(document).ready(
    function () {
        var is_mouse_hover = false;
        $("#login-area-image-container").hover(function () {
            $(".g-user-card").css("visibility", "visible");
        },function () {
            setTimeout(500, function () {
                if (!is_mouse_hover)$(".g-user-card").css("visibility", "hidden");
            });
        });
        $(".g-user-card").hover(function () {
            is_mouse_hover = true;
            $(".g-user-card").css("visibility", "visible");
        },function () {
            is_mouse_hover = false;
            $(".g-user-card").css("visibility", "hidden");
        });
    }
);