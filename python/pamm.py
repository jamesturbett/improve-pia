def calculate_pamm_bounds(
    progs: int, prefs_before: int, ratio_after_ukfpo: float
) -> int | tuple[int, int]:

    max_possible_pamm = min(progs, prefs_before)

    valid_pamm: list[int] = []

    # Try each possible PAMM value, and see if it yields the published competition ratio after PAMM
    for pamm in range(max_possible_pamm + 1):
        prefs_after = prefs_before - pamm
        progs_after = progs - pamm
        if (
            progs_after > 0
        ):  # Can't PAMM all programmes otherwise competition ratio becomes infinite
            ratio_after_exact = prefs_after / progs_after
            ratio_after_2dp = round(ratio_after_exact, 2)
            if ratio_after_2dp == ratio_after_ukfpo:
                valid_pamm.append(pamm)

    # If there's only one valid PAMM value, return it
    if len(valid_pamm) == 1:
        return valid_pamm[0]

    # Otherwise return the min and max valid PAMM values
    pamm_bounds = (min(valid_pamm), max(valid_pamm))
    return pamm_bounds
