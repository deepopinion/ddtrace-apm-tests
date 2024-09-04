# ddtrace-apm-tests

Just a test repo to verify failures with ddtrace

## Dependencies

These are the dependencies to run this example app:
* Python 3.9
* [Just](https://just.systems/)
* [Poetry](https://python-poetry.org/)

## Running

To run this example app and see the error:

```shell
$ just run
```

Notice how it runs fine without ddtrace-run, but as soon as ddtrace-run wraps the command it doesn't work anymore.
