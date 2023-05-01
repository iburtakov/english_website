from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import notes_work
from . import quote_work
from . import grammar_work

########################### index ###########################

def index(request):
    quote, person = quote_work.get_quote_to_use()
    return render(request, "index.html", context={"quote": quote, "person": person})

#############################################################


########################### terms ###########################

def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term_to_check(request):
    if request.method != "POST":
        return add_term(request)

    cache.clear()

    new_term = request.POST.get("new_word", "").strip()
    new_definition = request.POST.get("new_translation", "").replace(";", ",").strip()

    context = {"user": "user"}

    if not new_term or not new_definition:
        context.update({
            "success": False,
            "comment": "Fields with word and translation must not be empty. Return to the previous page",
        })
    else:
        terms_work.write_term(new_term, new_definition, "user")
        context.update({
            "success": True,
            "comment": "Success!",
            "success-title": "",
        })

    return render(request, "term_request.html", context)


def terms_use(request):
    trans = terms_work.get_term_to_use()
    return render(request, "terms_use.html", context={"trans": trans})


def check_term(request):
    if request.method != "POST":
        return terms_use(request)

    cache.clear()
    known_word_user = request.POST.get("known_word", "")
    known_word_correct = terms_work.get_term_to_check()

    context = {
        "success": known_word_user.lower() == known_word_correct.lower(),
        "correct": known_word_correct,
        "user_ans": known_word_user,
    }

    if not context["success"]:
        context["comment"] = f"Right answer: {known_word_correct}. Your answer: {known_word_user}"
    else:
        context["comment"] = "Your answer is right"

    return render(request, "terms_use_check.html", context)

#############################################################

########################### notes ###########################

def add_note(request):
    return render(request, "add_note.html")

def send_note(request):
    if request.method != "POST":
        return add_note(request)
    
    cache.clear()
    note_name = request.POST.get("new_note", "")
    note_description = request.POST.get("new_note_description", "")
    
    if not note_name or not note_description:
        context = {
            "success": False,
            "comment": "Fields with note name and description must not be empty. Return to the previous page"
        }
    else:
        notes_work.write_note(note_name, note_description)
        context = {
            "success": True,
            "comment": "Success!"
        }

    return index(request)

def show_notes(request):
    notes = notes_work.get_notes_to_show()
    return render(request, "notes.html", context={"notes": notes})

#############################################################


########################## grammar ##########################

def grammar_play(request):
    trans = grammar_work.get_grammar_to_use()
    return render(request, "grammar_play.html", context={"trans": trans})

def check_grammar(request):
    if request.method != "POST":
        return terms_use(request)

    cache.clear()

    known_word_user = request.POST.get("known_word", "")
    known_word_correct = grammar_work.get_grammar_to_check()

    context = {
        "success": known_word_user.lower() == known_word_correct.lower(),
        "comment": f"Right answer: {known_word_correct} Your answer: {known_word_user}" if known_word_user.lower() != known_word_correct.lower() else "Your answer is right",
        "correct": known_word_correct if known_word_user.lower() != known_word_correct.lower() else "",
        "user_ans": known_word_user,
    }

    return render(request, "grammar_play_check.html", context)
    

#############################################################