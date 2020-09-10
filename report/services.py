from .models import Product, ProductDetail
import requests
from django.db.models import Min, Max, Avg


def fetchData():
    ''' fetch data from petroleum_report api'''
    response = requests.get(
        'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json')
    data = response.json()
    # Product.objects.all().delete()
    # print(data)
    # print(len(data))
    # data_text = response.text
    # print(type(data_text))
    return data


def insertProduct():
    '''insert product name to Products'''
    data = fetchData()
    products = []
    # print(products)
    for item in data:
        if item.get('petroleum_product') not in products:
            products.append(item.get('petroleum_product'))
    print(products)
    for item in products:
        if Product.objects.filter(product_name__iexact=item).count() == 0:
            Product.objects.create(product_name=item)
    # num_of_product_db_objects= len(Product.objects.all())
    # num_of_product = len(products)
    # if  num_of_product != num_of_product_db_objects :
    #     for excess_product in range(num_of_product_db_objects,num_of_product):
    #         Product.objects.create(product_name=products[excess_product]).save()


def insertProductDetail():
    '''insert product year,sale to ProductDetail'''
    data = fetchData()
    # obj= Product.objects.get(product_name='petrol')
    # print(obj)
    # print(type(obj))
    # ProductDetail.objects.create(sales=data[0]['sale'],product=obj, year=int(data[0]['year']))
    for item in data:
        obj = Product.objects.get(
            product_name__iexact=item.get('petroleum_product'))
        if ProductDetail.objects.filter(product=obj).filter(year=int(item.get('year'))).count() == 0:
            ProductDetail.objects.create(sales=item.get(
                'sale'), product=obj, year=int(item.get('year')))


def calcIntervals(initial, final, interval):
    year_diff = (final - initial) + 1
    if year_diff % interval == 0:
        return int(year_diff/interval)
    return int(year_diff/interval) + 1


def queryMin(uppperYear, lowerYear, item):
    minValue = ProductDetail.objects.filter(product__product_name=item).filter(
        year__gte=lowerYear).filter(year__lte=uppperYear).exclude(sales__exact=0).aggregate(Min('sales'))

    if minValue.get('sales__min') == None:
        return 0
    else:
        return minValue.get('sales__min')


def queryMax(uppperYear, lowerYear, item):
    maxValue = ProductDetail.objects.filter(product__product_name=item).filter(
        year__gte=lowerYear).filter(year__lte=uppperYear).exclude(sales__exact=0).aggregate(Max('sales'))

    if maxValue.get('sales__max') == None:
        return 0
    else:
        return maxValue.get('sales__max')


def queryAvg(uppperYear, lowerYear, item):
    avgValue = ProductDetail.objects.filter(product__product_name=item).filter(
        year__gte=lowerYear).filter(year__lte=uppperYear).exclude(sales__exact=0).aggregate(Avg('sales'))

    if avgValue.get('sales__avg') == None:
        return 0
    else:
        return avgValue.get('sales__avg')


def calcMinMaxAvg():
    result = {
        'prod_name': '',
        'year': '',
        'min': 0,
        'max': 0,
        'avg': 0,
    }
    result_list = []
    start_year = ProductDetail.objects.aggregate(Min('year')).get('year__min')
    final_year = ProductDetail.objects.aggregate(Max('year')).get('year__max')
    year_diff = (final_year - start_year) + 1
    interval_period = 5
    product = Product.objects.all()
    # result['prod_name'] = product
    num_of_interval = calcIntervals(start_year, final_year, interval_period)
    for item in product:
        upperYear = final_year
        if year_diff % 5 == 0:
            lowerYear = upperYear - 4
        else:
            lowerYear = upperYear - (year_diff % 5)
        for interval in range(0, num_of_interval):
            copy_of_result = result.copy()
            copy_of_result['prod_name'] = item.product_name
            copy_of_result['year'] = f"{lowerYear}-{upperYear}"

            # print("num of interval: ", interval)
            # print(lowerYear, upperYear)
            minValue = queryMin(upperYear, lowerYear, item)
            copy_of_result['min'] = minValue
            maxValue = queryMax(upperYear, lowerYear, item)
            copy_of_result['max'] = maxValue
            avgValue = queryAvg(upperYear, lowerYear, item)
            copy_of_result['avg'] = avgValue
            upperYear = lowerYear-1
            lowerYear -= 5
            result_list.append(copy_of_result)
    # print(result_list)
    # print(len(result_list))
    return result_list
