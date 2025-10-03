def calc_pamm_bounds(
    progs: int, prefs_before: int, pub_ratio_after: float
) -> int | tuple[int, int]:

    # Can't PAMM more than number of progs or first choice prefs
    max_poss_pamm: int = int(min(progs, prefs_before))

    valid_pamm_vals: list[int] = []

    # Try each possible number of PAMM applicants
    for num_pamm in range(max_poss_pamm + 1):

        # Calculate remaining prefs and progs after PAMM
        prefs_after = prefs_before - num_pamm
        progs_after = progs - num_pamm

        # Can't PAMM all progs otherwise comp ratio becomes inf
        if progs_after > 0:

            # Calculate the exact ratio after PAMM and round to 2dp
            exact_ratio_after = prefs_after / progs_after
            ratio_after_2dp = round(exact_ratio_after, 2)

            # Check if matches the published ratio after PAMM
            if ratio_after_2dp == pub_ratio_after:
                valid_pamm_vals.append(num_pamm)

    # If there's only one valid PAMM value, return it
    if len(valid_pamm_vals) == 1:
        return valid_pamm_vals[0]

    # Otherwise return the min and max valid PAMM values
    pamm_bounds = (min(valid_pamm_vals), max(valid_pamm_vals))
    return pamm_bounds
