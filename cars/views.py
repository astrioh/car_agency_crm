from django.shortcuts import render


def car_all_view(request, *args, **kwargs):
    return render(request, "cars/all.html", status=200)

def car_detailed_view(request, tweet_id, *args, **kwargs):
    return render(request, "cars/detail.html", context={"tweet_id": tweet_id}, status=200)