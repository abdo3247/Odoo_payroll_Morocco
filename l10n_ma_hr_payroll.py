

from openerp import api, models, fields

import openerp.addons.decimal_precision as dp



class hr_contract(models.Model):
    _inherit = 'hr.contract'
    _name = 'hr.contract'
    Heures_mois = fields.Integer(string='Heures de travail par mois', default='191',required=True)
    Avan_nature = fields.Float(string='Avantages en nature')
    Indemnite = fields.Float(string='Indemnités')


class res_company(models.Model):

    _inherit = 'res.company'
    _name = 'res.company'

    is_CIMR_worker = fields.Boolean(string=" CIMR contrat ouvrier")
    cimr_pat_worker = fields.Float(string="Contisation Patronale", digits_compute=dp.get_precision('Payroll'))
    cimr_sal_worker = fields.Float(string="Contisation Salariale", digits_compute=dp.get_precision('Payroll'))
    is_CIMR_employe = fields.Boolean(string="CIMR contrat Employé")
    cimr_pat_employe = fields.Float(string="Contisation Patronale", digits_compute=dp.get_precision('Payroll'))
    cimr_sal_employe = fields.Float(string="Contisation Salariale", digits_compute=dp.get_precision('Payroll'))
    is_CIMR_cadre = fields.Boolean(string="CIMR contrat Cadre")
    cimr_pat_cadre = fields.Float(string="Contisation Patronale", digits_compute=dp.get_precision('Payroll'))
    cimr_sal_cadre = fields.Float(string="Contisation Salariale", digits_compute=dp.get_precision('Payroll'))
    ass_comp = fields.Boolean(string="Assurance complementaire")
    ass_pat = fields.Float(string="Taux Contisation Patronale Assurance", digits_compute=dp.get_precision('Payroll'))
    ass_sal = fields.Float(string="Taux Contisation Salariale Assurance", digits_compute=dp.get_precision('Payroll'))


class hr_payslip(models.Model):
    _inherit = 'hr.payslip'
    _name = 'hr.payslip'

    payment_mode=fields.Char(string='Mode de paiement', required=False)


  

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    _name = 'hr.employee'

    cin = fields.Char(string='Numéro CIN')
    matricule_cnss = fields.Char(string='Numéro CNSS')


    matricule_cimr = fields.Char(string='Numéro CIMR')
    matricule_mut = fields.Char(string='Numéro MUTUELLE')
    abs = fields.Integer(string='Absence en heures')
    anc = fields.Selection([('0','inferieur a 2 ans'),('5','entre 2 et 5 ans'),('10','entre 5 et 12 ans'),('15','entre 12 et 25 ans'), ('25','superieur a 25 ans')],'Taux d\'anciente' ,default='0' ,required=True)
    hs25 = fields.Float(string='Heures sup à 25')
    hs50 = fields.Float(string='Heures sup à 50')
    hs100 = fields.Float(string='Heures sup à 100')
    Prime = fields.Float(string='primes et gratifications')
    AvaRet = fields.Float(string='Avance ou Retenue de Salaire Net')
    Remboursement =fields.Float(string='Remboursement Net')





	
    
		

		
		
		
	
