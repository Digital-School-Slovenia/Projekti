from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    base = Path(__file__).parent
    avg = pd.read_csv(base / 'avgIQpercountry.csv')
    iqc = pd.read_csv(base / 'iq_classification.csv', sep=';')

    avg['Average IQ'] = pd.to_numeric(avg['Average IQ'], errors='coerce')
    avg['HDI (2021)'] = pd.to_numeric(avg.get('HDI (2021)'), errors='coerce')

    percent_column = [c for c in iqc.columns if 'Percent' in c][0]
    iqc['percent'] = (
        iqc[percent_column].astype(str)
        .str.replace('%', '', regex=False)
        .str.replace('<', '', regex=False)
        .str.strip()
        .replace('', '0')
        .astype(float)
    )

    out_dir = base / 'plots'
    out_dir.mkdir(exist_ok=True)
    saved_files = []

    filepath = out_dir / 'histogram_povprecni_iq.png'
    plt.figure(figsize=(8, 5))
    plt.hist(avg['Average IQ'].dropna(), bins=20, color='#4C72B0', edgecolor='black')
    plt.title('Porazdelitev povprečnega IQ')
    plt.xlabel('Povprečni IQ')
    plt.ylabel('Število držav')
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()
    saved_files.append(filepath.name)

    filepath = out_dir / 'top15_povprecni_iq.png'
    top15 = avg.nlargest(15, 'Average IQ').sort_values('Average IQ')
    plt.figure(figsize=(8, 6))
    plt.barh(top15['Country'], top15['Average IQ'], color='#55A868')
    plt.title('Top 15 držav po povprečnem IQ')
    plt.xlabel('Povprečni IQ')
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()
    saved_files.append(filepath.name)

    if 'Continent' in avg.columns:
        cont = avg.dropna(subset=['Continent', 'Average IQ'])
        groups = [cont.loc[cont['Continent'] == c, 'Average IQ'] for c in cont['Continent'].unique()]
        filepath = out_dir / 'boxplot_iq_po_kontinentih.png'
        plt.figure(figsize=(10, 6))
        plt.boxplot(groups, tick_labels=cont['Continent'].unique(), patch_artist=True)
        plt.xticks(rotation=45)
        plt.title('Povprečni IQ po kontinentih')
        plt.ylabel('Povprečni IQ')
        plt.tight_layout()
        plt.savefig(filepath)
        plt.close()
        saved_files.append(filepath.name)

    if 'Classification' in iqc.columns:
        labels = iqc['Classification'].astype(str)
        sizes = iqc['percent']
        filepath = out_dir / 'tortni_graf_iq_razredi.png'
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Deleži razredov IQ')
        plt.tight_layout()
        plt.savefig(filepath)
        plt.close()
        saved_files.append(filepath.name)

    print('Ustvarjene so bile naslednje slike:')
    for image_file in saved_files:
        print(f' - {image_file}')


if __name__ == '__main__':
    main()


