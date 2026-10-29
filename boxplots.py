import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
df1 = pd.read_csv("GNN_SE_TN.csv")
df2 = pd.read_csv("GNN_SE_FP.csv")
df3 = pd.read_csv("GNN_SE_FN.csv")
df4 = pd.read_csv("GNN_SE_TP.csv")

plt.rcParams.update({
    "font.size": 14,
    "axes.labelsize": 16,
    "axes.titlesize": 16,
    "xtick.labelsize": 13,
    "ytick.labelsize": 13,
    "legend.fontsize": 13,
    "axes.linewidth": 1.5,
    "xtick.major.width": 1.3,
    "ytick.major.width": 1.3,
    "xtick.major.size": 6,
    "ytick.major.size": 6,
    "xtick.minor.size": 3,
    "ytick.minor.size": 3,
})


def publication_boxplot(data, labels, colors, ylabel, title, filename,
                        showmeans=True, meanline=True, showfliers=False):

    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)

    mean_style = dict(linewidth=2, color='purple')
    median_style = dict(linewidth=2, color='black')

    bp = ax.boxplot(
        data,
        labels=labels,
        showfliers=showfliers,
        patch_artist=True,
        showmeans=showmeans,
        meanline=meanline,
        meanprops=mean_style,
        medianprops=median_style
    )

    # Apply custom colors to boxes
    for patch, c in zip(bp['boxes'], colors):
        patch.set_facecolor(c)
        patch.set_edgecolor('black')
        patch.set_linewidth(0.8)

    #ax.axhline(0.05, color='black', linestyle='--', linewidth=1)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Ticks and spines polish
    ax.tick_params(direction='in', top=True, right=True)
    ax.minorticks_on()
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)

    plt.tight_layout()
    legend_elements = [
        Line2D([0], [0], color='purple', lw=2, linestyle='--', label='Mean'),
        Line2D([0], [0], color='black', lw=2, linestyle='-', label='Median')
    ]

    # 3. CALL THE LEGEND WITH PROPER HANDLES
    ax.legend(handles=legend_elements, loc="upper right", frameon=True)
    # plt.legend(loc="center", handles=[mean_style, median_style],labels=["Mean","Median"])
    # Save high-quality figures
    plt.savefig(f"{filename}.png", dpi=600, bbox_inches='tight')
    plt.savefig(f"{filename}.pdf", bbox_inches='tight')

    plt.show()

# Prepare data and call the function
data = [df1['DS2(CAS2-1) [eV]'] , df2['DS2(CAS2-1) [eV]'] , df3['DS2(CAS2-1) [eV]'] , df4['DS2(CAS2-1) [eV]'] ]
labels = ['TN', 'FP', 'FN', 'TP']
#colors = ['skyblue', 'salmon', 'goldenrod', 'lightgreen']
colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

publication_boxplot(
    data=data,
    labels=labels,
    colors=colors,
    ylabel='DS2 energy (eV)',
    title='DS2 energy distribution for GNN_SE model',
    filename='ds2_comp_gnnse'
)

