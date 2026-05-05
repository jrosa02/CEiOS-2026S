import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs")
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "hourly_krakow_2023.csv")

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]
SAMPLE_MONTHS = {6: "Czerwiec", 9: "Wrzesień", 12: "Grudzień"}
COLORS = {"Gb(i)": "#e07b00", "Gd(i)": "#5b9bd5"}

df = pd.read_csv(DATA, skiprows=8, nrows=8760)
df.columns = [c.strip() for c in df.columns]

# Parse timestamps
df["month"] = df["time"].astype(str).str[4:6].astype(int)
df["hour"]  = df["time"].astype(str).str[9:11].astype(int)
df["GHI"]   = df["Gb(i)"] + df["Gd(i)"]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    "Godzinowe dane promieniowania słonecznego — Kraków 2023 (PVGIS-SARAH3)",
    fontsize=11,
)

# ── Panel left: monthly GHI stacked bar ───────────────────────────────────
ax = axes[0]
monthly = df.groupby("month")[["Gb(i)", "Gd(i)"]].sum() / 1000  # W→kWh
months = range(1, 13)
gb = [monthly.loc[m, "Gb(i)"] for m in months]
gd = [monthly.loc[m, "Gd(i)"] for m in months]

bars1 = ax.bar(months, gb, label="Gb(i) bezpośrednie", color=COLORS["Gb(i)"])
bars2 = ax.bar(months, gd, bottom=gb, label="Gd(i) rozproszone", color=COLORS["Gd(i)"])
ax.set_xticks(list(months))
ax.set_xticklabels(MONTHS_PL, fontsize=8)
ax.set_ylabel("Suma miesięczna [kWh/m²]")
ax.set_title("Miesięczne sumy irradiancji poziomej 2023")
ax.legend(fontsize=8)
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.grid(axis="y", alpha=0.3)

# ── Panel right: average daily profiles for 3 months ─────────────────────
ax2 = axes[1]
line_styles = ["-", "--", ":"]
colors = ["#e07b00", "#2ca02c", "#1a6faf"]
for (m_num, m_name), ls, col in zip(SAMPLE_MONTHS.items(), line_styles, colors):
    sub = df[df["month"] == m_num]
    profile = sub.groupby("hour")["GHI"].mean()
    ax2.plot(profile.index, profile.values, label=m_name,
             linestyle=ls, color=col, linewidth=2)

ax2.set_xlabel("Godzina UTC")
ax2.set_ylabel("Średnia irradiancja GHI [W/m²]")
ax2.set_title("Średni dobowy profil GHI (wybrane miesiące)")
ax2.set_xlim(0, 23)
ax2.set_ylim(bottom=0)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.legend(fontsize=9)
ax2.grid(alpha=0.3)

plt.tight_layout()
out = os.path.join(OUT_DIR, "q7_hourly_radiation.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"Zapisano: {out}")
