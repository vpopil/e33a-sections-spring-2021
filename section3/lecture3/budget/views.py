from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


class NewCategoryForm(forms.Form):
    category = forms.CharField(label="New Category", required=True)
    allowance = forms.IntegerField(
        label="Allowance", min_value=1, max_value=1000)


# Create your views here.
def index(request):

    y = my_function(5)
    y = my_function(5)

    if "categories" not in request.session:
        request.session["categories"] = []

    # comment blah
    y = my_function(5)

    html_string = "<b>Hello Section</b>"

    return render(request, "budget/index.html",
                  {"categories": request.session["categories"],
                   "html_string": html_string})


def my_function(x):
    x *= 2
    return x


def add(request):
    """ this functino does abc... """
    count = 1

    if request.method == "POST":
        # Fetch the form ...
        form = NewCategoryForm(request.POST)

        # Validation form and saving the budget cate
        if form.is_valid():
            category = form.cleaned_data["category"]
            request.session["categories"] += [category]
            count += 1
            return HttpResponseRedirect(reverse("budget:index"))
        return render(request, "budget/add.html", {
            "form": form
        })

    return render(request, "budget/add.html", {
        "form": NewCategoryForm()
    })
