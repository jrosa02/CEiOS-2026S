"""Zadanie 3 – Wybór najlepszej taryfy na zakup energii elektrycznej

Porównanie taryf G11, G12, G12w, G13 firmy Tauron S.A.
dla gospodarstwa domowego w Krakowie, rok 2026.

Uruchomienie:
    uv run python lab01/zadanie3.py
"""

from __future__ import annotations

import tomllib
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

LAB_DIR = Path(__file__).parent


# ---------------------------------------------------------------------------
# Ładowanie danych
# ---------------------------------------------------------------------------

def load_config() -> dict:
    with open(LAB_DIR / "tariffs.toml", "rb") as f:
        return tomllib.load(f)


def load_usage_profile() -> dict[int, float]:
    """Zwraca słownik {godzina (0-23): zużycie [kWh]}."""
    df = pd.read_csv(LAB_DIR / "usage_profile.csv")
    return dict(zip(df["hour"], df["energy_kwh"]))


# ---------------------------------------------------------------------------
# Budowanie ramki danych z pełnym rokiem
# ---------------------------------------------------------------------------

def build_hourly_df(cfg: dict) -> pd.DataFrame:
    """Tworzy DataFrame z jednym wierszem na każdą godzinę roku 2026."""
    year = cfg["metadata"]["year"]
    idx = pd.date_range(f"{year}-01-01", f"{year + 1}-01-01", freq="h", inclusive="left")

    df = pd.DataFrame(index=idx)
    df["hour"] = df.index.hour
    df["weekday"] = df.index.weekday  # 0 = poniedziałek, 6 = niedziela

    holiday_dates = pd.to_datetime(cfg["holidays_2026"]["dates"]).normalize()
    df["date"] = df.index.normalize()
    df["is_holiday"] = df["date"].isin(holiday_dates)
    df["is_weekend"] = df["weekday"] >= 5
    df["is_work_free"] = df["is_holiday"] | df["is_weekend"]

    usage = load_usage_profile()
    df["energy_kwh"] = df["hour"].map(usage)

    return df


# ---------------------------------------------------------------------------
# Przypisanie stref taryfowych
# ---------------------------------------------------------------------------

def assign_zones(df: pd.DataFrame, tariff_cfg: dict) -> pd.DataFrame:
    """Dodaje kolumnę 'zone' do df na podstawie reguł danej taryfy.

    Obsługiwane klucze stref w TOML:
    - all_hours      → strefa aktywna we WSZYSTKICH dniach (np. G12 dzienna/nocna,
                       gdzie podział dzień/noc obowiązuje 7 dni/tydzień bez wyjątku)
    - workday_hours  → strefa aktywna TYLKO w dni robocze; soboty, niedziele i święta
                       trafiają do strefy domyślnej (np. G12w szczyt, G13 szczyty)
    - brak obu       → strefa domyślna (ostatnia w TOML = najtańsza)
    """
    zones = tariff_cfg["zones"]
    zone_keys = list(zones.keys())
    default_zone = zone_keys[-1]  # ostatnia strefa = najtańsza / domyślna

    df = df.copy()
    df["zone"] = default_zone

    for zk in zone_keys[:-1]:
        zc = zones[zk]
        if "all_hours" in zc:
            # Strefa obowiązuje każdego dnia, bez wyjątku weekendowego
            mask = df["hour"].isin(zc["all_hours"])
        elif "workday_hours" in zc:
            # Strefa obowiązuje tylko w dni robocze
            mask = (~df["is_work_free"]) & (df["hour"].isin(zc["workday_hours"]))
        else:
            continue
        df.loc[mask, "zone"] = zk

    return df


# ---------------------------------------------------------------------------
# Obliczanie kosztów
# ---------------------------------------------------------------------------

def compute_costs(df: pd.DataFrame, tariff_cfg: dict, cfg: dict) -> dict:
    """Oblicza roczne koszty dla danej taryfy."""
    zones = tariff_cfg["zones"]
    fixed = cfg["tariffs"]["common"]["fixed_per_month"]
    n_periods = cfg["metadata"]["billing_periods_per_year"]
    vat = cfg["metadata"]["vat_rate"]

    total_energy = df["energy_kwh"].sum()

    # Koszty zmienne strefowe
    zone_rows: list[dict] = []
    total_purchase_net = 0.0
    total_distribution_net = 0.0

    for zk, zc in zones.items():
        mask = df["zone"] == zk
        energy = df.loc[mask, "energy_kwh"].sum()
        purch = energy * zc["purchase_net"]
        distr = energy * zc["distribution_net"]
        total_purchase_net += purch
        total_distribution_net += distr
        zone_rows.append({
            "zone_name": zc["name"],
            "purchase_unit": zc["purchase_net"],
            "distribution_unit": zc["distribution_net"],
            "energy_kwh": energy,
            "purchase_net": purch,
            "distribution_net": distr,
        })

    # Opłaty stałe (roczne)
    fixed_annual = {k: v * 12 for k, v in fixed.items()}
    total_fixed_net = sum(fixed_annual.values())

    total_net = (total_purchase_net + total_distribution_net
                 + total_fixed_net)
    total_gross = total_net * (1 + vat)

    return {
        "zone_rows": zone_rows,
        "fixed_annual": fixed_annual,
        "total_energy_kwh": total_energy,
        "total_purchase_net": total_purchase_net,
        "total_distribution_net": total_distribution_net,
        "total_fixed_net": total_fixed_net,
        "total_net": total_net,
        "total_gross": total_gross,
    }


# ---------------------------------------------------------------------------
# Wyświetlanie wyników
# ---------------------------------------------------------------------------

_FIXED_LABELS = {
    "sieciowa_stala": "Opłata sieciowa stała (OSD)",
    "abonamentowa": "Opłata abonamentowa (OSD)",
    "mocowa": "Opłata mocowa",
}


def print_tariff_results(tariff_key: str, tariff_cfg: dict, result: dict, vat: float) -> None:
    print(f"\n{'=' * 72}")
    print(f"  Taryfa {tariff_key}: {tariff_cfg['description']}")
    print(f"{'=' * 72}")

    # --- Tabela strefowa ---
    rows = []
    for zr in result["zone_rows"]:
        total_unit = zr["purchase_unit"] + zr["distribution_unit"]
        var_net = zr["purchase_net"] + zr["distribution_net"]
        rows.append({
            "Strefa": zr["zone_name"],
            "Zakup [PLN/kWh]": zr["purchase_unit"],
            "Dystrybucja [PLN/kWh]": zr["distribution_unit"],
            "Razem jedn. [PLN/kWh]": total_unit,
            "Energia [kWh]": zr["energy_kwh"],
            "Zakup netto [PLN]": zr["purchase_net"],
            "Dystrybucja netto [PLN]": zr["distribution_net"],
            "Razem zm. netto [PLN]": var_net,
            "VAT 23% [PLN]": var_net * vat,
            "Razem zm. brutto [PLN]": var_net * (1 + vat),
        })

    zone_df = pd.DataFrame(rows).set_index("Strefa")
    float_cols = zone_df.columns.tolist()

    # formatowanie: ceny jednostkowe na 4 miejsca, reszta na 2
    fmt = {}
    for col in float_cols:
        if "PLN/kWh" in col:
            fmt[col] = "{:.4f}"
        else:
            fmt[col] = "{:.2f}"

    print("\nKoszty zmienne strefowe:\n")
    print(zone_df.to_csv(sep="\t", float_format=lambda x: f"{x:.2f}"))

    # --- Opłaty stałe ---
    print("\nOpłaty stałe (netto / rok):")
    for k, v in result["fixed_annual"].items():
        print(f"  {_FIXED_LABELS.get(k, k):<36}: {v:>9.2f} PLN")
    total_fixed = result["total_fixed_net"]
    print(f"  {'Razem':<36}: {total_fixed:>9.2f} PLN  "
          f"| brutto: {total_fixed * (1 + vat):>9.2f} PLN")

    # --- Podsumowanie ---
    vat_amount = result["total_net"] * vat
    print(f"\n  {'Łącznie netto':<34}: {result['total_net']:>10.2f} PLN")
    print(f"  {'VAT 23%':<34}: {vat_amount:>10.2f} PLN")
    print(f"  {'Łącznie brutto':<34}: {result['total_gross']:>10.2f} PLN")


def print_summary(all_results: dict[str, dict], vat: float) -> None:
    print(f"\n{'=' * 72}")
    print("  ZESTAWIENIE PORÓWNAWCZE")
    print(f"{'=' * 72}\n")

    rows = []
    for tkey, res in all_results.items():
        rows.append({
            "Taryfa": tkey,
            "Zakup energii [PLN]": res["total_purchase_net"],
            "Dystrybucja zm. [PLN]": res["total_distribution_net"],
            "Opłaty stałe [PLN]": res["total_fixed_net"],
            "Netto [PLN]": res["total_net"],
            "VAT 23% [PLN]": res["total_net"] * vat,
            "Brutto [PLN]": res["total_gross"],
        })

    summary = pd.DataFrame(rows).set_index("Taryfa")
    print(summary.to_csv(sep="\t", float_format=lambda x: f"{x:,.2f}"))

    best = min(all_results, key=lambda t: all_results[t]["total_gross"])
    worst = max(all_results, key=lambda t: all_results[t]["total_gross"])
    diff = all_results[worst]["total_gross"] - all_results[best]["total_gross"]
    print(f"\n  Najtańsza taryfa: {best}  ({all_results[best]['total_gross']:,.2f} PLN brutto/rok)")
    print(f"  Najdroższa taryfa: {worst}  ({all_results[worst]['total_gross']:,.2f} PLN brutto/rok)")
    print(f"  Różnica: {diff:,.2f} PLN/rok ({diff / all_results[worst]['total_gross'] * 100:.1f}%)")


# ---------------------------------------------------------------------------
# Wizualizacja
# ---------------------------------------------------------------------------

_COST_COLORS = {
    "Zakup energii": "#2E7D32",
    "Dystrybucja zm.": "#1565C0",
    "Opłaty płaskie": "#F9A825",
    "Opłaty stałe": "#C62828",
}


def plot_zone_heatmap(df_with_zones: dict[str, pd.DataFrame], save_path: Path) -> None:
    """Wykreśla mapy stref taryfowych – jeden panel na taryfę, tydzień 26 (23–29.06.2026).

    Każdy subplot: 7 wierszy (Pon–Nie) × 24 kolumny (godziny 0–23).
    """
    import matplotlib.colors as mcolors
    from matplotlib.patches import Patch

    # Kolory stref per taryfa (spójne z _COST_COLORS, czytelne kontrasty)
    _ZONE_COLORS: dict[str, dict[str, str]] = {
        "G11": {
            "all_day":          "#1976D2",
        },
        "G12": {
            "day":              "#F57C00",
            "night":            "#1565C0",
        },
        "G12w": {
            "peak":             "#F57C00",
            "off_peak":         "#1565C0",
        },
        "G13": {
            "afternoon_peak":   "#C62828",
            "morning_peak":     "#F57C00",
            "remaining":        "#1565C0",
        },
    }

    day_names = ["Pon", "Wto", "Śro", "Czw", "Pią", "Sob", "Nie"]
    # Tydzień 26: 22–28.06.2026 – pełny Pon–Nie, bez świąt
    target_dates = pd.date_range("2026-06-22", periods=7, freq="D").normalize()

    fig, axes = plt.subplots(2, 2, figsize=(16, 9))
    fig.suptitle("Zadanie 3 – Mapy stref taryfowych (22–28.06.2026)",
                 fontsize=13, fontweight="bold")
    axes = axes.flatten()

    for idx, (tkey, df) in enumerate(df_with_zones.items()):
        ax = axes[idx]
        zone_colors = _ZONE_COLORS.get(tkey, {})

        # Ustal kolejność stref (z TOML – kolejność wstawiania)
        ordered_zones = list(dict.fromkeys(df["zone"]))
        zone_to_int = {z: i for i, z in enumerate(ordered_zones)}
        palette = [zone_colors.get(z, "#888888") for z in ordered_zones]
        cmap = mcolors.ListedColormap(palette)

        # Filtruj do wybranego tygodnia
        df_week = df[df["date"].isin(target_dates)]

        # Zbuduj macierz 7 × 24
        grid = np.full((7, 24), np.nan)
        for _, row in df_week.iterrows():
            grid[int(row["weekday"]), int(row["hour"])] = zone_to_int[row["zone"]]

        # Heatmapa
        ax.imshow(grid, cmap=cmap, aspect="auto",
                  vmin=-0.5, vmax=len(ordered_zones) - 0.5,
                  interpolation="nearest")

        # Osie
        ax.set_yticks(range(7))
        ax.set_yticklabels(day_names, fontsize=9)
        ax.set_xticks(range(0, 24))
        ax.set_xticklabels(range(0, 24), fontsize=7, ha='left')
        ax.set_xlabel("Godzina", fontsize=9)
        ax.set_title(tkey, fontsize=11, fontweight="bold")

        # Siatka między kafelkami
        ax.set_xticks(np.arange(-0.5, 24, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 7, 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=0.8)
        ax.tick_params(which="minor", length=0)

        # Legenda wewnątrz panelu
        legend_patches = [Patch(facecolor=zone_colors.get(z, "#888888"),
                                edgecolor="white", label=z)
                          for z in ordered_zones]
        ax.legend(handles=legend_patches, loc="lower right", fontsize=8,
                  framealpha=0.85)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"Mapy stref zapisane: {save_path}")
    plt.show()


def plot_results(all_results: dict[str, dict], vat: float, save_path: Path) -> None:
    tariffs = list(all_results.keys())
    x = np.arange(len(tariffs))

    purchase = np.array([all_results[t]["total_purchase_net"] for t in tariffs])
    distribution = np.array([all_results[t]["total_distribution_net"] for t in tariffs])
    fixed = np.array([all_results[t]["total_fixed_net"] for t in tariffs])
    totals_net = purchase + distribution + fixed
    totals_gross = totals_net * (1 + vat)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Zadanie 3 – Porównanie taryf Tauron (Kraków, 2026)", fontsize=13, fontweight="bold")

    # --- Wykres 1: porównanie kosztów brutto ---
    bars = axes[0].bar(tariffs, totals_gross, color=["#1976D2", "#388E3C", "#F57C00", "#7B1FA2"],
                       alpha=0.85, edgecolor="white", linewidth=1.2)
    axes[0].bar(tariffs, totals_net, color=["#1976D2", "#388E3C", "#F57C00", "#7B1FA2"],
                alpha=0.45, edgecolor="white", linewidth=1.2)
    axes[0].set_title("Całkowity koszt roczny")
    axes[0].set_ylabel("Koszt [PLN/rok]")
    axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    for bar, gross, net in zip(bars, totals_gross, totals_net):
        axes[0].text(bar.get_x() + bar.get_width() / 2, gross + 15,
                     f"{gross:,.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold")
        axes[0].text(bar.get_x() + bar.get_width() / 2, net / 2,
                     f"netto\n{net:,.0f}", ha="center", va="center",
                     fontsize=7, color="white", fontweight="bold")
    axes[0].legend(
        handles=[
            plt.Rectangle((0, 0), 1, 1, color="gray", alpha=0.85, label="Brutto (z VAT)"),
            plt.Rectangle((0, 0), 1, 1, color="gray", alpha=0.45, label="Netto"),
        ],
        fontsize=9,
    )
    axes[0].set_ylim(0, totals_gross.max() * 1.12)
    axes[0].grid(True, alpha=0.3, linestyle="--", axis="y")

    # --- Wykres 2: struktura kosztów (skumulowany słupkowy, netto) ---
    bottoms = np.zeros(len(tariffs))
    components = [
        ("Zakup energii", purchase, "#2E7D32"),
        ("Dystrybucja zm.", distribution, "#1565C0"),
        ("Opłaty stałe", fixed, "#C62828"),
    ]
    for label, values, color in components:
        axes[1].bar(tariffs, values, bottom=bottoms, label=label, color=color, alpha=0.85,
                    edgecolor="white", linewidth=0.8)
        for i, (v, b) in enumerate(zip(values, bottoms)):
            if v > 30:
                axes[1].text(x[i], b + v / 2, f"{v:,.0f}", ha="center", va="center",
                             fontsize=7.5, color="white", fontweight="bold")
        bottoms += values

    axes[1].set_title("Struktura kosztów (netto)")
    axes[1].set_ylabel("Koszt [PLN/rok]")
    axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    axes[1].legend(loc="upper right", fontsize=9)
    axes[1].set_ylim(0, totals_gross.max() * 1.12)
    axes[1].grid(True, alpha=0.3, linestyle="--", axis="y")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"\nWykres zapisany: {save_path}")
    plt.show()


# ---------------------------------------------------------------------------
# Główna funkcja
# ---------------------------------------------------------------------------

def main() -> None:
    cfg = load_config()
    meta = cfg["metadata"]
    vat = meta["vat_rate"]

    df = build_hourly_df(cfg)

    # Informacje weryfikacyjne
    n_days = df["date"].nunique()
    n_work_free = df.groupby("date")["is_work_free"].first().sum()
    n_holidays = len(cfg["holidays_2026"]["dates"])
    print(f"Rok {meta['year']}: {n_days} dni, {len(df)} godzin")
    print(f"Dni wolne od pracy: {int(n_work_free)} "
          f"(weekendy + {n_holidays} świąt ustawowych)")
    print(f"Roczne zużycie energii: {df['energy_kwh'].sum():.2f} kWh")

    # Obliczenia dla każdej taryfy
    all_results: dict[str, dict] = {}
    df_with_zones: dict[str, pd.DataFrame] = {}
    for tkey, tcfg in cfg["tariffs"].items():
        if tkey == "common":  # skip shared config
            continue
        df_t = assign_zones(df, tcfg)
        result = compute_costs(df_t, tcfg, cfg)
        all_results[tkey] = result
        df_with_zones[tkey] = df_t
        print_tariff_results(tkey, tcfg, result, vat)

    # Zestawienie porównawcze
    print_summary(all_results, vat)

    # Wizualizacja
    plot_results(all_results, vat, LAB_DIR / "zadanie3_wyniki.png")
    plot_zone_heatmap(df_with_zones, LAB_DIR / "zadanie3_strefy.png")


if __name__ == "__main__":
    main()
