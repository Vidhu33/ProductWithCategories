# ProductWithCategories
Welcome to the ProductWithCategories wiki!

ProductWithCategories is a basic app created with the help of Django to play around with APIs for a model called Product which has categories and subcategories.

## Models :

1. Category:
   ```
   Fields : category_name , id
   Description : Stores store name of all categories.
   ```
2. Sub Category:
   ```
   Fields : sub_category_name, category, id
   Description : Stores the name of Sub Category and category linked to a Sub Category
   ```
3. Product :
   ```
   Fields : Product_name, sub_category, id
   Description : Stores the name of Product and sub category linked to Product

   ```

## APIs: 

1. GET API to get all category
```python
   endpoint : http://localhost:8000/category/
   response : {
    "CategoryList": [
        {
            "id": 1,
            "category_name": "Electronics"
        },
        {
            "id": 2,
            "category_name": "Sports"
        }
    ]
}
```

2. GET API to get subcategories for a category by passing the sub category name in the url  
```python
    endpoint : http://localhost:8000/sub_category/?category__category_name={category_name}
    sample_request : http://localhost:8000/sub_category/?category__category_name=Electronics
    response : 
    "results": [
        {
            "id": 1,
            "category_name": "Electronics",
            "sub_category_name": "Mobile",
            "category": 1
        },
        {
            "id": 2,
            "category_name": "Electronics",
            "sub_category_name": "Laptop",
            "category": 1
        }
    ]
}
```

3.  GET API to get all products for a category
```python
    endpoint : http://localhost:8000/product/?category={category_name}
    sample_request : http://localhost:8000/product/?category=Electronics
    response : 
    "results": [
        {
            "id": 1,
            "sub_category_name": "Mobile",
            "category_name": "Electronics",
            "product_name": "Samsung S9",
            "sub_category": 1
        },
        {
            "id": 4,
            "sub_category_name": "Mobile",
            "category_name": "Electronics",
            "product_name": "iPhoneX",
            "sub_category": 1
        }
    ]
}
```

4.  GET API to get all products for a sub category
```python
    endpoint : http://localhost:8000/product/?sub_category__sub_category_name={sub_category_name}
    sample_request : http://localhost:8000/product/?sub_category__sub_category_name=Laptop
    response : 
    {
    "results": [
        {
            "id": 2,
            "sub_category_name": "Laptop",
            "category_name": "Electronics",
            "product_name": "MacBook Pro",
            "sub_category": 2
        },
        {
            "id": 3,
            "sub_category_name": "Laptop",
            "category_name": "Electronics",
            "product_name": "Dell XPS",
            "sub_category": 2
        }
    ]
```

5. POST API to create a new product under existing subcategory and category.
```python
   endpoint : http://localhost:8000/product/
   body : {
            "product_name":"Gloves",
            "sub_category_name":"Cricket",
            "category_name":"Sports"
         }
   response:
    "results": {
        "id": 29,
        "sub_category_name": "Cricket",
        "category_name": "Sports",
        "product_name": "Bat",
        "sub_category": 4
    }
}
```


  


