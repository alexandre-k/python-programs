import simplejson as json

def jsonify(decorated_func):
    def inner(*args, **kwargs):
        jsonified = json.dumps(args, indent=4 * ' ')
        return jsonified
    return inner

@jsonify
def myfunc(*args, **kwargs):
    return args, kwargs
