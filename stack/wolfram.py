import wolframalpha


def wolfram_alpha_query(query: str):
    wa = wolframalpha.Client("VH5LXL-ALTVYGQVU3")
    return next(wa.query(query).results).text
