from django.shortcuts import redirect


def login_skip(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper