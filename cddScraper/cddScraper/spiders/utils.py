import pandas as pd
from scrapy.selector import Selector
import csv

def get_links_deputadas():

    links_deputadas = ["https://www.camara.leg.br/deputados/204528",
        "https://www.camara.leg.br/deputados/204545",
        "https://www.camara.leg.br/deputados/74057",
        "https://www.camara.leg.br/deputados/204353",
        "https://www.camara.leg.br/deputados/204400",
        "https://www.camara.leg.br/deputados/73696",
        "https://www.camara.leg.br/deputados/204509",
        "https://www.camara.leg.br/deputados/73701",
        "https://www.camara.leg.br/deputados/204374",
        "https://www.camara.leg.br/deputados/160589",
        "https://www.camara.leg.br/deputados/213762",
        "https://www.camara.leg.br/deputados/204507",
        "https://www.camara.leg.br/deputados/164360",
        "https://www.camara.leg.br/deputados/204369",
        "https://www.camara.leg.br/deputados/204380",
        "https://www.camara.leg.br/deputados/204462",
        "https://www.camara.leg.br/deputados/178928",
        "https://www.camara.leg.br/deputados/178939",
        "https://www.camara.leg.br/deputados/204459",
        "https://www.camara.leg.br/deputados/81297",
        "https://www.camara.leg.br/deputados/204434",
        "https://www.camara.leg.br/deputados/178994",
        "https://www.camara.leg.br/deputados/204421",
        "https://www.camara.leg.br/deputados/178989",
        "https://www.camara.leg.br/deputados/204525",
        "https://www.camara.leg.br/deputados/178945",
        "https://www.camara.leg.br/deputados/204357",
        "https://www.camara.leg.br/deputados/204535",
        "https://www.camara.leg.br/deputados/178961",
        "https://www.camara.leg.br/deputados/204360",
        "https://www.camara.leg.br/deputados/178946",
        "https://www.camara.leg.br/deputados/204534",
        "https://www.camara.leg.br/deputados/204464",
        "https://www.camara.leg.br/deputados/178901",
        "https://www.camara.leg.br/deputados/204466",
        "https://www.camara.leg.br/deputados/215044",
        "https://www.camara.leg.br/deputados/74784",
        "https://www.camara.leg.br/deputados/178866",
        "https://www.camara.leg.br/deputados/166402",
        "https://www.camara.leg.br/deputados/204458",
        "https://www.camara.leg.br/deputados/204471",
        "https://www.camara.leg.br/deputados/204430",
        "https://www.camara.leg.br/deputados/74398",
        "https://www.camara.leg.br/deputados/204540",
        "https://www.camara.leg.br/deputados/178956",
        "https://www.camara.leg.br/deputados/204428",
        "https://www.camara.leg.br/deputados/204432",
        "https://www.camara.leg.br/deputados/204453",
        "https://www.camara.leg.br/deputados/66179",
        "https://www.camara.leg.br/deputados/205535",
        "https://www.camara.leg.br/deputados/204377",
        "https://www.camara.leg.br/deputados/73943",
        "https://www.camara.leg.br/deputados/204529",
        "https://www.camara.leg.br/deputados/204565",
        "https://www.camara.leg.br/deputados/160639",
        "https://www.camara.leg.br/deputados/160641",
        "https://www.camara.leg.br/deputados/204467",
        "https://www.camara.leg.br/deputados/178925",
        "https://www.camara.leg.br/deputados/74075",
        "https://www.camara.leg.br/deputados/160575",
        "https://www.camara.leg.br/deputados/204407",
        "https://www.camara.leg.br/deputados/204354",
        "https://www.camara.leg.br/deputados/160598",
        "https://www.camara.leg.br/deputados/178966",
        "https://www.camara.leg.br/deputados/107283",
        "https://www.camara.leg.br/deputados/198197",
        "https://www.camara.leg.br/deputados/67138",
        "https://www.camara.leg.br/deputados/74848",
        "https://www.camara.leg.br/deputados/108338",
        "https://www.camara.leg.br/deputados/178839",
        "https://www.camara.leg.br/deputados/204468",
        "https://www.camara.leg.br/deputados/204546",
        "https://www.camara.leg.br/deputados/160534",
        "https://www.camara.leg.br/deputados/178832",
        "https://www.camara.leg.br/deputados/204375",
        "https://www.camara.leg.br/deputados/139285",
        "https://www.camara.leg.br/deputados/204405",
        "https://www.camara.leg.br/deputados/204410"]

    

    return links_deputadas


def get_links_deputados():
    links_deputados = ["https://www.camara.leg.br/deputados/141431",
    "https://www.camara.leg.br/deputados/92699",
    "https://www.camara.leg.br/deputados/204427",
    "https://www.camara.leg.br/deputados/204411",
    "https://www.camara.leg.br/deputados/141434",
    "https://www.camara.leg.br/deputados/191923",
    "https://www.camara.leg.br/deputados/204392",
    "https://www.camara.leg.br/deputados/204510",
    "https://www.camara.leg.br/deputados/204494",
    "https://www.camara.leg.br/deputados/204393",
    "https://www.camara.leg.br/deputados/115746",
    "https://www.camara.leg.br/deputados/160669",
    "https://www.camara.leg.br/deputados/204473",
    "https://www.camara.leg.br/deputados/204484",
    "https://www.camara.leg.br/deputados/204527",
    "https://www.camara.leg.br/deputados/204394",
    "https://www.camara.leg.br/deputados/74383",
    "https://www.camara.leg.br/deputados/204575",
    "https://www.camara.leg.br/deputados/204491",
    "https://www.camara.leg.br/deputados/74270",
    "https://www.camara.leg.br/deputados/204365",
    "https://www.camara.leg.br/deputados/160673",
    "https://www.camara.leg.br/deputados/178996",
    "https://www.camara.leg.br/deputados/74060",
    "https://www.camara.leg.br/deputados/178916",
    "https://www.camara.leg.br/deputados/204367",
    "https://www.camara.leg.br/deputados/204454",
    "https://www.camara.leg.br/deputados/204409",
    "https://www.camara.leg.br/deputados/160528",
    "https://www.camara.leg.br/deputados/62881",
    "https://www.camara.leg.br/deputados/160552",
    "https://www.camara.leg.br/deputados/116379",
    "https://www.camara.leg.br/deputados/205548",
    "https://www.camara.leg.br/deputados/204511",
    "https://www.camara.leg.br/deputados/204451",
    "https://www.camara.leg.br/deputados/178908",
    "https://www.camara.leg.br/deputados/204512",
    "https://www.camara.leg.br/deputados/204569",
    "https://www.camara.leg.br/deputados/164359",
    "https://www.camara.leg.br/deputados/204542",
    "https://www.camara.leg.br/deputados/160588",
    "https://www.camara.leg.br/deputados/178929",
    "https://www.camara.leg.br/deputados/160599",
    "https://www.camara.leg.br/deputados/143632",
    "https://www.camara.leg.br/deputados/160758",
    "https://www.camara.leg.br/deputados/204450",
    "https://www.camara.leg.br/deputados/204518",
    "https://www.camara.leg.br/deputados/204481",
    "https://www.camara.leg.br/deputados/204439",
    "https://www.camara.leg.br/deputados/204351",
    "https://www.camara.leg.br/deputados/204412",
    "https://www.camara.leg.br/deputados/204562",
    "https://www.camara.leg.br/deputados/141417",
    "https://www.camara.leg.br/deputados/74655",
    "https://www.camara.leg.br/deputados/204541",
    "https://www.camara.leg.br/deputados/92346",
    "https://www.camara.leg.br/deputados/204500",
    "https://www.camara.leg.br/deputados/178977",
    "https://www.camara.leg.br/deputados/141421",
    "https://www.camara.leg.br/deputados/141422",
    "https://www.camara.leg.br/deputados/204364",
    "https://www.camara.leg.br/deputados/160532",
    "https://www.camara.leg.br/deputados/204389",
    "https://www.camara.leg.br/deputados/178854",
    "https://www.camara.leg.br/deputados/198783",
    "https://www.camara.leg.br/deputados/161550",
    "https://www.camara.leg.br/deputados/132504",
    "https://www.camara.leg.br/deputados/204537",
    "https://www.camara.leg.br/deputados/160640",
    "https://www.camara.leg.br/deputados/204482",
    "https://www.camara.leg.br/deputados/178871",
    "https://www.camara.leg.br/deputados/178953",
    "https://www.camara.leg.br/deputados/68720",
    "https://www.camara.leg.br/deputados/178969",
    "https://www.camara.leg.br/deputados/141427",
    "https://www.camara.leg.br/deputados/171623",
    "https://www.camara.leg.br/deputados/204368",
    "https://www.camara.leg.br/deputados/160587",
    "https://www.camara.leg.br/deputados/66828",
    "https://www.camara.leg.br/deputados/204477",
    "https://www.camara.leg.br/deputados/72442",
    "https://www.camara.leg.br/deputados/204398",
    "https://www.camara.leg.br/deputados/204371",
    "https://www.camara.leg.br/deputados/160666",
    "https://www.camara.leg.br/deputados/204426",
    "https://www.camara.leg.br/deputados/141398",
    "https://www.camara.leg.br/deputados/204499",
    "https://www.camara.leg.br/deputados/204370",
    "https://www.camara.leg.br/deputados/178876",
    "https://www.camara.leg.br/deputados/204488",
    "https://www.camara.leg.br/deputados/141405",
    "https://www.camara.leg.br/deputados/73441",
    "https://www.camara.leg.br/deputados/204496",
    "https://www.camara.leg.br/deputados/204504",
    "https://www.camara.leg.br/deputados/205476",
    "https://www.camara.leg.br/deputados/204490",
    "https://www.camara.leg.br/deputados/141439",
    "https://www.camara.leg.br/deputados/204476",
    "https://www.camara.leg.br/deputados/204440",
    "https://www.camara.leg.br/deputados/74537",
    "https://www.camara.leg.br/deputados/141408",
    "https://www.camara.leg.br/deputados/204376",
    "https://www.camara.leg.br/deputados/204378",
    "https://www.camara.leg.br/deputados/204514",
    "https://www.camara.leg.br/deputados/178963",
    "https://www.camara.leg.br/deputados/135054",
    "https://www.camara.leg.br/deputados/204355",
    "https://www.camara.leg.br/deputados/141411",
    "https://www.camara.leg.br/deputados/74467",
    "https://www.camara.leg.br/deputados/152605",
    "https://www.camara.leg.br/deputados/204419",
    "https://www.camara.leg.br/deputados/74419",
    "https://www.camara.leg.br/deputados/204513",
    "https://www.camara.leg.br/deputados/160667",
    "https://www.camara.leg.br/deputados/204442",
    "https://www.camara.leg.br/deputados/73460",
    "https://www.camara.leg.br/deputados/204408",
    "https://www.camara.leg.br/deputados/204456",
    "https://www.camara.leg.br/deputados/204465",
    "https://www.camara.leg.br/deputados/204548",
    "https://www.camara.leg.br/deputados/178964",
    "https://www.camara.leg.br/deputados/178873",
    "https://www.camara.leg.br/deputados/204373",
    "https://www.camara.leg.br/deputados/178909",
    "https://www.camara.leg.br/deputados/204444",
    "https://www.camara.leg.br/deputados/73482",
    "https://www.camara.leg.br/deputados/204539",
    "https://www.camara.leg.br/deputados/178981",
    "https://www.camara.leg.br/deputados/73772",
    "https://www.camara.leg.br/deputados/178884",
    "https://www.camara.leg.br/deputados/178959",
    "https://www.camara.leg.br/deputados/141450",
    "https://www.camara.leg.br/deputados/160674",
    "https://www.camara.leg.br/deputados/109429",
    "https://www.camara.leg.br/deputados/141335",
    "https://www.camara.leg.br/deputados/204358",
    "https://www.camara.leg.br/deputados/178948",
    "https://www.camara.leg.br/deputados/204388",
    "https://www.camara.leg.br/deputados/141513",
    "https://www.camara.leg.br/deputados/204561",
    "https://www.camara.leg.br/deputados/160538",
    "https://www.camara.leg.br/deputados/74052",
    "https://www.camara.leg.br/deputados/204551",
    "https://www.camara.leg.br/deputados/204502",
    "https://www.camara.leg.br/deputados/93083",
    "https://www.camara.leg.br/deputados/204352",
    "https://www.camara.leg.br/deputados/204572",
    "https://www.camara.leg.br/deputados/178829",
    "https://www.camara.leg.br/deputados/204531",
    "https://www.camara.leg.br/deputados/178924",
    "https://www.camara.leg.br/deputados/204487",
    "https://www.camara.leg.br/deputados/141401",
    "https://www.camara.leg.br/deputados/204361",
    "https://www.camara.leg.br/deputados/178962",
    "https://www.camara.leg.br/deputados/178993",
    "https://www.camara.leg.br/deputados/204460",
    "https://www.camara.leg.br/deputados/74262",
    "https://www.camara.leg.br/deputados/141470",
    "https://www.camara.leg.br/deputados/204386",
    "https://www.camara.leg.br/deputados/204472",
    "https://www.camara.leg.br/deputados/204391",
    "https://www.camara.leg.br/deputados/160619",
    "https://www.camara.leg.br/deputados/74079",
    "https://www.camara.leg.br/deputados/204555",
    "https://www.camara.leg.br/deputados/74554",
    "https://www.camara.leg.br/deputados/209189",
    "https://www.camara.leg.br/deputados/74141",
    "https://www.camara.leg.br/deputados/204563",
    "https://www.camara.leg.br/deputados/215043",
    "https://www.camara.leg.br/deputados/204474",
    "https://www.camara.leg.br/deputados/204420",
    "https://www.camara.leg.br/deputados/74317",
    "https://www.camara.leg.br/deputados/204372",
    "https://www.camara.leg.br/deputados/73586",
    "https://www.camara.leg.br/deputados/204457",
    "https://www.camara.leg.br/deputados/204520",
    "https://www.camara.leg.br/deputados/204497",
    "https://www.camara.leg.br/deputados/204574",
    "https://www.camara.leg.br/deputados/204550",
    "https://www.camara.leg.br/deputados/178886",
    "https://www.camara.leg.br/deputados/204536",
    "https://www.camara.leg.br/deputados/151208",
    "https://www.camara.leg.br/deputados/98057",
    "https://www.camara.leg.br/deputados/178825",
    "https://www.camara.leg.br/deputados/204359",
    "https://www.camara.leg.br/deputados/204547",
    "https://www.camara.leg.br/deputados/74156",
    "https://www.camara.leg.br/deputados/74299",
    "https://www.camara.leg.br/deputados/92102",
    "https://www.camara.leg.br/deputados/74585",
    "https://www.camara.leg.br/deputados/204382",
    "https://www.camara.leg.br/deputados/196358",
    "https://www.camara.leg.br/deputados/204523",
    "https://www.camara.leg.br/deputados/204404",
    "https://www.camara.leg.br/deputados/178879",
    "https://www.camara.leg.br/deputados/74478",
    "https://www.camara.leg.br/deputados/178931",
    "https://www.camara.leg.br/deputados/178954",
    "https://www.camara.leg.br/deputados/204381",
    "https://www.camara.leg.br/deputados/160510",
    "https://www.camara.leg.br/deputados/204448",
    "https://www.camara.leg.br/deputados/160542",
    "https://www.camara.leg.br/deputados/150418",
    "https://www.camara.leg.br/deputados/204522",
    "https://www.camara.leg.br/deputados/160535",
    "https://www.camara.leg.br/deputados/204431",
    "https://www.camara.leg.br/deputados/204506",
    "https://www.camara.leg.br/deputados/74158",
    "https://www.camara.leg.br/deputados/178858",
    "https://www.camara.leg.br/deputados/204403",
    "https://www.camara.leg.br/deputados/204566",
    "https://www.camara.leg.br/deputados/178843",
    "https://www.camara.leg.br/deputados/75431",
    "https://www.camara.leg.br/deputados/204486",
    "https://www.camara.leg.br/deputados/74749",
    "https://www.camara.leg.br/deputados/141508",
    "https://www.camara.leg.br/deputados/188097",
    "https://www.camara.leg.br/deputados/178985",
    "https://www.camara.leg.br/deputados/92172",
    "https://www.camara.leg.br/deputados/154178",
    "https://www.camara.leg.br/deputados/178895",
    "https://www.camara.leg.br/deputados/204449",
    "https://www.camara.leg.br/deputados/204415",
    "https://www.camara.leg.br/deputados/146307",
    "https://www.camara.leg.br/deputados/74165",
    "https://www.camara.leg.br/deputados/178896",
    "https://www.camara.leg.br/deputados/204384",
    "https://www.camara.leg.br/deputados/204479",
    "https://www.camara.leg.br/deputados/74352",
    "https://www.camara.leg.br/deputados/178986",
    "https://www.camara.leg.br/deputados/194260",
    "https://www.camara.leg.br/deputados/74159",
    "https://www.camara.leg.br/deputados/204498",
    "https://www.camara.leg.br/deputados/74399",
    "https://www.camara.leg.br/deputados/178987",
    "https://www.camara.leg.br/deputados/204363",
    "https://www.camara.leg.br/deputados/73463",
    "https://www.camara.leg.br/deputados/73692",
    "https://www.camara.leg.br/deputados/204422",
    "https://www.camara.leg.br/deputados/204441",
    "https://www.camara.leg.br/deputados/204475",
    "https://www.camara.leg.br/deputados/204573",
    "https://www.camara.leg.br/deputados/160645",
    "https://www.camara.leg.br/deputados/204485",
    "https://www.camara.leg.br/deputados/204455",
    "https://www.camara.leg.br/deputados/162332",
    "https://www.camara.leg.br/deputados/204526",
    "https://www.camara.leg.br/deputados/204418",
    "https://www.camara.leg.br/deputados/179587",
    "https://www.camara.leg.br/deputados/156190",
    "https://www.camara.leg.br/deputados/179000",
    "https://www.camara.leg.br/deputados/146788",
    "https://www.camara.leg.br/deputados/204433",
    "https://www.camara.leg.br/deputados/76874",
    "https://www.camara.leg.br/deputados/133810",
    "https://www.camara.leg.br/deputados/204558",
    "https://www.camara.leg.br/deputados/204556",
    "https://www.camara.leg.br/deputados/178983",
    "https://www.camara.leg.br/deputados/179001",
    "https://www.camara.leg.br/deputados/81055",
    "https://www.camara.leg.br/deputados/204452",
    "https://www.camara.leg.br/deputados/215045",
    "https://www.camara.leg.br/deputados/178912",
    "https://www.camara.leg.br/deputados/122974",
    "https://www.camara.leg.br/deputados/204395",
    "https://www.camara.leg.br/deputados/122158",
    "https://www.camara.leg.br/deputados/160604",
    "https://www.camara.leg.br/deputados/178844",
    "https://www.camara.leg.br/deputados/204406",
    "https://www.camara.leg.br/deputados/204524",
    "https://www.camara.leg.br/deputados/73486",
    "https://www.camara.leg.br/deputados/204390",
    "https://www.camara.leg.br/deputados/204383",
    "https://www.camara.leg.br/deputados/204446",
    "https://www.camara.leg.br/deputados/178951",
    "https://www.camara.leg.br/deputados/204567",
    "https://www.camara.leg.br/deputados/141523",
    "https://www.camara.leg.br/deputados/74161",
    "https://www.camara.leg.br/deputados/73801",
    "https://www.camara.leg.br/deputados/73788",
    "https://www.camara.leg.br/deputados/215042",
    "https://www.camara.leg.br/deputados/204362",
    "https://www.camara.leg.br/deputados/160655",
    "https://www.camara.leg.br/deputados/160556",
    "https://www.camara.leg.br/deputados/160642",
    "https://www.camara.leg.br/deputados/204570",
    "https://www.camara.leg.br/deputados/160601",
    "https://www.camara.leg.br/deputados/204553",
    "https://www.camara.leg.br/deputados/74160",
    "https://www.camara.leg.br/deputados/171617",
    "https://www.camara.leg.br/deputados/141518",
    "https://www.camara.leg.br/deputados/141516",
    "https://www.camara.leg.br/deputados/178860",
    "https://www.camara.leg.br/deputados/204538",
    "https://www.camara.leg.br/deputados/193726",
    "https://www.camara.leg.br/deputados/160517",
    "https://www.camara.leg.br/deputados/160558",
    "https://www.camara.leg.br/deputados/204461",
    "https://www.camara.leg.br/deputados/204492",
    "https://www.camara.leg.br/deputados/74400",
    "https://www.camara.leg.br/deputados/133968",
    "https://www.camara.leg.br/deputados/141488",
    "https://www.camara.leg.br/deputados/90201",
    "https://www.camara.leg.br/deputados/213274",
    "https://www.camara.leg.br/deputados/178920",
    "https://www.camara.leg.br/deputados/204489",
    "https://www.camara.leg.br/deputados/152610",
    "https://www.camara.leg.br/deputados/160653",
    "https://www.camara.leg.br/deputados/204530",
    "https://www.camara.leg.br/deputados/204366",
    "https://www.camara.leg.br/deputados/141531",
    "https://www.camara.leg.br/deputados/74693",
    "https://www.camara.leg.br/deputados/204480",
    "https://www.camara.leg.br/deputados/160651",
    "https://www.camara.leg.br/deputados/178861",
    "https://www.camara.leg.br/deputados/122466",
    "https://www.camara.leg.br/deputados/178935",
    "https://www.camara.leg.br/deputados/73466",
    "https://www.camara.leg.br/deputados/74371",
    "https://www.camara.leg.br/deputados/178887",
    "https://www.camara.leg.br/deputados/73604",
    "https://www.camara.leg.br/deputados/160635",
    "https://www.camara.leg.br/deputados/178990",
    "https://www.camara.leg.br/deputados/204416",
    "https://www.camara.leg.br/deputados/160621",
    "https://www.camara.leg.br/deputados/74044",
    "https://www.camara.leg.br/deputados/74439",
    "https://www.camara.leg.br/deputados/178889",
    "https://www.camara.leg.br/deputados/204559",
    "https://www.camara.leg.br/deputados/160632",
    "https://www.camara.leg.br/deputados/204517",
    "https://www.camara.leg.br/deputados/160592",
    "https://www.camara.leg.br/deputados/204387",
    "https://www.camara.leg.br/deputados/178921",
    "https://www.camara.leg.br/deputados/73808",
    "https://www.camara.leg.br/deputados/178933",
    "https://www.camara.leg.br/deputados/204438",
    "https://www.camara.leg.br/deputados/204437",
    "https://www.camara.leg.br/deputados/204557",
    "https://www.camara.leg.br/deputados/74356",
    "https://www.camara.leg.br/deputados/204425",
    "https://www.camara.leg.br/deputados/178947",
    "https://www.camara.leg.br/deputados/92776",
    "https://www.camara.leg.br/deputados/177282",
    "https://www.camara.leg.br/deputados/178922",
    "https://www.camara.leg.br/deputados/143084",
    "https://www.camara.leg.br/deputados/204519",
    "https://www.camara.leg.br/deputados/160976",
    "https://www.camara.leg.br/deputados/197438",
    "https://www.camara.leg.br/deputados/178934",
    "https://www.camara.leg.br/deputados/157130",
    "https://www.camara.leg.br/deputados/178863",
    "https://www.camara.leg.br/deputados/195866",
    "https://www.camara.leg.br/deputados/160610",
    "https://www.camara.leg.br/deputados/74376",
    "https://www.camara.leg.br/deputados/141553",
    "https://www.camara.leg.br/deputados/204505",
    "https://www.camara.leg.br/deputados/204396",
    "https://www.camara.leg.br/deputados/74283",
    "https://www.camara.leg.br/deputados/137070",
    "https://www.camara.leg.br/deputados/204483",
    "https://www.camara.leg.br/deputados/141555",
    "https://www.camara.leg.br/deputados/204478",
    "https://www.camara.leg.br/deputados/204532",
    "https://www.camara.leg.br/deputados/178992",
    "https://www.camara.leg.br/deputados/160569",
    "https://www.camara.leg.br/deputados/178952",
    "https://www.camara.leg.br/deputados/160518",
    "https://www.camara.leg.br/deputados/74043"]

    return links_deputados



def get_csv_header():
    columns = ["nome", "genero","data_nascimento", 
    "presenca_plenario", "ausencia_plenario","ausencia_justificada_plenario", 
    "presenca_comissao", "ausencia_comissao","ausencia_justificada_comissao", 
    "gasto_total_par",
    "gasto_jan_par", "gasto_fev_par", "gasto_mar_par", "gasto_abr_par" , "gasto_maio_par",
    "gasto_junho_par", "gasto_jul_par", "gasto_agosto_par", "gasto_set_par",
    "gasto_out_par", "gasto_nov_par", "gasto_dez_par", 
    "gasto_total_gab", 
    "gasto_jan_gab", "gasto_fev_gab", "gasto_mar_gab","gasto_abr_gab" , "gasto_maio_gab", "gasto_junho_gab", 
    "gasto_jul_gab", "gasto_agosto_gab", "gasto_set_gab", "gasto_out_gab", "gasto_nov_gab", 
    "gasto_dez_gab", "salario_bruto", "quant_viagem"]


    return columns


def get_nome(response):
    nome = response.css("ul.informacoes-deputado").getall()
    nome = Selector(text=nome[0]).xpath('//li/text()').get()

    return nome.strip()


def get_info_plenario_comissao(response):
    try:
        plenario_com = response.css("ul.list-table__content").getall()
        plenario_com = Selector(text=plenario_com[0]).xpath('//dd/text()').getall()

        presenca_plen = int(plenario_com[0].split()[0])
        aus_just_plen = int(plenario_com[1].split()[0])
        aus_n_just_plen = int(plenario_com[2].split()[0])
        ausencia_plen = aus_just_plen + aus_n_just_plen

        presenca_com = int(plenario_com[3].split()[0])
        aus_just_com = int(plenario_com[4].split()[0])
        aus_n_just_com = int(plenario_com[5].split()[0])
        ausencia_com = aus_just_com + aus_n_just_com
    except:
        presenca_plen, ausencia_plen, aus_just_plen, presenca_com, ausencia_com, aus_just_com = 0,0,0,0,0,0

    return [presenca_plen, ausencia_plen, aus_just_plen, presenca_com, ausencia_com, aus_just_com]

def get_data_nascimento(response):

    data_nascimento = response.css("ul.informacoes-deputado").getall()
    # print("DATA NASCIMENTO: ", data_nascimento)
    try:
        data_nascimento = Selector(text=data_nascimento[0]).xpath('//li/text()').getall()[4].strip()
    except Exception as e:
        data_nascimento = Selector(text=data_nascimento[0]).xpath('//li/text()').getall()[1].strip()
    return data_nascimento


# Retorna os valores de gastos totais e mensais de cota parlamentar e verba de gabinete
def get_gastos_par_gab(response):
    gastos = []
    for result in response.xpath('//div[@class="gasto__col"]'):
            gasto = result.xpath('.//tbody//td/text()').getall()
            gastos.append(gasto)

    
    try:
        gasto_total_par = gastos[0][1]
    except:
        gasto_total_par = 0
    ordem_mes = {"JAN":0, "FEV":1, "MAR":2, "ABR":3, "MAI":4, "JUN":5, "JUL":6, "AGO":7, "SET":8, "OUT":9, "NOV":10, "DEZ":11}
    gastos_mes_par = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(gastos[1]), 3):
        gastos_mes_par[ordem_mes[gastos[1][i]]] = gastos[1][i+1].strip()
    
    gasto_total_gab = gastos[2][1]
    
    gastos_mes_gab = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(gastos[3]), 3):
        gastos_mes_gab[ordem_mes[gastos[3][i]]] = gastos[3][i+1].strip()
    

    return [gasto_total_par, gastos_mes_par, gasto_total_gab, gastos_mes_gab]


def get_salario_bruto(response):
    info_salarios = []
    for result in response.xpath('//div[@class="beneficio"]'):
        # Selector(text=result[0]).xpath('//a//h3//a/text()').getall()

        s = result.xpath('./a/text()').getall()
        info_salarios.append(s)
    
    salario = info_salarios[1][0].replace("\n", "").strip().replace(" ", "").replace("R$", "")
    return salario
    

def get_qtd_viagens(response):
    viagem = 0
    for result in response.xpath('//div[@class="beneficio beneficio__viagens"]'):
        viagem1 = result.xpath('./span/text()').get()
        viagem2 = result.xpath('./a/text()').get()
        if(viagem1 == None and viagem2 == None):
            viagem = 0
        elif(viagem1 != None and viagem2 == None):
            viagem = viagem1
        elif(viagem1 == None and viagem2 != None):
            viagem = viagem2

    return viagem

def build_csv(nome, genero, data_nasc, info_plen_com, gastos_par_gab, salario, qtd_viagens):
    info = [nome, genero, data_nasc, 
                          info_plen_com[0], info_plen_com[1], info_plen_com[2], info_plen_com[3], info_plen_com[4], info_plen_com[5],
                          gastos_par_gab[0], 
                          gastos_par_gab[1][0],gastos_par_gab[1][1],gastos_par_gab[1][2],gastos_par_gab[1][3],gastos_par_gab[1][4],
                          gastos_par_gab[1][5], gastos_par_gab[1][6],gastos_par_gab[1][7],gastos_par_gab[1][8],gastos_par_gab[1][9],
                          gastos_par_gab[1][10],gastos_par_gab[1][11],
                          gastos_par_gab[2],
                          gastos_par_gab[3][0],gastos_par_gab[3][1],gastos_par_gab[3][2],gastos_par_gab[3][3],gastos_par_gab[3][4],
                          gastos_par_gab[3][5], gastos_par_gab[3][6],gastos_par_gab[3][7],gastos_par_gab[3][8],gastos_par_gab[3][9],
                          gastos_par_gab[3][10],gastos_par_gab[3][11], 
                          salario, qtd_viagens]
    return info

            