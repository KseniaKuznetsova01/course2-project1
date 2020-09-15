import functools
import json
import os
import tempfile
import argparse

parser = argparse.ArgumentParser()

def decorator(func):
  @functools.wraps(func)
  def wrapped(*args, **kwargs):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        key, value = json.dumps(func(*args, **kwargs))
    args = parser.parse_args(key, action = 'store_const', const = value, type = dict)
    with open(storage_path, 'w') as f:
        json.dump(args, f)
    return args
  return wrapped

@decorator
def storage(*args):
  return args

