def get_part_string(source_string, part_size=30):
    if len(source_string) < part_size:
        return unicode(source_string)
    else:
        return unicode(source_string[:part_size - 1] + u'...')
