"""Independently reconcile exported results to named raw Excel cells and FRED rows."""
from pathlib import Path
from decimal import Decimal
import math
import csv, io, json, zipfile
from openpyxl import load_workbook

root=Path(__file__).resolve().parent
price=load_workbook(root/'raw/ypdgdpQvQd.xlsx',data_only=True)['YPDGDP']
gap=load_workbook(root/'raw/gap.xlsx',data_only=True)['gap']
rows=list(csv.DictReader((root/'quarterly_taylor_comparison.csv').open()))
aligned=list(csv.DictReader((root/'quarter_end_taylor_comparison.csv').open()))
with zipfile.ZipFile(root/'raw/rates.csv') as z:
    fred=list(csv.DictReader(io.StringIO(z.read('daily,_7-day.csv').decode())))
    market=list(csv.DictReader(io.StringIO(z.read('daily.csv').decode())))
for row in rows:
    a=Decimal(str(price[row['price_cell'].split('!')[1]].value))
    b=Decimal(str(price[row['price_lag_cell'].split('!')[1]].value))
    g=Decimal(str(gap[row['gap_cell'].split('!')[1]].value))
    pi=100*(a/b-1)
    rate=Decimal(2)+pi+Decimal('.5')*(pi-2)+Decimal('.5')*g
    assert abs(rate-Decimal(row['taylor_pct']))<Decimal('0.000000001')
    year=int(row['quarter'][:4]); quarter=int(row['quarter'][-1])
    values=[Decimal(r['DFF']) for r in fred if int(r['observation_date'][:4])==year and (int(r['observation_date'][5:7])-1)//3+1==quarter and r['DFF']]
    assert abs(sum(values)/len(values)-Decimal(row['DFF']))<Decimal('0.000000001')
for row in aligned:
    quarter=row['quarter']; year=int(quarter[:4]); q=int(quarter[-1])
    dff=[r for r in fred if int(r['observation_date'][:4])==year and (int(r['observation_date'][5:7])-1)//3+1==q and r['DFF']]
    assert dff[-1]['observation_date']==row['DFF_quarter_end_date']
    assert abs(Decimal(dff[-1]['DFF'])-Decimal(row['DFF_quarter_end']))<Decimal('0.000000001')
    for series in ['DGS2','DGS10']:
        values=[r for r in market if int(r['observation_date'][:4])==year and (int(r['observation_date'][5:7])-1)//3+1==q and r[series]]
        assert values[-1]['observation_date']==row[series+'_quarter_end_date']
        assert abs(Decimal(values[-1][series])-Decimal(row[series+'_quarter_end']))<Decimal('0.000000001')
def corr(x,y):
    mx=sum(x)/len(x); my=sum(y)/len(y)
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/math.sqrt(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))
metric_rows={r['target']:r for r in csv.DictReader((root/'timing_alignment_metrics.csv').open())}
for series in ['DFF','DGS2','DGS10']:
    x=[float(r['taylor_pct']) for r in aligned]; y=[float(r[series+'_quarter_end']) for r in aligned]
    dx=[x[i]-x[i-1] for i in range(1,len(x))]; dy=[y[i]-y[i-1] for i in range(1,len(y))]
    m=metric_rows[series]
    assert abs(corr(x,y)-float(m['level_correlation']))<1e-9
    assert abs(corr(dx,dy)-float(m['change_correlation']))<1e-9
    assert abs(sum(a-b for a,b in zip(x,y))/len(x)-float(m['mean_taylor_minus_rate_pp']))<1e-9
coverage=json.loads((root/'recent_coverage_sources.json').read_text())
assert coverage['conclusion'].startswith('No PIT-safe')
assert gap.max_column > 1 and gap.cell(1,gap.max_column).value=='GBgap_201204'
result={'raw_cell_formula_reconciliation_rows':len(rows),'independent_calendar_DFF_mean_rows':len(rows),
    'independent_quarter_end_rows':len(aligned),'independent_quarter_end_series':['DFF','DGS2','DGS10'],
    'independent_timing_metrics':['mean_gap','level_correlation','change_correlation'],
    'recent_coverage_last_staff_vintage':'GBgap_201204',
    'absolute_tolerance_pp':1e-9,'status':'passed'}
(root/'independent_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
