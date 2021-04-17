import pandas as pd
import numpy as np
import os
import json
from collections import defaultdict
from pathlib import Path
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/first_db')


def clean_df(df):
    # remove non important columns
    columns = [x for x in df.columns.values if all(a not in x for a in ['_spe', '_cod', '_pgi', 'temps_effet'])]
    # reformat NaN values
    df = df.replace('Non Renseigné', np.NaN)
    df = df.replace('N/R', np.NaN)
    df = df.replace('NaN', np.NaN)
    # remove columns with one value
    for col in columns:
        if len(df[col].unique()) == 1:
            columns.remove(col)
    return df[columns]


def rmissingvaluecol(dff, threshold):
    l = []
    l = list(dff.drop(dff.loc[:, list((100 * (dff.isnull().sum() / len(dff.index)) >= threshold))].columns,
                      1).columns.values)
    print('Columns: ', list(set(list((dff.columns.values))) - set(l)))
    return l


def last_non_null(agg):
    new_agg = [a for a in agg if a not in [None, np.NAN]]
    if new_agg:
        return new_agg[-1]
    else:
        return agg[-1]


# read files
print('read files')
base_path = Path('input')
os.makedirs('output', exist_ok=True)


""" d_compte_client = pd.read_sql('select * from dwh_d_compte_client')
f_compte_client = pd.read_sql('select * from dwh_f_compte_client')
f_detail_menage = pd.read_sql('select * from dwh_f_detail_menage')
f_menage = pd.read_sql('select * from dwh_f_menage')
d_element_louable = pd.read_sql('select * from dwh_d_element_louable')
d_nature_elo = pd.read_sql('select * from dwh_d_nature_elo')
d_geographie = pd.read_sql('select * from dwh_d_geographie')
d_zonage = pd.read_sql('select * from dwh_d_zonage')
d_detail_contrat = pd.read_sql('select * from dwh_d_detail_contrat')
d_type_contrat = pd.read_sql('select * from dwh_d_type_contrat')
d_terme = pd.read_sql('select * from dwh_d_terme')
d_type_tarif = pd.read_sql('select * from dwh_d_type_tarif')
d_type_elo = pd.read_sql('select * from dwh_d_type_elo')
d_condition_location = pd.read_sql('select * from dwh_d_condition_location')
d_categorie_menage = pd.read_sql('select * from dwh_d_categorie_menage')
d_type_revenu = pd.read_sql('select * from dwh_d_type_revenu')
d_type_handicap = pd.read_sql('select * from dwh_d_type_handicap')
d_type_contrat_travail = pd.read_sql('select * from dwh_d_type_contrat_travail')
d_type_compte_client = pd.read_sql('select * from dwh_d_type_compte_client') """

d_compte_client = pd.read_sql('select * from dwh_d_compte_client', con=engine)
f_compte_client = pd.read_sql('select * from dwh_f_compte_client', con=engine)
f_detail_menage = pd.read_sql('select * from dwh_f_detail_menage', con=engine)
f_menage = pd.read_sql('select * from dwh_f_menage', con=engine)
d_element_louable = pd.read_sql('select * from dwh_d_element_louable', con=engine)
d_nature_elo = pd.read_sql('select * from dwh_d_nature_elo', con=engine)
d_geographie = pd.read_sql('select * from dwh_d_geographie', con=engine)
d_zonage = pd.read_sql('select * from dwh_d_zonage', con=engine)
d_detail_contrat = pd.read_sql('select * from dwh_d_detail_contrat', con=engine)
d_type_contrat = pd.read_sql('select * from dwh_d_type_contrat', con=engine)
d_terme = pd.read_sql('select * from dwh_d_terme', con=engine)
d_type_tarif = pd.read_sql('select * from dwh_d_type_tarif', con=engine)
d_type_elo = pd.read_sql('select * from dwh_d_type_elo', con=engine)
d_condition_location = pd.read_sql('select * from dwh_d_condition_location', con=engine)
d_categorie_menage = pd.read_sql('select * from dwh_d_categorie_menage', con=engine)
d_type_revenu = pd.read_sql('select * from dwh_d_type_revenu', con=engine)
d_type_handicap = pd.read_sql('select * from dwh_d_type_handicap', con=engine)
d_type_contrat_travail = pd.read_sql('select * from dwh_d_type_contrat_travail', con=engine)
d_type_compte_client = pd.read_sql('select * from dwh_d_type_compte_client', con=engine)
# clean tables
print('clean tables')
d_compte_client = clean_df(d_compte_client)
f_compte_client = clean_df(f_compte_client)
f_detail_menage = clean_df(f_detail_menage)
f_menage = clean_df(f_menage)
d_element_louable = clean_df(d_element_louable)
d_nature_elo = clean_df(d_nature_elo)
d_geographie = clean_df(d_geographie)
d_zonage = clean_df(d_zonage)
d_detail_contrat = clean_df(d_detail_contrat)
d_type_contrat = clean_df(d_type_contrat)
d_terme = clean_df(d_terme)
d_type_tarif = clean_df(d_type_tarif)
d_type_elo = clean_df(d_type_elo)
d_condition_location = clean_df(d_condition_location)

d_categorie_menage = clean_df(d_categorie_menage)
d_type_revenu = clean_df(d_type_revenu)
d_type_handicap = clean_df(d_type_handicap)
d_type_contrat_travail = clean_df(d_type_contrat_travail)
d_type_compte_client = clean_df(d_type_compte_client)

# get important columns for each data table
print('get important columns for each data table')
columns = ['zonage_id', 'zonage_zone_sensible_lib', 'zonage_zone_loyer_lib', 'zonage_zone_apl_lib']
d_zonage = d_zonage[columns]

columns = ['cnc_id', 'type_cnc_id', 'cond_loc_id', 'type_trf_id', 'terme_id', 'cnc_dtdval', 'cnc_dtfval',
           'cnc_dteff', 'cnc_tem_al', 'cnc_tem_apl', 'cnc_tem_sls']
d_detail_contrat = d_detail_contrat[columns]

columns = ['compte_client_id', 'elo_id', 'type_ccl_id', 'cnc_id', 'compte_client_ref', 'compte_client_ind_parti']
d_compte_client = d_compte_client[columns]

columns = ['elo_id', 'nature_elo_id', 'type_elo_id', 'geo_id', 'zonage_id', 'elo_lib', 'elo_acceshand', 'elo_curval',
           'elo_dtf_construction', 'elo_categ_financement_inii', 'elo_etage', 'elo_mode_chauffage',
           'elo_type_chauffage', 'elo_tem_handicap', 'elo_type_construction']
d_element_louable = d_element_louable[columns]

columns = ['compte_client_id', 'd_compte_client_id', 'temps_arrete_id', 'nb_comptactifs_std', 'nb_comptes_factures_std',
           'nb_comptes_recouvres_std', 'nb_debiteurs_std', 'nb_crediteurs_std', 'nb_a_zero_std',
           'mnt_ttc_facture_ccl_std', 'mnt_ttc_echeance_std', 'mnt_loyer_ccl_std', 'mnt_charges_ccl_std',
           'mnt_caution_dg_ccl_std', 'mnt_aides_ccl_std', 'mnt_sls_ccl_std', 'mnt_solde_charges_ccl_std',
           'mnt_total_encaisse_std', 'solde_std', 'solde_crediteur_std', 'solde_debiteur_std', 'dette_du_mois_std',
           'dette_moins_3mois_std', 'dette_plus_3_a_6_mois_std', 'dette_plus_6_a_12_mois_std', 'dette_plus_12_mois_std',
           'nb_dette_sup_echeance_std', 'nb_dette_inf_1_an_std', 'nb_nouveaux_en_dette_std', 'solde_derjr_hquitt_std',
           'mnt_rls_regul_std']
f_compte_client = f_compte_client[columns]

columns = ['detail_menage_id', 'temps_arrete_id', 'elo_id', 'type_revenu_id', 'age_std',
           'mnt_ressource_mensuel_std', 'mnt_ressource_annuel_std', 'nb_csp_std', 'nb_handicape_std']
f_detail_menage = f_detail_menage[columns]

columns = ['menage_id', 'temps_arrete_id', 'cat_menage_id', 'cnc_id', 'elo_id', 'age_std', 'nb_seul_std',
           'nb_celibataire_std', 'nb_marie_std', 'nb_concubin_std', 'nb_veuf_std', 'nb_divorce_std', 'nb_separe_std',
           'nb_pacse_std', 'nbr_enfant_std', 'nb_menage_autre_std', 'nb_monoparental_std', 'nb_couple_av_enf_std',
           'nb_couple_ss_enf_std', 'nbr_occupant_menage_std', 'nb_recent_std', 'nb_al_std', 'nb_apl_std', 'nb_sls_std',
           'mnt_revenu_imp_n_std', 'mnt_revenu_imp_n1_std', 'mnt_plafond_plus_std', 'mnt_ressource_mensuel_std']
f_menage = f_menage[columns]

# merge element louable with nature elo, geo et zonage
print('merge element louable with nature elo, type elo, geo, et zonage')
elo_info = pd.merge(left=d_element_louable, right=d_nature_elo, on='nature_elo_id')
elo_info = pd.merge(left=elo_info, right=d_geographie, on='geo_id')
elo_info = pd.merge(left=elo_info, right=d_zonage, on='zonage_id')
elo_info = pd.merge(left=elo_info, right=d_type_elo, on='type_elo_id')
# elo_info = elo_info[elo_info.type_elo_id.isin([1, 2, 4, 5, 6, 7, 8, 9, 13, 16, 17, 18, 20, 21, 24, 25, 26, 27, 29,
# 31, 33, 34, 35, 37, 38, 39, 40])]

# remove columns with more than 98% of missing values
print('remove columns with more than 98% of missing values for elo_info')
l = rmissingvaluecol(elo_info, 98)
elo_info = elo_info[l]
elo_info = clean_df(elo_info)

# merge detail contrat with type contrat, terme, type tarif et condition location
print('merge detail contrat with type contrat, terme, type tarif et condition location')
contrat_info = pd.merge(left=d_detail_contrat, right=d_type_contrat, on='type_cnc_id')
contrat_info = pd.merge(left=contrat_info, right=d_terme, on='terme_id')
contrat_info = pd.merge(left=contrat_info, right=d_type_tarif, on='type_trf_id')
contrat_info = pd.merge(left=contrat_info, right=d_condition_location, on='cond_loc_id')
contrat_info = contrat_info[contrat_info.type_cnc_id == 5]

# remove columns with more than 98% of missing values
print('remove columns with more than 98% of missing values for contrat_info')
l = rmissingvaluecol(contrat_info, 98)
contrat_info = contrat_info[l]
contrat_info = clean_df(contrat_info)

# create a mapping of compte_client_ids for all clients (identified by ref + elo_id)
print('create dictionary of compte_client_ids for all clients (identified by ref + elo_id)')
cols_to_keep = ['compte_client_ref', 'elo_id', 'cnc_id', 'compte_client_id']
mapping_client = d_compte_client[cols_to_keep]
mapping_client = mapping_client.groupby(['compte_client_ref', 'elo_id']).agg(list).reset_index()

id_compte_mapping = {}
for l_ids in mapping_client.compte_client_id:
    for id_n in l_ids:
        id_compte_mapping[id_n] = l_ids[-1]

id_cnc_mapping = {}
for a in mapping_client.cnc_id:
    for id_n in a:
        id_cnc_mapping[id_n] = a[-1]

# replace different compte_client_id values to corresponding mapping value in d_compte_client and f_compte_client
print('replace different compte_client_id values to corresponding mapping value in d_compte_client and f_compte_client')
d_compte_client['compte_client_id'] = d_compte_client.compte_client_id.apply(lambda x: id_compte_mapping.get(x, x))
f_compte_client['d_compte_client_id'] = f_compte_client.d_compte_client_id.apply(lambda x: id_compte_mapping.get(x, x))

# merge f_compte_client with d_compte_client
print('merge f_compte_client with d_compte_client')
client_info = pd.merge(left=f_compte_client, right=d_compte_client, left_on='d_compte_client_id',
                       right_on='compte_client_id')
# select only 'locataires'
client_info = client_info[client_info.type_ccl_id == 3]

# remove columns with more than 98% of missing values
print('remove columns with more than 98% of missing values for client_info')
l = rmissingvaluecol(client_info, 98)
client_info = client_info[l]
client_info = clean_df(client_info)
print(client_info.shape)

# merge f_menage with f_detail_menage
print('merge f_menage with d_categorie_menage and f_detail_menage')
f_detail_menage = pd.merge(left=f_detail_menage, right=d_type_revenu, on=['type_revenu_id'])
f_menage = pd.merge(left=f_menage, right=d_categorie_menage, on=['cat_menage_id'])
menages = pd.merge(left=f_menage, right=f_detail_menage, on=['elo_id'])

# merge menages with contrat_info
print('merge menages with contrat_info')
menages = pd.merge(left=menages, right=contrat_info, on='cnc_id')
print(menages.shape)

# merge menages with elo_info
print('merge menages with elo_info')
menages = pd.merge(left=menages, right=elo_info, on='elo_id')
print(menages.shape)

# remove columns with more than 98% of missing values
print('remove columns with more than 98% of missing values for menages')
l = rmissingvaluecol(menages, 98)
menages = menages[l]
menages = clean_df(menages)

# replace different cnc_id values to corresponding mapping value in menages and client_info
print('replace different cnc_id values to corresponding mapping value in menages and client_info')
menages['cnc_id'] = menages.cnc_id.apply(lambda x: id_cnc_mapping.get(x, x))
client_info['cnc_id'] = client_info.cnc_id.apply(lambda x: id_cnc_mapping.get(x, x))

# merge menages with client_info
print('merge menages with client_info')
clients_menages = pd.merge(left=client_info, right=menages, left_on=['elo_id', 'temps_arrete_id', 'cnc_id'],
                           right_on=['elo_id', 'temps_arrete_id_y', 'cnc_id'])

# delete duplicae rows
print('with duplicates in clients_menages', clients_menages.shape)
clients_menages.drop_duplicates(subset=['elo_id', 'temps_arrete_id', 'cnc_id', 'd_compte_client_id'],
                                inplace=True)
print('without duplicates in clients_menages', clients_menages.shape)

# remove columns with more than 98% of missing values
print('remove columns with more than 98% of missing values for clients_menages')
l = rmissingvaluecol(clients_menages, 98)
clients_menages = clients_menages[l]
clients_menages = clean_df(clients_menages)

# delete redundant columns in clients_menages
print('delete redundant columns in clients_menages')
columns = [x for x in clients_menages.columns.values if all(a not in x
                                                            for a in ['compte_client_id_x', 'compte_client_id_y',
                                                                      'temps_arrete_id_x', 'temps_arrete_id_y',
                                                                      'elo_id_y', 'age_std_y', 'detail_menage_id',
                                                                      'menage_id', 'geo_id', 'cnc_id', 'type_elo_id',
                                                                      'type_ccl_id', 'dette_moins_3mois_std',
                                                                      'cat_menage_id', 'type_revenu_id'])]
clients_menages = clients_menages[columns]

# get clients_menages stat info
print('get clients_menages stat info')
set_client = set(clients_menages.d_compte_client_id.tolist())
print(clients_menages.shape, len(set_client))

# create and get clients_en_dette stat info
print('create and get clients_en_dette stat info')
clients_en_dette = clients_menages[(clients_menages.solde_debiteur_std != 0)]
set_dette_client = set(clients_en_dette.d_compte_client_id.tolist())
print(clients_en_dette.shape, len(set_dette_client))

# replace missing values (to verify for each case later)
print('replace missing values (to verify for each case later)')
clients_menages.fillna(-1, inplace=True)
clients_menages_to_history = defaultdict(list)

# dictionary of clients' history with client id as key
print('create clients_menages_to_history dict')
for a in clients_menages.to_dict('records'):
    clients_menages_to_history[a['d_compte_client_id']].append(a)

# save clients' history
print('save clients_menages_to_history to json')
with open('OUTDATED/output\clients_menages_to_history.json', 'w', encoding='utf-8') as fp:
    json.dump(clients_menages_to_history, fp, indent=4, ensure_ascii=False)

# select only clients en dette
print('create clients_en_dette_to_history dict')
clients_en_dette_to_history = {k: v for k, v in clients_menages_to_history.items() if k in set_dette_client}

# save clients en dette history
print('save clients_en_dette_to_history to json')
with open('OUTDATED/output\clients_en_dette_to_history.json', 'w', encoding='utf-8') as fp:
    json.dump(clients_en_dette_to_history, fp, indent=4, ensure_ascii=False)