// Execute the following code when the document is fully loaded and ready
$(document).ready(function () {
  // Function to create subcategories for a parent category
  function createSubcategories(parentCategory, parentLevel) {
    // Get the CSRF token
    var csrfToken = getCSRFToken();
    // Send an AJAX POST request to create subcategories
    $.ajax({
      url: "/create_subcategories/",
      method: "POST",
      data: { category_id: parentCategory },
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (data) {
        // After creating subcategories, retrieve and display them
        $.ajax({
          url: "/get_subcategories/",
          method: "GET",
          data: { category_id: parentCategory },
          success: function (data) {
            // Find the subcategory list associated with the parent category
            var subcategoryList = $(
              `input[value="${parentCategory}"]`
            ).siblings(".subcategory-list");
            // Populate the subcategory list with the retrieved subcategories
            subcategoryList.html(data.subcategories);

            // Add change event listener for the new checkboxes
            subcategoryList.find('input[type="checkbox"]').change(function () {
              var isChecked = $(this).is(":checked");
              var childCategory = $(this).val();
              var childLevel = parentLevel + 1;

              if (isChecked) {
                // Recursively create subcategories for the checked child category
                createSubcategories(childCategory, childLevel);
              } else {
                // Delete subcategories for the unchecked child category
                deleteSubcategories(childCategory);
                // Clear the subcategory list associated with the unchecked category
                $(this).siblings(".subcategory-list").empty();
              }
            });
          },
          error: function (error) {
            console.log(error);
          },
        });
      },
      error: function (error) {
        console.log(error);
      },
    });
  }

  // Function to delete subcategories for a parent category
  function deleteSubcategories(parentCategory) {
    // Get the CSRF token
    var csrfToken = getCSRFToken();
    // Send an AJAX POST request to delete subcategories
    $.ajax({
      url: "/delete_subcategories/",
      method: "POST",
      data: { parent_category_id: parentCategory },
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (data) {
        // Log a success message to the console
        console.log(data.message);
      },
      error: function (error) {
        // Log any errors to the console
        console.log(error);
      },
    });
  }

  // Function to retrieve the CSRF token from the input field
  function getCSRFToken() {
    return $('input[name="csrfmiddlewaretoken"]').val();
  }

  // Add a change event listener for checkboxes within the '#category-tree' element
  $('#category-tree input[type="checkbox"]').change(function () {
    var isChecked = $(this).is(":checked");
    var parentCategory = $(this).val();
    var parentLevel = $(this).data("level");

    if (isChecked) {
      // Create subcategories for the checked parent category
      createSubcategories(parentCategory, parentLevel);
    } else {
      // Delete subcategories for the unchecked parent category
      deleteSubcategories(parentCategory);
      // Clear the subcategory list associated with the unchecked category
      $(this).siblings(".subcategory-list").empty();
    }
  });
});
