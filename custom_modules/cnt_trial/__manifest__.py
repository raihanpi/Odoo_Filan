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

    'asset' :{
        'web.assets_backend' :[
            'cnt_trial/static/css/style.css'
            'cnt_trial/static/js/many2many_tags_field.js',
            'cnt_trial/static/js/systray.js',
            'cnt_trial/static/xml/systray.xml',
        ],
    },
    
    'auto_install': False,
    'application': False,
    
}