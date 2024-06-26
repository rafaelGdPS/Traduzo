from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

from models.history_model import HistoryModel

home_controller = Blueprint("home_controller", __name__)


@home_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translated = GoogleTranslator(
            source="auto", target=translate_to).translate(text_to_translate)

        HistoryModel(
            {
             "text_to_translate": text_to_translate,
             "translate_from": translate_from,
             "translate_to": translate_to,
            }
        ).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
        )


@home_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = GoogleTranslator(
        source="auto", target=translate_to).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
        )
