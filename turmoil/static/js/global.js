if(typeof jQuery !== "undefined") {

    (function($) {

        $('.navigation-item:not(.play), .navigation-item.play span span').pxgradient({
            step: 1,
            colors: ["#F3F3F3", "#565656"],
            dir: "y"
        });

        $('.news-article .text-content .text-header h2, .header-title h2, .small-header h2').pxgradient({
            step: 1,
            colors: ["#d4d4d4", "#7b7b7b"],
            dir: "y"
        });

    })(jQuery);

}

if(typeof Neo !== "undefined") {

    var $ = new Neo({ enable_history: false });
    var sliders = $.select("slider-wrap", "class");

    sliders.each(function(slider) {

        var actions = slider.select("slide-action", "class");
        var slides = slider.select("slide", "class");
        var first = slides.first();
        var offset = 0;

        actions.call("bind", [ "click", function(e) {

            e.preventDefault();

            var target = e.node;
            var index = 0;

            for(; index < actions.size(); index++) {
                if(actions.get(index) == target) {
                    break;
                }
            }

            first.css("margin-left", -(705 * (offset = index))+"px");

            clearInterval(interval);
            interval = setInterval(slide, 5000);

        } ]);

        var interval = setInterval(slide, 5000);

        function slide() {

            if(offset + 1 >= slides.size()) {
                offset = 0;
            } else {
                offset++;
            }

            first.css("margin-left", -(705 * offset)+"px");

        }

    });

    var articles = $.select("news-article", "class");

    articles.call("bind", [ "click", function(e) {

        var target = e.node;

        if(target.hasClass("closed")) {

            e.preventDefault();

            articles.call("addClass", [ "closed" ]);
            target.removeClass("closed");

        }

    } ]);

}