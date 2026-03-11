def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    new_tags = existing_tags.copy()
    for simple in simple_tags:
        new_tags[simple] = "true"

    for k, v in key_value_tags.items():
        new_tags[k] = v 

    return new_tags

if __name__ == "__main__":
    initial = {'owner': 'dev-team', 'env': 'dev'}
    final_tags = manage_tags(
        initial,
        'billable',              # A simple tag
        'critical',              # Another simple tag
        'critical',
        env='staging',           # A key-value tag that overwrites an existing key
        cost_center='xyz-123'    # A new key-value tag
    )

    print(final_tags)
    print(initial)