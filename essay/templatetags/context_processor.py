from essay.models import Essay, Type

def globals_var(request):

    essays = Essay.objects.filter(display=True)
    dates = [obj.ctime.date() for obj in essays]
    date_dict = {}
    for date in dates:
        ym = date.strftime("%Y-%m")
        if date_dict.has_key(ym):
            count = date_dict.get(ym) + 1
            date_dict[ym] = count
        else:
            date_dict.setdefault(ym, 1)

    types = Type.objects.order_by('-rank')

    return dict(date_dict=date_dict, types=types)