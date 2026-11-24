"""Load the two Text-Fabric corpora used throughout the project.

BHSA 2021  : ETCBC Biblia Hebraica Stuttgartensia Amstelodamensis (MT, Leningrad codex)
DSS 2.0.5  : Abegg/Bowley/Cook Dead Sea Scrolls morphology, converted by ETCBC
"""
import os
from tf.fabric import Fabric

BASE = os.path.expanduser("~/text-fabric-data/github/ETCBC")

def load_bhsa(features=None):
    TF = Fabric(locations=f"{BASE}/bhsa/tf/2021", silent="deep")
    feats = features or ("book chapter verse lex g_cons g_word_utf8 g_cons_utf8 language sp vt vs ps nu gn st "
                         "prs pfm vbs vbe uvf nme qere qere_utf8 kq_hybrid gloss function typ rela code freq_lex lex_utf8 "
                         "g_lex_utf8 g_prs_utf8 g_pfm_utf8 g_vbs_utf8 g_vbe_utf8 g_nme_utf8 g_uvf_utf8 g_prs g_pfm g_vbs g_vbe g_nme g_uvf g_lex txt domain pdp ls")
    api = TF.load(feats, silent="deep")
    return api

def load_dss(features=None):
    TF = Fabric(locations=f"{BASE}/dss/tf/2.0.5", silent="deep")
    feats = features or ("scroll fragment line book chapter verse biblical lang lex glex full fulle glyph sp cl ps gn nu st vs vt md "
                         "type morpho lex_etcbc sp_etcbc vs_etcbc vt_etcbc lang_etcbc g_cons g_pfm_etcbc g_prs_etcbc g_vbs_etcbc g_vbe_etcbc g_nme_etcbc unc rec cor alt vac")
    api = TF.load(feats, silent="deep")
    return api
