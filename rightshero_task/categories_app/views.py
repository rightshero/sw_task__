from django.http import JsonResponse
from django.shortcuts import render
from .models import Category


class CategoryViews():

    # This functions only renders the html template with the parent categories
    # The parent categories are the categories that are created with no parent
    # you can create as many parent categories as you want from the admin panel
    # which is accessible at host/admin/
    #
    # this function is triggered when the api host/category_list/ is called
    @staticmethod
    def category_list(request):
        categories = Category.objects.filter(parent=None)
        return render(request, 'category_list.html', {'categories': categories})

    # this function is called when a checkbox is checked in the template category_list.html
    # it gets the subcategories of the chosen category ( category here is considered the box that is
    # checked not parent categories ) and if the checked box has no subcategories it creates two
    # subcategories and returns them
    # after testing when the category name becomes more than 100 an error is raised, so every 5 SUB
    # are merged together as 'SUB* 5' and as it goes on the number changes to 15, 20, and so on.
    @staticmethod
    def get_subcategories(request):
        try:
            category_id = request.GET.get('category_id')
            subcategories = Category.objects.filter(parent_id=category_id)

            if not subcategories:
                parent_category = Category.objects.get(id=category_id)
                # this counts the depth levels of a subcategory
                levels = parent_category.name.count('SUB ')
                # merge_sub process the str and merge 'SUB'
                merged_name = CategoryViews.merge_sub(parent_category.name, levels)

                merged_name = 'SUB ' + merged_name
                for i in range(2):
                    Category.objects.create(name=merged_name + '-' + str(i + 1), parent=parent_category)

                subcategories = Category.objects.filter(parent_id=category_id)

            data = [{'id': subcat.id, 'name': subcat.name} for subcat in subcategories]
            return JsonResponse(data, safe=False)
        except Exception as err:
            print("err", err)
            return JsonResponse([], safe=False)

    def merge_sub(name, levels):
        # only merge when the depth of a subcategory increases by 5
        if levels == 5:
            # split by space
            parts = name.split(' ')
            merged_parts = []

            try:
                # check if the first element is a number and this indicates that this str has been merged before
                coeff = int(parts[-2])
                # adds 5 to the coeff number
                coeff += 5
            except:
                # if fails then this is the first merge
                coeff = 5

            # merge the
            merged_parts.append(' SUB* ' + str(coeff) + ' ' + parts[-1])

            merged_name = ' '.join(merged_parts)

            return merged_name
        else:
            return name
