def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates are ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.

    Raises:
        TypeError: If existing_tags is not a dictionary.
    """
    if not isinstance(existing_tags, dict):
        raise TypeError("Provided existing_tags not a dictionary.")

    new_tags = existing_tags.copy()

    for tag in set(simple_tags):
        new_tags[tag] = 'true'

    new_tags = new_tags | key_value_tags

    return new_tags

if __name__ == "__main__":
    good = {'name': 'good', 'age': 15}
    bad = ["this", "is", "a", "list"]

    print(manage_tags(good, "un", "deux", "trois", added="value"))
    #print(manage_tags(bad, "un", "deux", "trois", added="value"))