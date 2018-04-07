import sys
import importlib.util
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .pattern import Pattern

from . import builtins

class Loader(FileSystemEventHandler):
    def __init__(self, animator, *paths):
        self.animator = animator
        self.paths = paths
        self.observer = Observer();
        self.patterns = {}
        for path in paths:
            self.observer.schedule(self, str(path), recursive=True)
        self.observer.start()

    def loadPattern(self, name, *args, **kwargs):
        for path in self.paths:
            filepath = (path / name).with_suffix('.py')
            if filepath.exists:
                if filepath in self.patterns:
                    return self.patterns[filepath]
                module = self.loadModule(filepath)
                pattern = Pattern(module, *args, **kwargs)
                self.patterns[filepath] = pattern
                return pattern
            print('Pattern file {} not found.'.format(name), file=sys.stderr)
            return None

    def loadDependentPattern(self, name, *args, **kwargs):
        pattern = self.loadPattern(name, *args, **kwargs)
        Pattern.tracked.append(pattern)
        return pattern

    def on_modified(self, event):
        path = Path(event.src_path)
        if path in self.patterns:
            print('Reloading pattern {}.'.format(path.stem))
            pattern = self.patterns[path]
            pattern.module = self.loadModule(path)
            pattern.build();

    def loadModule(self, filepath):
        spec = importlib.util.spec_from_file_location(filepath.stem, str(filepath))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if not module.main:
            print('Pattern file {} has no "main" function.'.format(filepath), file=sys.stderr)
            return None
        for key in dir(builtins):
            if not key.startswith('__'):
                if key not in module.__dict__:
                    module.__dict__[key] = builtins.__dict__[key]
        module.__dict__['load'] = self.loadDependentPattern
        return module
