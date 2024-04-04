document.addEventListener("DOMContentLoaded", function() {
    const menuIcon = document.querySelector(".menu-icon");
    const menu = document.querySelector(".menu");

    menuIcon.addEventListener("click", function() {
        menu.classList.toggle("hidden");
        positionMenu(); // Вызываем функцию для позиционирования меню
    });

    function positionMenu() {
        const menuRect = menu.getBoundingClientRect(); // Получаем размеры и позицию меню
        const menuIconRect = menuIcon.getBoundingClientRect(); // Получаем размеры и позицию иконки меню

        const topOffset = 10; // Отступ сверху

        menu.style.top = (menuIconRect.top - menuRect.height - topOffset) + "px"; // Позиционируем меню над иконкой
    }
});
