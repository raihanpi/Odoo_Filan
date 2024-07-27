{
    'name': 'trial',
    'version': '1.0',
    'description': 'trial',
    'summary': 'trial',
    'author': 'cnt',
    'depends': [
        'cnt_pm'
    ],
    'data': [
        'views/mitra.views.xml',
        'security/ir.model.access.csv',
        'views/mitra_detail.views.xml',
        # 'views/asset.views.xml'
    ],

    # 'asset' :{
    #     'web.assets_backend' :[
    #         'cnt_trial/static/css/style.css'
    #     ],
    # },
    
    'auto_install': False,
    'application': False,
    
}