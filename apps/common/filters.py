from django.db.models import Q


def apply_search(queryset, request, search_fields):
    search = request.query_params.get("search")

    if not search:
        return queryset

    query = Q()

    for field in search_fields:
        query |= Q(**{f"{field}__icontains": search})

    return queryset.filter(query)


def apply_filters(queryset, request, filter_fields):
    filters = {}

    for field in filter_fields:
        value = request.query_params.get(field)

        if value in (None, ""):
            continue

        # Convert boolean string to Python bool
        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False

        filters[field] = value

    return queryset.filter(**filters)


def apply_ordering(queryset, request, allowed_fields):
    ordering = request.query_params.get("ordering")

    if ordering:
        field = ordering.replace("-", "")

        if field in allowed_fields:
            return queryset.order_by(ordering)

    return queryset