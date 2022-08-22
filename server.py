from flask import Flask, abort, request, jsonify
import Event

app = Flask(__name__)


@app.route('/api/v2/events/page')
def view():
    return jsonify(get_paginated_list(
        Event,
        '/api/v2/events/page',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 20)
    ))


def get_paginated_list(klass, url, start, limit):
    # check if page exists
    results = klass.query.all()
    count = len(results)
    if (count < start):
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj



'''@app.route("/magazines")
def magazines():
    # process query parameters
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per-page", 100, type=int)
    # query
    magazines = Magazine.query.paginate(page, per_page)
    # combine results with pagination
    results = {
        "results": [{"title": m.title, "publisher": m.publisher} for m in magazines.items],
        "pagination": {
            "count": magazines.total,
            "page": page,
            "per_page": per_page,
            "pages": magazines.pages,
        },
    }
    return jsonify(results)'''