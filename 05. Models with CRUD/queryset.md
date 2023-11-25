# Django Queryset

| Method                   | Example Code                                 | Description                                                                      |
|--------------------------|----------------------------------------------|----------------------------------------------------------------------------------|
| `all`                    | `MyModel.objects.all()`                     | Returns all objects in the QuerySet                                              |
| `filter`                 | `MyModel.objects.filter(field=value)`       | Filters the QuerySet by the specified field and value                            |
| `exclude`                | `MyModel.objects.exclude(field=value)`      | Excludes objects with the specified field and value from the QuerySet            |
| `get`                    | `MyModel.objects.get(field=value)`          | Retrieves a single object matching the specified field and value                 |
| `create`                 | `MyModel.objects.create(field=value)`       | Creates a new object with the specified field and value                          |
| `update`                 | `MyModel.objects.filter(field=value).update(new_field=new_value)` | Updates the objects in the QuerySet with the new field and value  |
| `delete`                 | `MyModel.objects.filter(field=value).delete()` | Deletes the objects in the QuerySet matching the specified field and value       |
| `values`                 | `MyModel.objects.values('field')`           | Returns a QuerySet containing dictionaries with the specified field values       |
| `values_list`            | `MyModel.objects.values_list('field')`      | Returns a QuerySet containing tuples with the specified field values             |
| `order_by`               | `MyModel.objects.order_by('field')`         | Orders the QuerySet by the specified field                                       |
| `distinct`               | `MyModel.objects.distinct()`                | Returns a QuerySet with distinct results based on the specified fields           |
| `count`                  | `MyModel.objects.count()`                   | Returns the number of objects in the QuerySet                                    |
| `first`                  | `MyModel.objects.first()`                   | Retrieves the first object in the QuerySet                                       |
| `last`                   | `MyModel.objects.last()`                    | Retrieves the last object in the QuerySet                                        |
| `exists`                 | `MyModel.objects.filter(field=value).exists()` | Checks if any objects in the QuerySet match the specified field and value        |
| `annotate`               | `MyModel.objects.annotate(total=Sum('field'))` | Adds an annotation to the QuerySet, such as the sum of a field's values          |
| `aggregate`              | `MyModel.objects.aggregate(total=Sum('field'))` | Returns a dictionary with the result of aggregating the specified field values   |
| `prefetch_related`       | `MyModel.objects.prefetch_related('related_field')` | Prefetches related objects, reducing the number of database queries              |
| `select_related`         | `MyModel.objects.select_related('related_field')` | Performs a SQL join and includes related fields in the QuerySet                  |
| `defer`                  | `MyModel.objects.defer('field')`            | Defers the loading of the specified field in the QuerySet                        |
| `only`                   | `MyModel.objects.only('field')`             | Loads only the specified field(s) in the QuerySet                                |
| `reverse`                | `MyModel.objects.reverse()`                 | Reverses the order of the QuerySet                                              |
| `none`                   | `MyModel.objects.none()`                    | Returns an empty QuerySet                                                        |
| `union`                  | `queryset1.union(queryset2)`                | Returns a QuerySet that is the union of two QuerySets                            |

# Here filed list: 
            Document: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#id4
            ----------------------------------------------------------------------------
| `pk`                  | `model.objects.get(pk=api_id, user=request.user)` | ID come from fontend by refering, user is current user two query is working here |
            | `pk` = | `Primary Key` |
            | id = | Identity Like PK |
            | custom_name = | Our created custom variable name |
            | custom_name__startswith = | custom_name is variable |
            | custom_name__istartswith = | custom_name is variable, Case-insensitive starts-with |
            | custom_name__endswith = | |
            | custom_name__iendswith = | Case-insensitive starts-with |
            | custom_name__contains = | custom_name is variable |
            | custom_name__icontains = | Case-insensitive containment test |
            | id__in= | [1, 3, 4] *** it can take multiple or Single id values |
            | custom_name__in = | *** it can take multiple or Single id values |
            | id__gt = | Greater than, lt(less than), lte(Less than or equal to.) thes only work for integer value |
