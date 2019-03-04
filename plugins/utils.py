def second_to_format(seconds):
    minute = int(seconds / 60)
    seconde = int(seconds % 60)
    return "{} minutes et {} secondes".format(minute, seconde)
