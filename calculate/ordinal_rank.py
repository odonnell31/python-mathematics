def ordinal_rank(seq, item):
    """
    Accepts a sequence and an item and returns the item's
    ordinal rank as an integer
    
    h3. Example usage
    
        >> import calculate
        >> qs = Player.objects.all().order_by("-career_home_runs")
        >> barry = Player.objects.get(first_name__iexact='Barry', last_name__iexact='Bonds')
        >> calculate.ordinal_rank(qs, barry)
        1
    
    h3. Documentation
    
        * "ordinal rank":http://en.wikipedia.org/wiki/Ranking#Ordinal_ranking_.28.221234.22_ranking.29

    """
    try:
        list_seq = list(seq)
    except TypeError:
        raise TypeError('First parameter must be a sequence. You submitted a %s object' % type(seq))

    index = list_seq.index(item)
    return index + 1
