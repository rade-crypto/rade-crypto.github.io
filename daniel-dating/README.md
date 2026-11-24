# Dating the Book of Daniel from its own text

A reproducible, data-driven study of whether the historical prophecies of Daniel (kingdoms and events,
not messianic passages) read like a 6th-century BCE composition or a later one. It works only from
primary data: the Hebrew/Aramaic text, dated comparison corpora, and ancient historical sources.

## Data (downloaded, not committed)
- ETCBC BHSA 2021 (Masoretic text, full morphology/syntax) - `~/text-fabric-data/github/ETCBC/bhsa/tf/2021`
- ETCBC DSS 2.0.5 (Abegg/Bowley/Cook Dead Sea Scrolls morphology) - `~/text-fabric-data/github/ETCBC/dss/tf/2.0.5`
- Perseus canonical-greekLit + First1KGreek + papyri.info (Greek attestation search)

## Scripts (`scripts/`)
| script | question |
|---|---|
| `aramaic_features.py` | Where does Daniel's Aramaic sit between Ezra (Achaemenid) and Qumran Aramaic? Includes the Qumran MSS of Daniel as a test of scribal "modernisation". |
| `aramaic_wordorder.py` | Object-verb vs verb-object order, Ezra vs Daniel |
| `hebrew_chronolect.py [full|function]` | Ridge-regression date model and period classifier for Hebrew, validated leave-one-text-out, with DSS copies of classical books as an annotation control |
| `hebrew_variables.py` | Choice-based linguistic variables (genre-neutral) |
| `prophecy_claims.py` | Claim-by-claim check of Dan 8 and 11 against ancient sources; resolution (words per decade) and Bayesian change-point |
| `loans_names_intertext.py` | Persian/Greek loanwords, Nebuchadnezzar spellings, 'Chaldeans', text reuse |
| `calendar_math.py` | 1,150 / 1,290 / 1,335 days against the Maccabean dates |
| `greek/` | Greek corpus search for συμφωνία, ψαλτήριον, κίθαρις |

Run with a venv that has `text-fabric pandas numpy scipy scikit-learn`.
