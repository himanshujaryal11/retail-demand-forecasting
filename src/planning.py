from __future__ import annotations
import pandas as pd

def promotion_planning_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """Summarise historical sales by store and promotion flag.

    This is descriptive planning support, not a causal estimate of promotion lift.
    """
    required = {"Store", "Promo", "Sales"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    summary = (frame.groupby(["Store", "Promo"], as_index=False)["Sales"]
               .agg(["mean", "median", "count"]).reset_index())
    return summary
