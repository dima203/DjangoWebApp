const anim_items = document.querySelectorAll('._anim_items');

if (anim_items.length > 0) {
    window.addEventListener('scroll', anim_on_scroll);
    function anim_on_scroll() {
        for (let index = 0; index < anim_items.length; index++) {
            const anim_item = anim_items[index];
            const anim_item_height = anim_item.offsetHeight;
            const anim_item_offset = offset(anim_item).top;
            const anim_start = 5;

            let anim_item_point = window.innerHeight - anim_item_height / anim_start;
            if (anim_item_height > window.innerHeight) {
                anim_item_point = window.innerHeight - window.innerHeight / anim_start;
            }

            if ((window.scrollY > anim_item_offset - anim_item_point) && window.scrollY < (anim_item_offset + anim_item_height)) {
                anim_item.classList.add('_active');
            } else {
                if (!anim_item.classList.contains('_anim_no_hide')) {
                    anim_item.classList.remove('_active');
                }
            }
        }
    }
    function offset(el) {
        const rect = el.getBoundingClientRect(),
            scroll_left = window.pageXOffset || document.documentElement.scrollLeft,
            scroll_top = window.scrollY || document.documentElement.scrollTop;
        return { left: rect.left + scroll_left, top: rect.top + scroll_top }
    }

    setTimeout(() => {
        anim_on_scroll();
    }, 200);
}