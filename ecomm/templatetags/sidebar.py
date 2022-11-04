from django import template

register = template.Library()



@register.inclusion_tag('sidebar.html')
def get_sidebar_info(products):

    specification_list = set()
    size_list = set()
    color_list = set()
    brand_list = set()
    country_list = set()
    material_list = set()

    for product in products:
        product_specification = product.productspecificationvalue_set.all()
        for spec in product_specification:
            if spec.specification not in specification_list:
                specification_list.add(spec.specification)

            if spec.specification_id == 1:
                size_list.add(spec.value)

            elif spec.specification_id == 2:
                color_list.add(spec.value)

            elif spec.specification_id == 3:
                brand_list.add(spec.value)

            elif spec.specification_id == 4:
                country_list.add(spec.value)

            elif spec.specification_id == 5:
                material_list.add(spec.value)

    return {'specifications': specification_list,
            'colors': color_list,
            'sizes': size_list,
            'brands': brand_list,
            'materials': material_list,
            'countries': country_list,
            'product': product}