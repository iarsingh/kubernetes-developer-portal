class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    image = str(body.get("image", ""))
    if image.endswith(":latest") or image == "latest":
        failed.append("image_tag_latest")

    reps = int(body.get("replicas") or 0)\n    if not 1 <= reps <= 5: failed.append("replicas")
    return {"passed": not failed, "failed": failed, "applied": False}
