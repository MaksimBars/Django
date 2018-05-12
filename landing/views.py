from django.shortcuts import render_to_response
from landing.models import Home, AboutMe, AboutSite, Feedback


def index(request):
    context = {}

    # Main (Home) section
    section_one = Home.objects.all()
    home = Home.objects.get(title=section_one[0].title)
    main_home = {
        'title': home.title,
        'sub': home.subtitle,
        'tag': home.tagline
    }
    context.update(main_home)

    # Second (About me) section
    section_two = AboutMe.objects.all()
    about_me = AboutMe.objects.get(name=section_two[0].name)
    me = {
        'name': about_me.name,
        'text_about': about_me.text,
        'name_second': about_me.name_second,
        'text_second': about_me.text_second
    }
    context.update(me)

    # Third (About the site) section
    section_three = AboutSite.objects.all()
    about_site = AboutSite.objects.get(title=section_three[0].title)
    site = {
        'title_site': about_site.title,
        'title_text': about_site.text,
        'name_one': about_site.name_one,
        'text_one': about_site.text_one,
        'name_two': about_site.name_two,
        'text_two': about_site.text_two,
        'name_three': about_site.name_three,
        'text_three': about_site.text_three,
        'name_four': about_site.name_four,
        'text_four': about_site.text_four
    }
    context.update(site)
    # Fourth (Feedback) section
    section_four = Feedback.objects.all()
    feedback = Feedback.objects.get(line_one=section_four[0].line_one)
    back = {
        'line': feedback.line_one,
        'line_second': feedback.line_two,
        'back': feedback.line_three
    }
    context.update(back)

    return render_to_response(
        "landing/index.html", context
    )
