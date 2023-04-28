from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import notes_work
from . import quote_work
from . import grammar_work

########################### index ###########################

def index(request):
    quote, person = quote_work.get_quote_to_play()
    return render(request, "index.html", context={"quote": quote, "person": person})

#############################################################


########################### terms ###########################

def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        new_term = request.POST.get("new_word", "")
        new_definition = request.POST.get("new_translation", "").replace(";", ",")

        context = {"user": user_name}
        if len(new_definition) == 0 and len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Слово или выражение и перевод должны быть не пустыми"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Слово или выражение должно быть не пустым"
        elif len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово или выражение добавлено"
            terms_work.write_term(new_term, new_definition, f"{user_name}/{user_email}")
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        return add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)

def terms_play(request):
    trans = terms_work.get_term_to_play()
    return render(request, "terms_play.html", context={"trans": trans})

def check_term(request):
    if request.method == "POST":
        cache.clear()
        known_word_user = request.POST.get("known_word", "")
        known_word_correct = terms_work.get_term_to_check()
        context = dict()
        if known_word_user.lower() != known_word_correct.lower():
            context["success"] = False
            context["comment"] = f"Правильный ответ: {known_word_correct}Вы ввели: {known_word_user}"
            context["correct"] = known_word_correct
            context["user_ans"] = known_word_user
        else:
            context["success"] = True
            context["comment"] = "Вы абсолютно правы! Так держать!"
        return render(request, "terms_play_check.html", context)
    else:
        return terms_play(request)

#############################################################

########################### notes ###########################

def add_note(request):
    return render(request, "add_note.html")

def send_note(request):
    if request.method == "POST":
        cache.clear()
        note_name = request.POST.get("new_note", "")
        note_description = request.POST.get("new_note_description")
        notes_work.write_note(note_name, note_description)
        return index(request)
    else:
        return add_note(request)

def show_notes(request):
    notes = notes_work.get_notes_to_show()
    return render(request, "notes.html", context={"notes": notes})

#############################################################

########################## grammar ##########################

def grammar_play(request):
    trans = grammar_work.get_grammar_to_play()
    return render(request, "grammar_play.html", context={"trans": trans})

def check_grammar(request):
    if request.method == "POST":
        cache.clear()
        known_word_user = request.POST.get("known_word", "")
        known_word_correct = grammar_work.get_grammar_to_check()
        context = dict()
        if known_word_user.lower() != known_word_correct.lower():
            context["success"] = False
            context["comment"] = f"Правильный ответ: {known_word_correct}Вы ввели: {known_word_user}"
            context["correct"] = known_word_correct
            context["user_ans"] = known_word_user
        else:
            context["success"] = True
            context["comment"] = "Вы абсолютно правы! Так держать!"
        return render(request, "grammar_play_check.html", context)
    else:
        return terms_play(request)
    

#############################################################