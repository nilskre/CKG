#Database directory
databasesDir = "/Users/albertosantos/Development/Clinical_Proteomics_Department/ClinicalKnowledgeGraph(CKG)/data/databases/"
#Databases
databases = [
            "Internal",
            "HGNC", 
            "RefSeq", 
            "UniProt", 
            "IntAct", 
            "DisGEnet", 
            "HGNC", 
            'DrugBank',
            "DGIdb", 
            "OncoKB", 
            "STRING", 
            #"STITCH", 
            "Mentions", 
            "OncoKB",
            "CancerGenomeInterpreter", 
            "SIDER",
            "HMDB",
            "PathwayCommons",
            'GWASCatalog'
            ]

sources = {
            "Drug":"DrugBank",
            "Metabolite":"HMDB",
            "Protein":"UniProt",
            "Gene":"HGNC"    
            }

###### UniProt Database ########
uniprot_id_url = "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/HUMAN_9606_idmapping.dat.gz"
uniprot_id_file = "/Users/albertosantos/Development/UniProt/HUMAN_9606_idmapping.dat"
uniprot_text_file = "/Users/albertosantos/Development/UniProt/uniprot-human.tab" #### Downloaded manually from UniProt until we know url (organism:human AND reviewed:yes)
uniprot_variant_file = "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/variants/homo_sapiens_variation.txt.gz"
uniprot_unique_peptides_file = "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/proteomics_mapping/UP000005640_9606_uniquePeptides.tsv"
uniprot_ids = ["UniProtKB-ID", 
                "NCBI_TaxID", 
                "Gene_Name", 
                "RefSeq", 
                "PDB", 
                "STRING", 
                "KEGG", 
                "Reactome", 
                "HPA", 
                "ChEMBL", 
                "Ensembl"]
uniprot_synonyms = ["UniProtKB-ID", 
                    "Gene_Name", 
                    "STRING", 
                    "HPA", 
                    "Ensembl", 
                    "ChEMBL", 
                    "PDB"]
uniprot_protein_relationships = {"KEGG": ("Pathway", "IS_PART_OF_KEGG_PATHWAY"), 
                                "Reactome":("Pathway","IS_PART_OF_REACTOME_PATHWAY"), 
                                "RefSeq": ("Transcript", "TRANSLATED_INTO"), 
                                "Gene_Name":("Gene","TRANSLATED_INTO"),
                                             "PDB":("Structure","FOUND")
                                }
##### HUGO Gene Nomenclature #######
hgnc_url = "ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/tsv/hgnc_complete_set.txt"
##### RefSeq #########
refseq_url = "ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/GCF_000001405.37_GRCh38.p11/GCF_000001405.37_GRCh38.p11_feature_table.txt.gz"
headerEntities = {"Transcript":["ID", ":LABEL", "name", "class", "assembly", "taxid"], 
                "Chromosome":["ID", ":LABEL", "name", "taxid"],
                "LOCATED_IN": ['START_ID', 'END_ID','TYPE','start','end','strand', 'source'],
                "TRANSCRIBED_INTO": ['START_ID', 'END_ID','TYPE', 'source']}
###### PathwayCommons Database #######
pathwayCommons_pathways_url = "http://www.pathwaycommons.org/archives/PC2/v9/PathwayCommons9.All.uniprot.gmt.gz"
pathway_type = -45
##### Reactome ######
reactome_urls = {"pathways" : "https://reactome.org/download/current/ReactomePathways.txt",
                "hierarchy" : "https://reactome.org/download/current/ReactomePathwaysRelation.txt",
                "protein_pathways" : "https://reactome.org/download/current/UniProt2Reactome_All_Levels.txt"}
###### The Drug Gene Interaction Database (DGIdb) #########
DGIdb_url = "http://www.dgidb.org/data/interactions.tsv"
###### OncoKB Database #########
OncoKB_annotated_url = "http://oncokb.org/api/v1/utils/allAnnotatedVariants.txt"
OncoKB_actionable_url = "http://oncokb.org/api/v1/utils/allActionableVariants.txt"
OncoKB_levels = {"1": ("approved", "Responsive"), 
                "2A": ("approved","Responsive"), 
                "2B": ("approved", "Responsive other"), 
                "3A": ("Clinical evidence", "Responsive"), 
                "3B":("Clinical evidence", "Responsive other"), 
                "4":("Biological evidence","Responsive"), 
                "4B":("FDA approved","Resistant")}

##### Cancer Genome Interpreter ######
cancerGenes_url = "https://www.cancergenomeinterpreter.org/data/catalog_of_cancer_genes_latest.zip"
cancerVariants_url = "https://www.cancergenomeinterpreter.org/data/catalog_of_validated_oncogenic_mutations_latest.zip"
cancerBioactivities_url = "https://www.cancergenomeinterpreter.org/data/cancer_bioactivities_latest.zip"

cancerBiomarkers_url = "https://www.cancergenomeinterpreter.org/data/cgi_biomarkers_latest.zip"
cancerBiomarkers_variant_file = "cgi_biomarkers_per_variant.tsv"

###### IntAct Database #######
intact_psimitab_url = "ftp://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/intact.txt"
intact_file = "Intact/intact/intact.txt"
###### STRING database #######
STRING_cutoff = 0.4
STRING_mapping_url = "https://stringdb-static.org/download/protein.aliases.v10.5/9606.protein.aliases.v10.5.txt.gz"
STRING_url = "https://stringdb-static.org/download/protein.links.detailed.v10.5/9606.protein.links.detailed.v10.5.txt.gz"
###### STITCH database #######
STITCH_url = "http://stitch.embl.de/download/protein_chemical.links.detailed.v5.0/9606.protein_chemical.links.detailed.v5.0.tsv.gz"
##### DisGeNet Database ######
disgenet_url = "http://www.disgenet.org/ds/DisGeNET/results/"
disgenet_files = {"gene_curated":"curated_gene_disease_associations.tsv.gz",
                    "gene_befree": "befree_gene_disease_associations.tsv.gz",
                    "variant_curated":"curated_variant_disease_associations.tsv.gz",
                    "variant_befree":"befree_variant_disease_associations.tsv.gz"
                }
disgenet_mapping_files = {"protein_mapping":"mapa_geneid_4_uniprot_crossref.tsv.gz",
                            "disease_mapping":"disease_mappings.tsv.gz"
                        }

##### Human Metabolome Database #######
HMDB_url = "http://www.hmdb.ca/system/downloads/current/hmdb_metabolites.zip"
HMDB_DO_source = "OMIM"
HMDB_dictionary_file = "mapping.tsv"
HMDB_fields = ['accession', 
                'name', 
                'description',
                'chemical_formula', 
                'average_molecular_weight', 
                'monoisotopic_molecular_weight', 
                'status',
                'origin',
                'drugbank_id', 
                'foodb_id', 
                'knapsack_id', 
                'chemspider_id', 
                'biocyc_id', 
                'bigg_id', 
                'wikipidia', 
                'mugowiki', 
                'mutagene', 
                'metlin_id', 
                'pubchem_compound_id',
                'het_id', 
                'chebi_id',
                'tissue',
                'cellular_location'] 
HMDB_parentFields = ['synonyms',
                    'origins', 
                    'taxonomy',
                    'cellular_locations', 
                    'biofluid_locations',
                    'tissue_locations', 
                    'pathways', 
                    'diseases',
                    'general_references',
                    'protein_associations']
HMDB_structures = {"pathways": ["smpdb_id"], 
                    "diseases":["omim_id"],
                    "synonyms":["synonym"],
                    'protein_associations':["uniprot_id"],
                    "cellular_locations":["cellular_location"], 
                    "biofluid_locations":["biofluid"],
                    "general_references":["pubmed_id"],
                    "taxonomy":['direct_parent', 'kingdom', 'super_class', 'class', 'sub_class']
                  }
HMDB_associations = {"pathways": ("ANNOTATED_IN_PATHWAY","hmdb_annotated_in_pathway"), 
                    "diseases": ("ASSOCIATED_WITH", "hmdb_associated_with_disease"), 
                    'protein_associations': ("ASSOCIATED_WITH", "hmdb_associated_with_protein"),
                    "cellular_locations": ("ASSOCIATED_WITH", "hmdb_associated_with_cellular_location"), 
                    "biofluid_locations": ("ASSOCIATED_WITH","hmdb_associated_with_biofluid_location"),
                    "general_references": ("MENTIONED_IN_PUBLICATION","Metabolite_Publication_mentioned_in_publication"),
                    "tissue_locations":("ASSOCIATED_WITH","hmdb_associated_with_tissue")
                    }

HMDB_attributes = ['name', 
                   'description',
                   'direct_parent',
                   'kingdom', 
                   'super_class', 
                   'class', 
                   'sub_class', 
                   'chemical_formula', 
                   'average_molecular_weight', 
                   'monoisotopic_molecular_weight', 
                   'pubchem_compound_id',
                   'food_id',
                   'status',
                   'knapsack_id', 
                   'chemspider_id', 
                   'biocyc_id', 
                   'bigg_id', 
                   'wikipidia', 
                   'mugowiki', 
                   'mutagene', 
                   'metlin_id', 
                   'het_id', 
                   'chebi_id',
                   'synonyms']

###### Drug bank ########
DrugBank_url = "https://www.drugbank.ca/releases/5-1-1/downloads/drugbank_all_full_database.xml.zip" ## Manual download need to login
DrugBank_vocabulary_url = "https://www.drugbank.ca/releases/5-1-1/downloads/drugbank_all_drugbank_vocabulary.csv.zip"
DrugBank_dictionary_file = "mapping.tsv"
DrugBank_fields = ['drugbank-id', 
                'name', 
                'description',  
                'group', 
                'indication',
                'price',
                'pharmacodynamics', 
                'mechanism-of-action', 
                'toxicity', 
                'metabolism', 
                'absorption', 
                'half-life',
                'route-of-elimination',
                'kingdom', 
                'superclass', 
                'class', 
                'subclass'] 
DrugBank_parentFields = ['groups',
                    'prices', 
                    'pathways', 
                    'pathways', 
                    'articles',
                    'drug-interactions',
                    'experimental-properties',
                    'external-identifiers',
                    'targets',
                    'enzymes',
                    'snp-effects',
                    'snp-adverse-drug-reactions'
                    ]
DrugBank_structures = {"general-references": ["pubmed-id"], 
                    "drug-interactions":["drugbank-id","description"],
                    "experimental-properties":["kind", "value"],
                    'external-identifiers':["identifier"],
                    "pathways":["smpdb-id"], 
                    "targets":["resource","identifier"],
                    "prices":["cost"],
                    "snp-effects":["gene-symbol", "rs-id", "description"],
                    'snp-adverse-drug-reactions':["gene-symbol","rs-id","desciption"]
                  }

DrugBank_attributes = ['name', 
                   'description',  
                   'indication',
                   'mechanism-of-action',
                   'metabolism',
                   'pharmacodynamics',
                   'prices',
                   'route-of-elimination',
                   'toxicity',
                   'synonyms',
                   'absorption',
                   #'alt_drugbank-id',
                   'half-life',
                   'groups',
                   'experimental-properties'# NEEDS TO BE THE LAST ATTRIBUTE
                   ]
DrugBank_exp_prop = [
                    "Melting Point",
                    "Hydrophobicity",
                    "Isoelectric Point",
                    "Molecular Weight",
                    "Molecular Formula",
                    "Water Solubility",
                    "Monoisotopic Weight",
                    "Polar Surface Area (PSA)",
                    "Refractivity",
                    "Polarizability",
                    "Rotatable Bond Count",
                    "H Bond Acceptor Count",
                    "H Bond Donor Count",
                    "pKa (strongest acidic)",
                    "pKa (strongest basic)",
                    "Physiological Charge",
                    "Number of Rings",
                    "Bioavailability",
                    "Rule of Five",
                    "Ghose Filter",
                    "MDDR-Like Rule",
                    "caco2 Permeability",
                    "pKa",
                    "Boiling Point"
                    ]

DrugBank_associations = {"pathways": ("ANNOTATED_IN_PATHWAY","drugbank_annotated_in_pathway"), 
                    'targets': ("ASSOCIATED_WITH", "drugbank_targets_protein"),
                    "drug-interactions": ("ASSOCIATED_WITH", "drugbank_interacts_with_drug"), 
                    }


##### Internal Databases (jensenlab.org) #####
internal_db_directory = databasesDir + "InternalDatabases/"
internal_db_url = "http://download.jensenlab.org/FILE"
internal_db_files = {"-26":"human_disease_integrated_full.tsv", 
                    "-25":"human_tissue_integrated_full.tsv",
                    "-23":"human_compartment_integrated_full.tsv"}
internal_db_mentions_files = {"-26":"disease_textmining_mentions.tsv", 
                    "-25":"tissue_textmining_mentions.tsv",
                    "-23":"compartment_textmining_mentions.tsv",
                    "9606": "human_textmining_mentions.tsv",
                    "-1": "chemical_textmining_mentions.tsv"}
internal_db_types = {"-26":("Protein","Disease"),
                    "-25":("Protein","Tissue"),
                    "-23":("Protein","Cellular_compartment")}
internal_db_mentions_types = {"-26":("Disease", "Publication"),
                            "-25":("Tissue", "Publication"),
                            "-23":("Cellular_compartment", "Publication"), 
                            "9606":("Protein","Publication"), 
                            "-1":("Chemical","Publication")}
internal_db_mentions_filters = {"-25": ["BTO:0000000"],
                                "-26": ["DOID:4", "DOID:162"],
                                "-23":["GO:0005575", "GO:0005623", "GO:0044464", "GO:0030054"]}
internal_db_sources = {"-25": "TISSUES", "-26": "DISEASES", "-23": "COMPARTMENTS"}

#### SIDER database #####
SIDER_url = "http://sideeffects.embl.de/media/download/meddra_all_label_se.tsv.gz"
SIDER_source = "UMLS_CUI"

#### Pubmed ######
PMC_db_url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/PMC-ids.csv.gz"
PMC_fields = ["PMID","Journal Title","ISSN","Year","Volume","Issue","Page","DOI","PMCID"]
pubmed_linkout = "https://www.ncbi.nlm.nih.gov/pubmed/PUBMEDID"


#### GWAS Catalog #####
GWASCat_url = "https://www.ebi.ac.uk/gwas/api/search/downloads/alternative"
