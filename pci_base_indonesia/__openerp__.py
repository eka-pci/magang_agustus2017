# -*- coding: utf-8 -*-
{
    "name": "Base Indonesia",
    "version": "1.0",
    "author": "Port Cities",
    "website": "http://portcitiesindonesia.com",
    "category": "Branch module",
    "depends": ["product", "stock", "account"],
    "description": """
    - Information partner for indonesian customer or vendor
    - Product tag
    
\n
1.1
tax fields move to l10n_id_laris

v1.1
----
* add menu branch in settings
* add field analytic account 
* replace action window customers

v1.2
----
* automatic create analytic account on branch

v1.3
----
* create menu salesman

v1.4
----
* create field many2many (branch_ids)

*Author : Eka

*Author : Eka



""",
    "demo_xml":[],
    "data":[
        "security/ir.model.access.csv",
        "security/stock.location.csv",
        "views/res_partner.xml",
        "views/stock.xml",
    ],
    "active": False,
    "installable": True,
    "auto_install": False
}
