from flask import Blueprint, render_template
from models.language_model import LanguageModel

home_controller = Blueprint("home_controller", __name__)


@home_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
        )
