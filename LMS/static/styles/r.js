// Get all sections with class 'collapsible'
const sections = document.querySelectorAll('section');

// Loop through each section and add a click event listener
sections.forEach(section => {
    const header = section.querySelector('h2');
    header.addEventListener('click', () => {
        section.classList.toggle('active');
    });
});