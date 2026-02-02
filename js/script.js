document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Simple smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Marquee Cloning for infinite loop (simple JS fallback/enhancement)
    const marquees = document.querySelectorAll('.marquee-content');
    marquees.forEach(marquee => {
        const content = marquee.innerHTML;
        // Duplicate content 4 times to ensure enough length for big screens
        marquee.innerHTML = content + content + content + content;
    });
});
