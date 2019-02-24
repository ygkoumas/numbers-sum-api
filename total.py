import flask
from numbers_to_add import get_numbers_to_add

total = flask.Blueprint("total", __name__)

@total.route("")
def get_total():
    try:
        numbers = get_numbers_to_add()
    except:
        flask.abort(503)

    total = sum(numbers)
    return flask.jsonify({"total": total})
