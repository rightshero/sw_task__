document.addEventListener("DOMContentLoaded", function () {

    const categoryCheckboxes = document.querySelectorAll('.category');

    categoryCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleCheckboxChange);
    });

    function fetchAndDisplaySubcategories(categoryId, parentElement) {
        fetch(`/categories/get_subcategories/${categoryId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    const ul = document.createElement('ul');
                    parentElement.appendChild(ul);

                    data.forEach(subcategory => {
                        const li = document.createElement('li');
                        const label = document.createElement('label');
                        label.textContent = subcategory.name;
                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.className = 'category';
                        checkbox.value = subcategory.id;
                        label.insertBefore(checkbox, label.firstChild);
                        li.appendChild(label);
                        ul.appendChild(li);
                        checkbox.addEventListener('change', handleCheckboxChange);

                    });
                }
            })
            .catch(error => {
                console.error(error);
            });
    }

    function handleCheckboxChange() {
        const id = this.value;
        const parentElement = this.parentElement.parentElement;
        if (this.checked) {
            fetchAndDisplaySubcategories(id, parentElement);
        } else {
            removeSubcategories(parentElement);
        }
    }

    function removeSubcategories(parentElement) {
        const ul = parentElement.querySelector('ul');
        if (ul) {
            parentElement.removeChild(ul);
        }
    }

});