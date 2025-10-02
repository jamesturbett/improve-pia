def calc_pamm_bounds(
    progs: int, prefs_before: int, pub_ratio_after: float
) -> int | tuple[int, int]:

    max_poss_pamm = min(progs, prefs_before)

    valid_pamm_vals: list[int] = []

    # Try each possible num_pamm value, and see if it yields the pub competition ratio after num_pamm
    for num_pamm in range(max_poss_pamm + 1):
        prefs_after = prefs_before - num_pamm
        progs_after = progs - num_pamm
        if (
            progs_after > 0
        ):  # Can't PAMM all programmes otherwise competition ratio becomes infinite
            exact_ratio_after = prefs_after / progs_after
            ratio_after_2dp = round(exact_ratio_after, 2)
            if ratio_after_2dp == pub_ratio_after:
                valid_pamm_vals.append(num_pamm)

    # If there's only one valid PAMM value, return it
    if len(valid_pamm_vals) == 1:
        return valid_pamm_vals[0]

    # Otherwise return the min and max valid PAMM values
    pamm_bounds = (min(valid_pamm_vals), max(valid_pamm_vals))
    return pamm_bounds
