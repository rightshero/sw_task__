document.addEventListener("DOMContentLoaded", () => {
  const categoryContainer = document.querySelector(".category-container");
  const categoryList = document.querySelector(".category-list");

  categoryContainer.addEventListener("change", async (event) => {
    const target = event.target;
    if (target.matches('input[type="checkbox"]')) {
      if (target.checked) {
        // Get the category id
        const categoryId = +target.id.split("-").pop();
        console.log(`categoryId: ${categoryId}`);

        // Send the post request to create the two sub categories
        const subcategories = await createSubcategories(categoryId);
        console.log(subcategories);

        // Add the sub categories to this category
        subcategories.forEach((subcategory) => {
          const subcategoryItemHtml = `
            <li class="category">
              <label for="sub-category-${subcategory.id}">
                ${subcategory.name}
              </label>
              <input
                type="checkbox"
                id="category-${subcategory.id}"
                name="category"
                value="${subcategory.name}"
              />
            </li>
          `;
          categoryList.insertAdjacentHTML("beforeend", subcategoryItemHtml);
        });
      }
    }
  });
});

async function createSubcategories(parentCategoryId) {
  try {
    // Create the data to send in the request
    const requestData = {
      parent_id: parentCategoryId,
    };

    // Send the POST request using the Fetch API
    const response = await fetch("/categories/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestData),
    });

    if (response.status === 201) {
      const data = await response.json();
      // Handle the successful response here
      console.log(data);
      return data.subcategories;
    } else {
      throw new Error("Failed to create subcategories");
    }
  } catch (error) {
    // Handle any errors here
    console.error(error);
  }
}
