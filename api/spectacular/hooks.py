from drf_spectacular.plumbing import is_versioning_supported

def custom_preprocessing_hook(endpoints, **kwargs):
    filtered = []
    for path, path_regex, method, view in endpoints:
        if path == "/auth/users/" and method == "POST":
            filtered.append((path, path_regex, method, view))
        elif not path.startswith("/auth"):
            filtered.append((path, path_regex, method, view))
    return filtered