# flisk
A lightweight wrapper for flask

## What is flisk?
- flisk is a decorator system designed to make url routing across files easier and cleaner.

### What flisk does
- flisk works of a custom decorator under `views` this allows parsing of kwargs like `name`, `pass_request` and `classview` with this flisk automatically registers the url endpoint based off class name (if applicable) and function name *or* if you have specified a `name` it will use that, this works with multi-slash names also e.g `v1/home`.

### Example
- Here is an example showing how easy it is to start using flisk!

__In our main file__
```py
from flisk import FliskApp

WEB_SERVER_DETAILS = REGISTERED_APPS = [  # This is the list requires to tell flisk what files contain views in.
    'webserver.myapp.apiviews',   # This happens to be in webserver/myapp/apiviews.py
    'webserver.myapp.mainsite'
]

app = FliskApp(__name__, WEB_SERVER_DETAILS)  # flisk inherits Flask's app class.
app.load()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
```

__Meanwhile in our views file__
```py
from flisk import Extensions, views   # We import flisk and register our views

# This makes our url <some base ip>/api/v1/myendpoints/<int:user_id>/
class Api(views.RouteView):
    @classmethod
    @views.register_path(name="v1/myendpoints", classview=True, pass_request=True)
    def test(cls, request: Extensions.Request, user_id: int):
        return f"Hello! {user_id}"
```
