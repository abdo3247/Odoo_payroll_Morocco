# -*- encoding: utf-8 -*-
##############################################################################
#
#    
#    Copyright (C) 2016 rhfree (<http://rhfree.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'HR payroll Morocco',
    'category': 'Localization',
    'author': 'elmehdi',
    'website': 'www.eva-solutions.ma',
    "license": "AGPL-3",
    'version': '1.0',
    'depends': ['hr_payroll'],
    
	
    'description': """Moroccan Payroll Rules
======================

    * Paie selon les regles de la paie Marocaine
    * Gestion des abcences,
    * prime d'anciente
    * CNSS, AMO
    * CIMR...
	-Ceci est une version Basic, veuilluez nous contactez pour avoir une version personnaliser
    """,
    'active': False,
    'data': [
        'l10n_ma_hr_payroll_view.xml',
        'l10n_ma_hr_payroll_data.xml',
		'views/payslip_report_view.xml',
        'l10n_ma_hr_payroll_reports.xml',
     ],
    'installable': True,
}
