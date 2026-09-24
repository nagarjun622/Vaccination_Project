from pathlib import Path
import pandas as pd, numpy as np, sqlite3, json, re
base=Path.cwd(); data=base/'work'/'vaccination_project'/'Vaccination project'; out=base/'outputs'; clean=out/'cleaned_data'; out.mkdir(exist_ok=True); clean.mkdir(exist_ok=True)
files={'coverage':'coverage-data.xlsx','incidence':'incidence-rate-data.xlsx','cases':'reported-cases-data.xlsx','introduction':'vaccine-introduction-data.xlsx','schedule':'vaccine-schedule-data.xlsx'}
tables={}; audit=[]
for name,file in files.items():
 raw=pd.read_excel(data/file); df=raw.copy(); df.columns=[re.sub(r'[^a-z0-9]+','_',str(c).lower()).strip('_') for c in df.columns]; df=df.drop_duplicates().copy()
 for c in ['year','target_number','doses','coverage','incidence_rate','cases','schedule_rounds']:
  if c in df: df[c]=pd.to_numeric(df[c],errors='coerce')
 for c in ['code','iso_3_code']:
  if c in df: df[c]=df[c].astype('string').str.strip().str.upper()
 tables[name]=df; audit.append({'table':name,'source_file':file,'rows':len(df),'columns':len(df.columns),'exact_duplicates_removed':len(raw)-len(df),'missing_cells':int(df.isna().sum().sum()),'year_min':int(df.year.min()) if 'year' in df and df.year.notna().any() else None,'year_max':int(df.year.max()) if 'year' in df and df.year.notna().any() else None})
coverage,incidence,cases,introduction,schedule=[tables[k] for k in files]
admin=coverage[coverage.coverage_category.astype('string').str.upper().str.contains('ADMIN',na=False)].copy(); admin=admin[admin.coverage.notna()&admin.year.notna()].copy()
incidence['disease_norm']=incidence.disease.astype('string').str.upper().str.replace(r'[^A-Z0-9]+','_',regex=True)
country_cov=admin.groupby(['code','name','year','antigen'],dropna=False).coverage.mean().reset_index()
year_cov=admin.groupby(['year','antigen']).coverage.agg(['mean','median','count']).reset_index()
intro=introduction.copy(); intro['is_yes']=intro.intro.astype('string').str.casefold().eq('yes'); region_intro=intro.groupby(['who_region','description','year'],dropna=False).is_yes.mean().mul(100).rename('introduced_pct').reset_index()
pairs={'MEASLES':['MEASLES','MCV1','MCV2'],'POLIO':['POL3','IPV1','IPV2'],'DIPHTHERIA':['DTP1','DTP3','DIPHCV1','DIPHCV3'],'HEPATITIS_B':['HEPB3','HEPB_BD'],'TUBERCULOSIS':['BCG'],'RUBELLA':['RUBELLA','RCV1']}; parts=[]
for disease,ants in pairs.items():
 dv=incidence[incidence.disease_norm.str.contains(disease,na=False)]
 for antigen in ants:
  cv=country_cov[country_cov.antigen.astype('string').str.upper().eq(antigen)]
  if len(cv) and len(dv):
   m=cv.merge(dv[['code','year','disease','incidence_rate','denominator']],on=['code','year'],how='inner');m['antigen']=antigen;parts.append(m)
assoc=pd.concat(parts,ignore_index=True) if parts else pd.DataFrame(columns=['coverage','incidence_rate'])
rho=float(assoc[['coverage','incidence_rate']].corr(method='spearman').iloc[0,1]) if len(assoc)>2 and assoc.coverage.nunique()>1 and assoc.incidence_rate.nunique()>1 else float('nan')
summary={'coverage_source_rows':len(coverage),'admin_usable_rows':len(admin),'admin_year_min':int(admin.year.min()),'admin_year_max':int(admin.year.max()),'countries':int(admin.code.nunique()),'antigens':int(admin.antigen.nunique()),'coverage_median':float(admin.coverage.median()),'coverage_below_95_pct':float((admin.coverage<95).mean()*100),'coverage_source_missing_pct':float(coverage.coverage.isna().mean()*100),'introduction_rows':len(introduction),'schedule_rows':len(schedule),'incidence_rows':len(incidence),'case_rows':len(cases),'matched_candidate_pairs':len(assoc),'candidate_spearman_rho':rho}
for n,d in tables.items():d.to_csv(clean/f'{n}.csv',index=False,encoding='utf-8-sig')
derived={'coverage_admin':admin,'coverage_by_year_antigen':year_cov,'introduction_by_region':region_intro,'candidate_coverage_incidence':assoc}
for n,d in derived.items():d.to_csv(clean/f'{n}.csv',index=False,encoding='utf-8-sig')
db=out/'vaccination_analysis.sqlite'
if db.exists():db.unlink()
with sqlite3.connect(db) as con:
 for n,d in tables.items():d.to_sql(n,con,index=False,if_exists='replace')
 for n,d in derived.items():d.to_sql(n,con,index=False,if_exists='replace')
(out/'data_quality_summary.json').write_text(json.dumps({'inputs':audit,'summary':summary,'association_pairs':pairs,'association_interpretation':'Ecological, descriptive only; no causal inference.'},indent=2,default=str),encoding='utf-8')
print(json.dumps({'summary':summary,'audit':audit},indent=2,default=str))
