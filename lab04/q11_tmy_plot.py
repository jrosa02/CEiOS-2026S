import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs")
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "tmy_krakow.csv")

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

# Read month-year selection table from header (lines 5-16, 0-indexed 4-15)
month_years = {}
with open(DATA) as f:
    lines = f.readlines()
for line in lines[4:16]:
    parts = line.strip().split(",")
    if len(parts) == 2 and parts[0].isdigit():
        month_years[int(parts[0])] = int(parts[1])

# Read data (skip 17 header lines)
df = pd.read_csv(DATA, skiprows=17, nrows=8760)
df.columns = [c.strip() for c in df.columns]

df["month"] = df["time(UTC)"].astype(str).str[4:6].astype(int)
df["hour"]  = df["time(UTC)"].astype(str).str[9:11].astype(int)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    "Typowy Rok Meteorologiczny (TMY) — Kraków, PVGIS-SARAH3 (2005–2023)",
    fontsize=11,
)

# ── Panel left: monthly GHI sum (stacked Gb + Gd) ────────────────────────
ax = axes[0]
monthly = df.groupby("month")[["G(h)", "Gb(n)", "Gd(h)"]].sum() / 1000

# Use G(h) = Gb_horiz + Gd(h) — split into direct horiz and diffuse
# Gb_horiz not directly in TMY; approx from G(h) - Gd(h)
gb_h = monthly["G(h)"] - monthly["Gd(h)"]
gd_h = monthly["Gd(h)"]
months = range(1, 13)

ax.bar(months, [gb_h.loc[m] for m in months], label="Bezpośrednie poziome",
       color="#e07b00")
ax.bar(months, [gd_h.loc[m] for m in months],
       bottom=[gb_h.loc[m] for m in months],
       label="Rozproszone DHI", color="#5b9bd5")

ax.set_xticks(list(months))
# Label with month and source year
xlabels = [f"{MONTHS_PL[m-1]}\n({month_years.get(m, '?')})" for m in months]
ax.set_xticklabels(xlabels, fontsize=7)
ax.set_ylabel("Suma miesięczna GHI [kWh/m²]")
ax.set_title("Miesięczne sumy GHI (rok źródłowy w nawiasie)")
ax.legend(fontsize=8)
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.grid(axis="y", alpha=0.3)

# ── Panel right: heatmap hour × month of mean G(h) ───────────────────────
ax2 = axes[1]
pivot = df.pivot_table(index="hour", columns="month", values="G(h)", aggfunc="mean")
pivot = pivot.reindex(columns=range(1, 13), index=range(24))

im = ax2.imshow(pivot.values, aspect="auto", origin="lower",
                cmap="YlOrRd", interpolation="nearest",
                extent=[-0.5, 12.5, -0.5, 23.5])
cbar = plt.colorbar(im, ax=ax2)
cbar.set_label("Średnie G(h) [W/m²]")

ax2.set_xticks(range(12))
ax2.set_xticklabels(MONTHS_PL, fontsize=7)
ax2.set_yticks(range(0, 24, 4))
ax2.set_ylabel("Godzina UTC")
ax2.set_title("Rozkład godzinowy GHI (mapa ciepła)")

plt.tight_layout()
out = os.path.join(OUT_DIR, "q11_tmy_profile.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"Zapisano: {out}")
